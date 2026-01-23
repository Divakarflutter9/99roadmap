# Google Sign-In Setup Guide

The code for "Sign in with Google" is ready! Now you need to get the API keys from Google and add them to your website.

## 1. Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a **New Project**.
3. Name it "99Roadmap" (or your app name).

## 2. Configure Consent Screen
1. In the left menu, go to **APIs & Services > OAuth consent screen**.
2. Select **External** and click **Create**.
3. Fill in:
   - **App Name**: 99Roadmap
   - **User Support Email**: Your email
   - **Developer Contact Info**: Your email
4. Click **Save and Continue**.
5. Skipping Scopes is fine for now (setup default email/profile).
6. **Test Users**: Add your own email so you can test it.

## 3. Get Credentials (Client ID & Secret)
1. Go to **APIs & Services > Credentials**.
2. Click **+ CREATE CREDENTIALS** > **OAuth client ID**.
3. **Application Type**: Web application.
4. **Name**: 99Roadmap Web Client.
5. **Authorized JavaScript origins**:
   - `http://127.0.0.1:8000`
   - `http://localhost:8000`
   - (Add your production domain later, e.g., `https://99roadmap.com`)
6. **Authorized redirect URIs**:
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
   - `http://localhost:8000/accounts/google/login/callback/`
   - (Production: `https://99roadmap.com/accounts/google/login/callback/`)
7. Click **Create**.
8. **Copy** the `Client ID` and `Client Secret`.

## 4. Add Keys to Django Admin
1. Run your server: `python manage.py runserver`
2. Go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
3. Log in as superuser.
4. Under **Social Accounts**, click **Social applications**.
5. Click **Add social application**.
6. Fill in:
   - **Provider**: Google
   - **Name**: Google OAuth
   - **Client id**: (Paste from Google)
   - **Secret key**: (Paste from Google)
   - **Sites**: Select `example.com` (Move it to the right box).
7. Click **Save**.

## 5. Test It!
Go to the [Login Page](http://127.0.0.1:8000/login/) and click **Continue with Google**.
