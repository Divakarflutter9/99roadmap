# Email Configuration Guide for 99Roadmap

## Option 1: Gmail SMTP (Recommended for Testing)

### Step 1: Enable App Passwords in Gmail
1. Go to your Google Account settings
2. Security → 2-Step Verification → App passwords
3. Generate an app password for "Mail"
4. Copy the 16-character password

### Step 2: Add to .env file
```env
# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
DEFAULT_FROM_EMAIL=99Roadmap <your-email@gmail.com>
```

### Step 3: Update settings.py
```python
# Email Configuration
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', '99Roadmap <noreply@99roadmap.com>')
SITE_URL = os.getenv('SITE_URL', 'http://127.0.0.1:8000')
```

---

## Option 2: SendGrid (Recommended for Production)

### Step 1: Create SendGrid Account
1. Sign up at https://sendgrid.com
2. Verify your sender email
3. Create an API key

### Step 2: Install SendGrid
```bash
pip install sendgrid
```

### Step 3: Add to .env
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=99Roadmap <noreply@99roadmap.com>
```

---

## Option 3: AWS SES (For High Volume)

### Step 1: Set up AWS SES
1. Go to AWS Console → SES
2. Verify your domain or email
3. Create SMTP credentials

### Step 2: Add to .env
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-smtp-username
EMAIL_HOST_PASSWORD=your-smtp-password
DEFAULT_FROM_EMAIL=99Roadmap <noreply@99roadmap.com>
```

---

## Testing Email Configuration

### Test in Django Shell
```python
python manage.py shell

from django.core.mail import send_mail

send_mail(
    'Test Email',
    'This is a test email from 99Roadmap',
    'noreply@99roadmap.com',
    ['your-email@example.com'],
    fail_silently=False,
)
```

### Expected Behavior
- Welcome emails on registration ✅
- Password reset emails ✅
- Contact form submissions ✅
- Notification emails ✅

---

## Current Email Templates

1. `templates/emails/welcome.html` - Welcome email
2. `templates/emails/reset_password.html` - Password reset
3. Contact form sends to `DEFAULT_FROM_EMAIL`

---

## Troubleshooting

### Emails not sending?
1. Check `.env` file has correct credentials
2. Verify `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`
3. Check spam folder
4. Enable "Less secure app access" for Gmail (not recommended)
5. Use app-specific password for Gmail

### 535 Authentication Failed
- Wrong password or username
- Use app password for Gmail
- Check 2FA settings

### Connection Timeout
- Check `EMAIL_PORT` and `EMAIL_USE_TLS`
- Verify firewall/network settings

---

## Production Best Practices

1. **Use SendGrid or AWS SES** for production
2. **Never commit credentials** to Git
3. **Use environment variables** for all email settings
4. **Monitor email deliverability** with SendGrid dashboard
5. **Implement email rate limiting** to prevent spam
6. **Set up SPF and DKIM records** for your domain
7. **Use a dedicated sending domain** (e.g., mail.99roadmap.com)
