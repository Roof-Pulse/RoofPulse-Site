# RoofPulse 🏠⚡

**Never Miss a Roofing Lead Again.**

A lead-converting website that demonstrates automated missed call recovery, AI follow-up, and appointment booking for roofing companies — built with Python/Flask.

---

## What This Does

- **Landing page** that sells the RoofPulse service to roofing companies
- **Live demo simulator** — visitors can enter a name/phone and watch the automated text-back system respond in real time
- **Contact/lead capture form** — sends inquiries directly to you
- **Thank you page** — sets expectations after sign-up

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOURUSERNAME/roofpulse.git
cd roofpulse

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
python app.py
```

Visit: `http://localhost:5000`

---

## Deploy Free (Render.com — Recommended)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Hit Deploy — your site is live in ~3 minutes

**Free tier is enough** to run this for prospects.

---

## Project Structure

```
roofpulse/
├── app.py                  # Flask routes
├── requirements.txt        # Dependencies
├── Procfile               # For deployment
├── templates/
│   ├── landing.html       # Main landing page
│   └── thankyou.html      # Post-form submission
└── README.md
```

---

## Customization

**To update your contact info:**
Edit `templates/landing.html` — search for "Collierville" and replace with your details.

**To connect a real form backend:**
In `app.py`, update the `/contact` route to send an email or SMS notification using Twilio/SendGrid.

**To add Google Analytics:**
Add your GA4 tag in the `<head>` of `landing.html`.

---

Built by RoofPulse · Collierville, TN
