"""
Django Admin Configuration for 99Roadmap Platform
Complete admin interface for managing all models
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from nested_admin import NestedModelAdmin, NestedTabularInline
from .models import (
    User, RoadmapCategory, Roadmap, Stage, Topic, Quiz, QuizQuestion, QuizOption, RoadmapBundle,
    UserRoadmapEnrollment, UserTopicProgress, UserQuizAttempt, UserGamification, XPTransaction
)


class UserRoadmapEnrollmentInline(admin.TabularInline):
    model = UserRoadmapEnrollment
    extra = 0
    fields = ['roadmap', 'enrolled_at', 'progress_percentage_display', 'delete_button']
    readonly_fields = ['enrolled_at', 'progress_percentage_display', 'delete_button']
    can_delete = True
    show_change_link = True
    
    def progress_percentage_display(self, obj):
        return f"{obj.get_progress_percentage()}%"
    progress_percentage_display.short_description = 'Progress'

    def delete_button(self, obj):
        if obj.id:
            from django.urls import reverse
            url = reverse('admin:core_userroadmapenrollment_delete', args=[obj.id])
            return format_html(
                '<a href="{}" style="display: inline-block; background-color: #ba2121; color: white !important; padding: 5px 12px; border-radius: 4px; text-decoration: none; font-weight: bold; font-size: 11px; text-transform: uppercase;">Unenroll / Delete</a>',
                url
            )
        return ""
    delete_button.short_description = 'Action'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Enhanced admin for custom User model"""
    
    list_display = ['email', 'full_name', 'study_type', 'branch', 'is_verified', 'is_active', 'date_joined']
    list_filter = ['is_verified', 'is_active', 'study_type', 'date_joined']
    search_fields = ['email', 'full_name', 'phone', 'branch', 'college']
    ordering = ['-date_joined']
    
    fieldsets = (
        ('Account', {'fields': ('email', 'password', 'is_verified', 'verification_token')}),
        ('Personal Info', {'fields': ('full_name', 'phone', 'profile_image', 'bio')}),
        ('Academic Info', {'fields': ('study_type', 'branch', 'year', 'college')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    
    readonly_fields = ['date_joined', 'last_login']
    
    inlines = [UserRoadmapEnrollmentInline]


@admin.register(RoadmapCategory)
class RoadmapCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'colored_icon', 'order', 'roadmaps_count']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    
    def colored_icon(self, obj):
        return format_html(
            '<i class="{}" style="color: {}; font-size: 20px;"></i>',
            obj.icon, obj.color
        )
    colored_icon.short_description = 'Icon'
    
    def roadmaps_count(self, obj):
        return obj.roadmaps.count()
    roadmaps_count.short_description = 'Roadmaps'


class TopicInline(NestedTabularInline):
    model = Topic
    extra = 1
    fields = ['order', 'title', 'content_type', 'duration_minutes', 'xp_reward']
    ordering = ['order']


class StageInline(NestedTabularInline):
    model = Stage
    extra = 1
    fields = ['order', 'title', 'is_free', 'required_xp', 'xp_reward']
    ordering = ['order']
    inlines = [TopicInline]


@admin.register(Roadmap)
class RoadmapAdmin(NestedModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'is_premium', 'price', 'total_stages', 'enrolled_count', 'is_active', 'is_featured']
    list_filter = ['category', 'difficulty', 'is_premium', 'is_active', 'is_featured']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_active', 'is_featured']
    
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'slug', 'short_description', 'description', 'category', 'difficulty')}),
        ('Visual', {'fields': ('thumbnail', 'banner', 'pdf_file')}),
        ('Pricing', {'fields': ('is_premium', 'price')}),
        ('Stats', {'fields': ('total_stages', 'estimated_hours', 'enrolled_count')}),
        ('Status', {'fields': ('is_active', 'is_featured')}),
    )
    
    readonly_fields = ['total_stages', 'enrolled_count']
    inlines = [StageInline]
    
    actions = ['activate_roadmaps', 'deactivate_roadmaps', 'feature_roadmaps']
    
    def activate_roadmaps(self, request, queryset):
        queryset.update(is_active=True)
    activate_roadmaps.short_description = "Activate selected roadmaps"
    
    def deactivate_roadmaps(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_roadmaps.short_description = "Deactivate selected roadmaps"
    
    def feature_roadmaps(self, request, queryset):
        queryset.update(is_featured=True)
    feature_roadmaps.short_description = "Feature selected roadmaps"


@admin.register(RoadmapBundle)
class RoadmapBundleAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'get_roadmaps_count', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['roadmaps']


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'roadmap', 'order', 'is_free', 'required_xp', 'topics_count']
    list_filter = ['roadmap', 'is_free']
    search_fields = ['title', 'roadmap__title']
    
    inlines = [TopicInline]
    
    def topics_count(self, obj):
        return obj.get_topics_count()
    topics_count.short_description = 'Topics'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'stage', 'content_type', 'order', 'duration_minutes', 'xp_reward']
    list_filter = ['content_type', 'stage__roadmap']
    search_fields = ['title', 'content']


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1
    fields = ['order', 'question_text', 'question_type']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'stage', 'passing_score', 'time_limit', 'xp_reward', 'is_required', 'questions_count']
    list_filter = ['is_required', 'stage__roadmap']
    search_fields = ['title', 'stage__title']
    
    inlines = [QuizQuestionInline]
    
    def questions_count(self, obj):
        return obj.get_questions_count()
    questions_count.short_description = 'Questions'


