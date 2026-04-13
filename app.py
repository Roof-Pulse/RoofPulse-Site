from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import os, threading, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

OWNER_EMAIL = os.environ.get("OWNER_EMAIL", "Hayesscale500@gmail.com")
SMTP_HOST   = os.environ.get("SMTP_HOST",   "smtp.resend.com")
SMTP_PORT   = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USER   = os.environ.get("SMTP_USER",   "resend")
SMTP_PASS   = os.environ.get("SMTP_PASS",   "")
FROM_EMAIL  = os.environ.get("FROM_EMAIL",  "onboarding@resend.dev")

DEMO_LEADS = [
    {"id": 1, "name": "Mike Johnson",   "phone": "(901) 555-0142", "status": "Booked",     "source": "Missed Call", "value": 8500,  "time": "2 mins ago"},
    {"id": 2, "name": "Sarah Williams", "phone": "(901) 555-0287", "status": "Responding", "source": "Missed Call", "value": 12000, "time": "11 mins ago"},
    {"id": 3, "name": "David Chen",     "phone": "(901) 555-0391", "status": "Booked",     "source": "Web Form",    "value": 6800,  "time": "34 mins ago"},
    {"id": 4, "name": "Amanda Torres",  "phone": "(901) 555-0456", "status": "New",        "source": "Missed Call", "value": 9200,  "time": "1 hr ago"},
    {"id": 5, "name": "Robert Hill",    "phone": "(901) 555-0512", "status": "Booked",     "source": "Referral",    "value": 15000, "time": "2 hrs ago"},
]
leads = []


def _send(to_addr, subject, html_body):
    if not SMTP_PASS:
        print(f"[EMAIL SKIPPED] No SMTP_PASS. Would send to {to_addr}: {subject}")
        return
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = f"RoofPulse <{FROM_EMAIL}>"
        msg["To"]      = to_addr
        msg.attach(MIMEText(html_body, "html"))
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=20) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(FROM_EMAIL, to_addr, msg.as_string())
        print(f"[EMAIL OK] {to_addr}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")


def send_async(to_addr, subject, html_body):
    threading.Thread(target=_send, args=(to_addr, subject, html_body), daemon=True).start()


