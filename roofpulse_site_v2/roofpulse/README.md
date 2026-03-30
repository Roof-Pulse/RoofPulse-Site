# RoofPulse 🏠⚡

**Never Miss a Roofing Lead Again.**

A lead-converting website with automated email notifications — when a roofer fills out the form, you get a notification email instantly and they get a branded confirmation email automatically.

---

## What This Does

- **Landing page** that sells the RoofPulse service to roofing companies
- **Live demo simulator** — visitors watch the automated text-back system in real time
- **Contact form** — captures name, company, phone, email, missed calls/week
- **Emails you instantly** when a new lead signs up (beautiful HTML email)
- **Emails the roofer** a branded confirmation with next steps
- **Thank you page** — sets expectations after sign-up

---

## ⚡ Quick Setup (Gmail Email)

### Step 1 — Get a Gmail App Password
Gmail requires an "App Password" (not your regular password) for SMTP.

1. Go to your Google Account → **Security**
2. Enable **2-Step Verification** if not already on
3. Go to **Security → App Passwords**
4. Select app: **Mail** · Select device: **Other** → type "RoofPulse"
5. Click **Generate** — copy the 16-character password

### Step 2 — Set Environment Variables

**On Render.com (recommended):**
In your service dashboard → Environment → Add these:
```
GMAIL_USER  =  Hayesscale500@gmail.com
GMAIL_PASS  =  your-16-char-app-password
OWNER_EMAIL =  Hayesscale500@gmail.com
```

**Running locally:**
```bash
export GMAIL_USER="Hayesscale500@gmail.com"
export GMAIL_PASS="your-16-char-app-password"
export OWNER_EMAIL="Hayesscale500@gmail.com"
python app.py
```

---

## Local Setup

```bash
git clone https://github.com/YOURUSERNAME/roofpulse.git
cd roofpulse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit: `http://localhost:5000`

---

## Deploy Free (Render.com)

1. Push repo to GitHub
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variables (see above)
6. Deploy — live in ~3 minutes

---

## Project Structure

```
roofpulse/
├── app.py                  # Flask app + email logic
├── requirements.txt
├── Procfile
├── README.md
└── templates/
    ├── landing.html        # Full landing page + demo simulator
    └── thankyou.html       # Post-submission page
```

---

## How the Emails Work

**You receive:** A bold red notification email with all lead details and a one-click "Reply Now" button

**They receive:** A branded RoofPulse confirmation email with the 4 next steps, what to expect, and a personal tone that reinforces you're local and real

Both emails are fully HTML — they look professional in Gmail, Apple Mail, and on mobile.

---

Built by RoofPulse · Collierville, TN
