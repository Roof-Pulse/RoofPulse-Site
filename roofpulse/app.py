from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

# Simple in-memory storage for demo (in production use a real DB)
leads = []
missed_calls = []
messages = []

# ── Demo data to simulate a live system ──────────────────────────────────────
DEMO_LEADS = [
    {"id": 1, "name": "Mike Johnson", "phone": "(901) 555-0142", "status": "Booked", "source": "Missed Call", "value": 8500, "time": "2 mins ago"},
    {"id": 2, "name": "Sarah Williams", "phone": "(901) 555-0287", "status": "Responding", "source": "Missed Call", "time": "11 mins ago", "value": 12000},
    {"id": 3, "name": "David Chen", "phone": "(901) 555-0391", "status": "Booked", "source": "Web Form", "value": 6800, "time": "34 mins ago"},
    {"id": 4, "name": "Amanda Torres", "phone": "(901) 555-0456", "status": "New", "source": "Missed Call", "value": 9200, "time": "1 hr ago"},
    {"id": 5, "name": "Robert Hill", "phone": "(901) 555-0512", "status": "Booked", "source": "Referral", "value": 15000, "time": "2 hrs ago"},
]

DEMO_MESSAGES = [
    {"from": "RoofPulse", "to": "Mike Johnson", "text": "Hey Mike! This is Memphis Roofing Co — sorry we missed your call. We'd love to help. Can we schedule a free inspection this week?", "time": "2 mins ago", "direction": "out"},
    {"from": "Mike Johnson", "to": "RoofPulse", "text": "Yes! Thursday works great.", "time": "1 min ago", "direction": "in"},
    {"from": "RoofPulse", "to": "Mike Johnson", "text": "Perfect! Thursday at 10am is confirmed. We'll send a reminder the night before. See you then!", "time": "just now", "direction": "out"},
]

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}
    
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/demo')
def demo():
    return render_template('demo.html', leads=DEMO_LEADS, messages=DEMO_MESSAGES)

@app.route('/api/simulate-call', methods=['POST'])
def simulate_call():
    data = request.json
    name = data.get('name', 'Unknown Caller')
    phone = data.get('phone', '(901) 555-0000')
    
    # Simulate missed call → instant text back
    new_lead = {
        "id": len(DEMO_LEADS) + len(leads) + 1,
        "name": name,
        "phone": phone,
        "status": "New",
        "source": "Missed Call",
        "value": 0,
        "time": "just now"
    }
    leads.append(new_lead)
    
    auto_text = f"Hey {name.split()[0]}! This is RoofPulse Demo Co — sorry we missed your call! We'd love to help with your roofing needs. Can we schedule a free inspection this week? Reply YES to confirm."
    
    return jsonify({
        "success": True,
        "lead": new_lead,
        "auto_text": auto_text,
        "response_time": "0:47 seconds"
    })

@app.route('/api/leads', methods=['GET'])
def get_leads():
    all_leads = DEMO_LEADS + leads
    return jsonify(all_leads)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    company = request.form.get('company')
    # In production: send to GHL, email, SMS
    return redirect(url_for('thankyou'))

@app.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