class QuizOptionInline(admin.TabularInline):
    model = QuizOption
    extra = 4
    fields = ['order', 'option_text', 'is_correct']


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'question_type', 'order', 'question_preview']
    list_filter = ['question_type', 'quiz__stage__roadmap']
    search_fields = ['question_text']
    
    inlines = [QuizOptionInline]
    
    def question_preview(self, obj):
        return obj.question_text[:100]
    question_preview.short_description = 'Question'


@admin.register(UserRoadmapEnrollment)
class UserRoadmapEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'roadmap', 'enrolled_at', 'progress_bar', 'current_stage', 'completed_at']
    list_filter = ['enrolled_at', 'roadmap']
    search_fields = ['user__email', 'user__full_name', 'roadmap__title']
    readonly_fields = ['enrolled_at', 'last_accessed']
    
    def progress_bar(self, obj):
        percentage = obj.get_progress_percentage()
        return format_html(
            '<div style="width:100px; background-color:#ddd; border-radius:5px;">'
            '<div style="width:{}%; background-color:#4CAF50; height:20px; border-radius:5px; text-align:center; color:white;">{}%</div>'
            '</div>',
            percentage, percentage
        )
    progress_bar.short_description = 'Progress'


@admin.register(UserTopicProgress)
class UserTopicProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'is_completed', 'completed_at', 'time_spent_minutes']
    list_filter = ['is_completed', 'topic__stage__roadmap']
    search_fields = ['user__email', 'topic__title']
    readonly_fields = ['completed_at']
    
    def time_spent_minutes(self, obj):
        return f"{obj.time_spent // 60} min"
    time_spent_minutes.short_description = 'Time Spent'


@admin.register(UserQuizAttempt)
class UserQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'passed_badge', 'started_at', 'time_taken_display']
    list_filter = ['passed', 'quiz__stage__roadmap', 'started_at']
    search_fields = ['user__email', 'quiz__title']
    readonly_fields = ['started_at', 'completed_at']
    
    def passed_badge(self, obj):
        if obj.passed:
            return format_html('<span style="color:green; font-weight:bold;">✓ PASSED</span>')
        return format_html('<span style="color:red; font-weight:bold;">✗ FAILED</span>')
    passed_badge.short_description = 'Status'
    
    def time_taken_display(self, obj):
        return f"{obj.time_taken // 60}m {obj.time_taken % 60}s"
    time_taken_display.short_description = 'Time Taken'


@admin.register(UserGamification)
class UserGamificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'level_badge', 'total_xp', 'current_streak', 'topics_completed', 'quizzes_passed', 'roadmaps_completed']
    list_filter = ['level', 'last_activity_date']
    search_fields = ['user__email', 'user__full_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('XP & Level', {'fields': ('total_xp', 'level')}),
        ('Streaks', {'fields': ('current_streak', 'longest_streak', 'last_activity_date')}),
        ('Stats', {'fields': ('total_time_spent', 'topics_completed', 'quizzes_passed', 'roadmaps_completed')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def level_badge(self, obj):
        colors = {1: '#CD7F32', 2: '#C0C0C0', 3: '#FFD700', 4: '#E5E4E2', 5: '#B9F2FF'}
        color = colors.get(min(obj.level, 5), '#6366f1')
        return format_html(
            '<span style="background:{}; color:white; padding:5px 10px; border-radius:15px; font-weight:bold;">Level {}</span>',
            color, obj.level
        )
    level_badge.short_description = 'Level'


@admin.register(XPTransaction)
class XPTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_display', 'action', 'description', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['user__email', 'description']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def amount_display(self, obj):
        color = '#4CAF50' if obj.amount > 0 else '#F44336'
        return format_html(
            '<span style="color:{}; font-weight:bold;">{:+d} XP</span>',
            color, obj.amount
        )
    amount_display.short_description = 'XP'


# Register remaining models
admin.site.register(QuizOption)

# Customize admin site
admin.site.site_header = "99Roadmap Admin"
admin.site.site_title = "99Roadmap Admin Portal"
admin.site.index_title = "Welcome to 99Roadmap Administration"
