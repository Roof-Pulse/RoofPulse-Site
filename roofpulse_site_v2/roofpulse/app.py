from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

OWNER_EMAIL = os.environ.get("OWNER_EMAIL", "Hayesscale500@gmail.com")
GMAIL_USER  = os.environ.get("GMAIL_USER",  "Hayesscale500@gmail.com")
GMAIL_PASS  = os.environ.get("GMAIL_PASS",  "")

DEMO_LEADS = [
    {"id": 1, "name": "Mike Johnson",   "phone": "(901) 555-0142", "status": "Booked",     "source": "Missed Call", "value": 8500,  "time": "2 mins ago"},
    {"id": 2, "name": "Sarah Williams", "phone": "(901) 555-0287", "status": "Responding", "source": "Missed Call", "value": 12000, "time": "11 mins ago"},
    {"id": 3, "name": "David Chen",     "phone": "(901) 555-0391", "status": "Booked",     "source": "Web Form",    "value": 6800,  "time": "34 mins ago"},
    {"id": 4, "name": "Amanda Torres",  "phone": "(901) 555-0456", "status": "New",        "source": "Missed Call", "value": 9200,  "time": "1 hr ago"},
    {"id": 5, "name": "Robert Hill",    "phone": "(901) 555-0512", "status": "Booked",     "source": "Referral",    "value": 15000, "time": "2 hrs ago"},
]
leads = []