def owner_email(name, company, phone, email, missed_calls, submitted_at):
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:'Helvetica Neue',Arial,sans-serif;background:#0D1117;margin:0;padding:40px 20px}}
.w{{max-width:560px;margin:0 auto}}
.hd{{background:#E63946;border-radius:10px 10px 0 0;padding:28px 36px;text-align:center}}
.hd h1{{font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#ffffff80;margin:0 0 6px}}
.hd h2{{font-size:26px;font-weight:900;color:#fff;margin:0}}
.bd{{background:#161B22;border:1px solid #ffffff10;border-top:none;border-radius:0 0 10px 10px;padding:32px 36px}}
.hl{{background:#E6394610;border:1px solid #E6394630;border-radius:8px;padding:18px 22px;margin-bottom:24px}}
.hl p{{font-size:14px;color:#cdd9e5;margin:0;line-height:1.6}}
.hl strong{{color:#E63946}}
.fl{{margin-bottom:16px}}
.fl-l{{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8B949E;margin-bottom:5px}}
.fl-v{{font-size:15px;color:#F0F6FC;font-weight:600;background:#0D1117;border:1px solid #ffffff10;border-radius:5px;padding:10px 14px}}
hr{{border:none;border-top:1px solid #ffffff10;margin:24px 0}}
.cta{{display:block;text-align:center;background:#E63946;color:#fff;font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;text-decoration:none;padding:14px 28px;border-radius:5px}}
.ft{{text-align:center;padding:20px;font-size:11px;color:#8B949E}}
</style></head><body>
<div class="w">
  <div class="hd"><h1>RoofPulse</h1><h2>🔥 New Pilot Request</h2></div>
  <div class="bd">
    <div class="hl"><p><strong>{name}</strong> from <strong>{company}</strong> just requested a free 14-day pilot. They estimate missing <strong>{missed_calls}</strong> per week. Reach out within the hour.</p></div>
    <div class="fl"><div class="fl-l">Name</div><div class="fl-v">{name}</div></div>
    <div class="fl"><div class="fl-l">Company</div><div class="fl-v">{company}</div></div>
    <div class="fl"><div class="fl-l">Phone</div><div class="fl-v">{phone}</div></div>
    <div class="fl"><div class="fl-l">Email</div><div class="fl-v">{email}</div></div>
    <div class="fl"><div class="fl-l">Missed Calls/Week</div><div class="fl-v">{missed_calls}</div></div>
    <div class="fl"><div class="fl-l">Submitted</div><div class="fl-v">{submitted_at}</div></div>
    <hr>
    <a href="mailto:{email}" class="cta">Reply to {name} Now →</a>
  </div>
  <div class="ft">RoofPulse · Collierville, TN</div>
</div></body></html>"""


def prospect_email(name, company):
    first = name.split()[0]
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:'Helvetica Neue',Arial,sans-serif;background:#0D1117;margin:0;padding:40px 20px}}
.w{{max-width:560px;margin:0 auto}}
.hd{{background:#0D1117;border:1px solid #ffffff10;border-bottom:none;border-radius:10px 10px 0 0;padding:36px;text-align:center}}
.logo{{font-size:24px;font-weight:900;letter-spacing:4px;color:#fff;margin-bottom:20px;display:block}}
.logo span{{color:#E63946}}
.circle{{width:68px;height:68px;background:#16803420;border:2px solid #16803460;border-radius:50%;font-size:28px;margin:0 auto 18px;line-height:68px;text-align:center}}
.hd h1{{font-size:26px;font-weight:900;color:#fff;margin:0 0 6px}}
.hd p{{font-size:14px;color:#8B949E;margin:0}}
.bd{{background:#161B22;border:1px solid #ffffff10;border-top:none;border-radius:0 0 10px 10px;padding:32px 36px}}
.greet{{font-size:15px;color:#F0F6FC;line-height:1.75;margin-bottom:28px}}
.greet strong{{color:#E63946}}
.step{{display:flex;gap:14px;align-items:flex-start;margin-bottom:18px}}
.sn{{background:#E63946;color:#fff;width:30px;height:30px;border-radius:50%;font-size:13px;font-weight:700;flex-shrink:0;line-height:30px;text-align:center;margin-top:1px}}
.stitle{{font-size:14px;font-weight:700;color:#F0F6FC;margin-bottom:3px}}
.sdesc{{font-size:12px;color:#8B949E;line-height:1.55}}
hr{{border:none;border-top:1px solid #ffffff10;margin:24px 0}}
.ft{{text-align:center;font-size:12px;color:#8B949E;line-height:1.6}}
</style></head><body>
<div class="w">
  <div class="hd">
    <span class="logo">ROOF<span>PULSE</span></span>
    <div class="circle">✅</div>
    <h1>You're confirmed, {first}.</h1>
    <p>Your free 14-day pilot request has been received.</p>
  </div>
  <div class="bd">
    <p class="greet">Hey {first} — this is Hayden, not an auto-reply bot. I'm local to Collierville and I personally set up every system. I'll be reaching out to you at <strong>{company}</strong> within the next few hours.</p>
    <div class="step"><div class="sn">1</div><div><div class="stitle">I'll reach out personally</div><div class="sdesc">Expect a call or text within 2–4 hours to confirm your details.</div></div></div>
    <div class="step"><div class="sn">2</div><div><div class="stitle">30-minute setup call</div><div class="sdesc">I configure everything. You don't touch any software.</div></div></div>
    <div class="step"><div class="sn">3</div><div><div class="stitle">Live within 48 hours</div><div class="sdesc">Missed call text back and follow-up sequences go live automatically.</div></div></div>
    <div class="step"><div class="sn">4</div><div><div class="stitle">Day 14 — we review together</div><div class="sdesc">I'll show you exactly what the system recovered. You decide what happens next.</div></div></div>
    <hr>
    <p class="ft">RoofPulse · Collierville, TN · Questions? Reply to this email.<br><span style="color:#ffffff20">14-day free pilot · no card · no commitment</span></p>
  </div>
</div></body></html>"""


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/api/simulate-call', methods=['POST'])
def simulate_call():
    data  = request.json
    name  = data.get('name',  'Unknown')
    phone = data.get('phone', '(901) 555-0000')
    leads.append({"id": len(DEMO_LEADS)+len(leads)+1, "name": name, "phone": phone, "status": "New", "source": "Missed Call", "value": 0, "time": "just now"})
    return jsonify({"success": True})

@app.route('/api/leads', methods=['GET'])
def get_leads():
    return jsonify(DEMO_LEADS + leads)

@app.route('/contact', methods=['POST'])
def contact():
    name         = request.form.get('name',         '').strip()
    company      = request.form.get('company',      '').strip()
    phone        = request.form.get('phone',        '').strip()
    email        = request.form.get('email',        '').strip()
    missed_calls = request.form.get('missed_calls', 'Not specified')
    submitted_at = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    send_async(OWNER_EMAIL, f"🔥 New Pilot Request: {name} — {company}", owner_email(name, company, phone, email, missed_calls, submitted_at))
    if email:
        send_async(email, f"You're confirmed, {name.split()[0]}! — RoofPulse", prospect_email(name, company))
    return redirect(url_for('thankyou'))

@app.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
