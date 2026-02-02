"""
Forms for 99Roadmap Platform
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import User, UserTopicProgress, WeeklyGoal

class WeeklyGoalForm(forms.ModelForm):
    """Form to set weekly goals"""
    
    target_value = forms.IntegerField(
        label="Topics to Complete this Week",
        min_value=1,
        max_value=50,
        initial=5,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 5'
        })
    )
    
    class Meta:
        model = WeeklyGoal
        fields = ['target_value']

from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """Registration form with extended user fields"""
    
    full_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )
    
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        })
    )
    
    study_type = forms.ChoiceField(
        choices=User.STUDY_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    branch = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Branch/Department (e.g., CSE, ECE, Mechanical)'
        })
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password (min 8 characters with letters)'
        }),
        help_text="Must be at least 8 characters with letters"
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter Password'
        })
    )
    
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'study_type', 'branch', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if not phone:
            raise ValidationError("Phone number is required.")
            
        # 1. Must contain only digits
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")
            
        # 2. Must be exactly 10 digits
        if len(phone) != 10:
            raise ValidationError(f"Phone number must be exactly 10 digits. You entered {len(phone)}.")
            
        # 3. Must start with 5, 6, 7, 8, or 9
        if int(phone[0]) < 5:
            raise ValidationError("Phone number must accept valid numbers (starts with 5-9).")
            
        # 4. Check for uniqueness
        if User.objects.filter(phone=phone).exists():
            raise ValidationError("This phone number is already registered.")
            
        return phone


class UserLoginForm(AuthenticationForm):
    """Login form with custom styling - accepts email or phone"""
    
    username = forms.CharField(
        label="Email or Phone",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address or Phone Number',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = None
            # Try to authenticate by Email
            if '@' in username:
                user = authenticate(username=username, password=password)
            else:
                # Try to authenticate by Phone
                try:
                    user_obj = User.objects.get(phone=username)
                    # Authenticate using the email associated with this phone
                    user = authenticate(username=user_obj.email, password=password)
                except User.DoesNotExist:
                    pass
                except User.MultipleObjectsReturned:
                    # Handle case where multiple users have same phone (shouldn't happen with unique constraint)
                    raise forms.ValidationError("Multiple accounts found with this phone number. Please contact support.")
            
            if user is None:
                raise forms.ValidationError("Invalid email/phone or password.")
            
            self.user_cache = user # Important for AuthenticationForm
            
        return self.cleaned_data



class UserProfileForm(forms.ModelForm):
    """Form for updating user profile"""
    
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'study_type', 'branch', 'year', 'college', 'bio', 'profile_image', 'future_goals']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'study_type': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'future_goals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What are your career goals? e.g. Become a Full Stack Developer'}),
        }


class UserAvatarForm(forms.ModelForm):
    """Form for updating just the profile image"""
    class Meta:
        model = User
        fields = ['profile_image']


class QuizSubmissionForm(forms.Form):
    """Dynamic form for quiz submission"""
    
    def __init__(self, quiz, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for question in quiz.questions.all():
            field_name = f'question_{question.id}'
            
            if question.question_type == 'single':
                choices = [(opt.id, opt.option_text) for opt in question.options.all()]
                self.fields[field_name] = forms.ChoiceField(
                    label=question.question_text,
                    choices=choices,
                    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                    required=True
                )
            
            elif question.question_type == 'multiple':
                choices = [(opt.id, opt.option_text) for opt in question.options.all()]
                self.fields[field_name] = forms.MultipleChoiceField(
                    label=question.question_text,
                    choices=choices,
                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                    required=True
                )
            
            elif question.question_type == 'truefalse':
                self.fields[field_name] = forms.ChoiceField(
                    label=question.question_text,
                    choices=[('true', 'True'), ('false', 'False')],
                    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                    required=True
                )