def send_email(to_addr, subject, html_body):
    if not GMAIL_PASS:
        print(f"[EMAIL SKIPPED] No GMAIL_PASS. Would send to {to_addr}: {subject}")
        return True, None
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = f"RoofPulse <{GMAIL_USER}>"
        msg["To"]      = to_addr
        msg.attach(MIMEText(html_body, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(GMAIL_USER, GMAIL_PASS)
            s.sendmail(GMAIL_USER, to_addr, msg.as_string())
        return True, None
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False, str(e)


def owner_email(name, company, phone, email, missed_calls, submitted_at):
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:'Helvetica Neue',Arial,sans-serif;background:#0D1117;margin:0;padding:40px 20px}}
.w{{max-width:580px;margin:0 auto}}
.hd{{background:#E63946;border-radius:10px 10px 0 0;padding:32px 40px;text-align:center}}
.hd h1{{font-size:12px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#ffffff90;margin:0 0 8px}}
.hd h2{{font-size:28px;font-weight:900;color:#fff;margin:0}}
.bd{{background:#161B22;border:1px solid #ffffff10;border-top:none;border-radius:0 0 10px 10px;padding:36px 40px}}
.badge{{display:inline-block;background:#E6394620;border:1px solid #E6394640;color:#E63946;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:6px 14px;border-radius:4px;margin-bottom:28px}}
.hl{{background:linear-gradient(135deg,#E6394610,#E6394605);border:1px solid #E6394630;border-radius:8px;padding:20px 24px;margin-bottom:24px}}
.hl p{{font-size:14px;color:#cdd9e5;margin:0;line-height:1.6}}
.hl strong{{color:#E63946}}
.fl{{margin-bottom:20px}}
.fl-l{{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8B949E;margin-bottom:6px}}
.fl-v{{font-size:16px;color:#F0F6FC;font-weight:600;background:#0D1117;border:1px solid #ffffff10;border-radius:6px;padding:12px 16px}}
hr{{border:none;border-top:1px solid #ffffff10;margin:28px 0}}
.cta{{display:block;text-align:center;background:#E63946;color:#fff;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;text-decoration:none;padding:16px 32px;border-radius:6px;margin-top:28px}}
.ft{{text-align:center;padding:24px;font-size:12px;color:#8B949E}}
</style></head><body>
<div class="w">
  <div class="hd"><h1>RoofPulse</h1><h2>🔥 New Lead Just Came In</h2></div>
  <div class="bd">
    <div class="badge">⚡ New Trial Request</div>
    <div class="hl"><p><strong>{name}</strong> from <strong>{company}</strong> just signed up for a free 30-day trial. They miss <strong>{missed_calls}</strong> per week. Reach out within the hour while they're warm.</p></div>
    <div class="fl"><div class="fl-l">Full Name</div><div class="fl-v">{name}</div></div>
    <div class="fl"><div class="fl-l">Company</div><div class="fl-v">{company}</div></div>
    <div class="fl"><div class="fl-l">Phone</div><div class="fl-v">{phone}</div></div>
    <div class="fl"><div class="fl-l">Email</div><div class="fl-v">{email}</div></div>
    <div class="fl"><div class="fl-l">Missed Calls/Week</div><div class="fl-v">{missed_calls}</div></div>
    <div class="fl"><div class="fl-l">Submitted At</div><div class="fl-v">{submitted_at}</div></div>
    <hr>
    <a href="mailto:{email}" class="cta">Reply to {name} Now →</a>
  </div>
  <div class="ft">RoofPulse · Collierville, TN · Hayesscale500@gmail.com</div>
</div></body></html>"""


def prospect_email(name, company):
    first = name.split()[0]
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:'Helvetica Neue',Arial,sans-serif;background:#0D1117;margin:0;padding:40px 20px}}
.w{{max-width:580px;margin:0 auto}}
.hd{{background:#0D1117;border:1px solid #ffffff10;border-bottom:none;border-radius:10px 10px 0 0;padding:40px;text-align:center}}
.logo{{font-size:26px;font-weight:900;letter-spacing:4px;color:#fff;margin-bottom:24px;display:block}}
.logo span{{color:#E63946}}
.circle{{width:72px;height:72px;background:#16803420;border:2px solid #16803460;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:32px;margin:0 auto 20px;line-height:72px;text-align:center}}
.hd h1{{font-size:28px;font-weight:900;color:#fff;margin:0 0 8px}}
.hd p{{font-size:15px;color:#8B949E;margin:0}}
.bd{{background:#161B22;border:1px solid #ffffff10;border-top:none;border-radius:0 0 10px 10px;padding:36px 40px}}
.greet{{font-size:16px;color:#F0F6FC;line-height:1.7;margin-bottom:32px}}
.greet strong{{color:#E63946}}
.ib{{background:#E6394608;border:1px solid #E6394625;border-radius:8px;padding:20px 24px;margin-bottom:28px}}
.ib p{{font-size:14px;color:#cdd9e5;margin:0;line-height:1.6}}
.ib strong{{color:#E63946}}
.st{{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8B949E;margin-bottom:20px}}
.step{{display:flex;gap:16px;align-items:flex-start;margin-bottom:20px}}
.sn{{background:#E63946;color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;flex-shrink:0;line-height:32px;text-align:center}}
.sc{{flex:1}}
.stitle{{font-size:15px;font-weight:700;color:#F0F6FC;margin-bottom:4px}}
.sdesc{{font-size:13px;color:#8B949E;line-height:1.5}}
hr{{border:none;border-top:1px solid #ffffff10;margin:28px 0}}
.fl{{text-align:center;font-size:13px;color:#8B949E;line-height:1.6}}
.fl-logo{{text-align:center;margin-bottom:8px;font-size:18px;font-weight:900;letter-spacing:3px;color:#ffffff40}}
.fl-logo span{{color:#E6394660}}
</style></head><body>
<div class="w">
  <div class="hd">
    <span class="logo">ROOF<span>PULSE</span></span>
    <div class="circle">✅</div>
    <h1>You're Confirmed, {first}!</h1>
    <p>Your free 30-day trial request has been received.</p>
  </div>
  <div class="bd">
    <p class="greet">Hey {first} — this is a real person, not an auto-reply. I'm local to Collierville, TN and I personally set up every system. I'll be reaching out to you at <strong>{company}</strong> within the next few hours to get everything going.</p>
    <div class="ib"><p>The average roofing company we work with recovers <strong>8–14 missed leads in their first 30 days</strong> — that's $64,000–$168,000 in potential revenue that was going straight to voicemail. We're about to change that for you.</p></div>
    <div class="st">Here's exactly what happens next</div>
    <div class="step"><div class="sn">1</div><div class="sc"><div class="stitle">I'll reach out personally</div><div class="sdesc">Expect a call or text within 2–4 hours to confirm your details and answer any questions.</div></div></div>
    <div class="step"><div class="sn">2</div><div class="sc"><div class="stitle">30-minute setup call</div><div class="sdesc">We'll go through your business number, call script, and booking process. You don't touch any software.</div></div></div>
    <div class="step"><div class="sn">3</div><div class="sc"><div class="stitle">Live within 48 hours</div><div class="sdesc">Your missed call text back, follow-up sequence, and booking system go live automatically.</div></div></div>
    <div class="step"><div class="sn">4</div><div class="sc"><div class="stitle">Watch the leads come back</div><div class="sdesc">After 30 days we'll review your results together — every recovered call, every dollar saved.</div></div></div>
    <hr>
    <div class="fl-logo">ROOF<span>PULSE</span></div>
    <p class="fl">RoofPulse · Collierville, TN<br>Questions? Reply directly to this email.<br><span style="color:#ffffff25">100% free trial. No card. No commitment.</span></p>
  </div>
</div></body></html>"""

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}
    
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/api/simulate-call', methods=['POST'])
def simulate_call():
    data  = request.json
    name  = data.get('name',  'Unknown Caller')
    phone = data.get('phone', '(901) 555-0000')
    leads.append({"id": len(DEMO_LEADS)+len(leads)+1, "name": name, "phone": phone, "status": "New", "source": "Missed Call", "value": 0, "time": "just now"})
    return jsonify({"success": True, "auto_text": f"Hey {name.split()[0]}! This is RoofPulse Demo — sorry we missed you! Can we schedule a free inspection this week? Reply YES to confirm.", "response_time": "0:47 seconds"})

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

    send_email(OWNER_EMAIL, f"🔥 New RoofPulse Lead: {name} — {company}", owner_email(name, company, phone, email, missed_calls, submitted_at))

    if email:
        send_email(email, f"You're confirmed, {name.split()[0]}! Here's what happens next — RoofPulse", prospect_email(name, company))

    return redirect(url_for('thankyou'))

@app.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
