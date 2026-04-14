<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RoofPulse — Turn Missed Calls Into Booked Roofing Jobs</title>
  <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
  <link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
  <link rel="apple-touch-icon" href="/static/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {
      --red: #E63946;
      --red-dark: #c1121f;
      --dark: #0D1117;
      --dark-2: #161B22;
      --dark-3: #1E2530;
      --white: #FFFFFF;
      --gray: #8B949E;
      --light: #F0F6FC;
      --border: #ffffff10;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Barlow', sans-serif;
      background: var(--dark);
      color: var(--white);
      overflow-x: hidden;
    }

    /* ── NAV ── */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 20px 60px;
      background: linear-gradient(to bottom, #0D1117f0, transparent);
      backdrop-filter: blur(6px);
    }
    .nav-logo { font-family: 'Bebas Neue', sans-serif; font-size: 26px; letter-spacing: 3px; }
    .nav-logo span { color: var(--red); }
    .nav-links { display: flex; gap: 32px; align-items: center; }
    .nav-links a { font-size: 13px; font-weight: 600; letter-spacing: 1px; color: var(--gray); text-decoration: none; transition: color .2s; }
    .nav-links a:hover { color: var(--white); }
    .nav-cta { background: var(--red) !important; color: var(--white) !important; padding: 9px 22px; border-radius: 4px; font-size: 12px !important; }
    .nav-cta:hover { background: var(--red-dark) !important; }

    /* ── HERO ── */
    .hero {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      padding: 120px 60px 80px;
      gap: 60px;
      position: relative;
      overflow: hidden;
    }

    .hero-grid {
      position: absolute; inset: 0;
      background-image: linear-gradient(#ffffff04 1px, transparent 1px), linear-gradient(90deg, #ffffff04 1px, transparent 1px);
      background-size: 52px 52px;
      mask-image: radial-gradient(ellipse 70% 70% at 30% 50%, black 40%, transparent 100%);
    }

    .hero-left { position: relative; z-index: 2; }

    .founder-badge {
      display: inline-flex; align-items: center; gap: 10px;
      background: var(--dark-2); border: 1px solid var(--border);
      border-radius: 100px; padding: 8px 16px 8px 8px;
      margin-bottom: 32px;
    }
    .founder-avatar {
      width: 32px; height: 32px; border-radius: 50%;
      background: var(--red); display: flex; align-items: center;
      justify-content: center; font-size: 14px; font-weight: 700;
      flex-shrink: 0;
    }
    .founder-badge-text { font-size: 13px; color: var(--gray); }
    .founder-badge-text strong { color: var(--white); }

    h1 {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(44px, 5.5vw, 72px);
      line-height: 1.0;
      letter-spacing: 1px;
      margin-bottom: 20px;
      color: var(--white);
    }
    h1 .accent { color: var(--red); }

    .hero-sub {
      font-size: 17px; line-height: 1.75;
      color: var(--gray); max-width: 480px;
      margin-bottom: 36px;
    }
    .hero-sub strong { color: var(--white); }

    .hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 40px; }

    .btn-primary {
      background: var(--red); color: var(--white);
      padding: 14px 32px; font-family: 'Barlow', sans-serif;
      font-size: 14px; font-weight: 700; letter-spacing: 1px;
      border: none; border-radius: 4px; cursor: pointer;
      text-decoration: none; display: inline-block;
      transition: all .2s;
    }
    .btn-primary:hover { background: var(--red-dark); transform: translateY(-1px); }

    .btn-ghost {
      background: transparent; color: var(--white);
      padding: 14px 32px; font-size: 14px; font-weight: 600;
      border: 1px solid #ffffff25; border-radius: 4px;
      cursor: pointer; text-decoration: none; display: inline-block;
      transition: all .2s;
    }
    .btn-ghost:hover { border-color: #ffffff60; background: #ffffff08; }

    .hero-trust {
      display: flex; align-items: center; gap: 20px;
      padding-top: 28px; border-top: 1px solid var(--border);
      flex-wrap: wrap;
    }
    .trust-item { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--gray); }
    .trust-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--red); flex-shrink: 0; }

    /* Hero right — conversation mockup */
    .hero-right {
      position: relative; z-index: 2;
      display: flex; flex-direction: column; gap: 12px;
    }

    .mockup-label {
      font-size: 11px; font-weight: 700; letter-spacing: 2px;
      text-transform: uppercase; color: var(--gray); margin-bottom: 4px;
    }

    .phone-mockup {
      background: var(--dark-2);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
    }

    .phone-header {
      background: var(--dark-3);
      padding: 14px 20px;
      display: flex; align-items: center; gap: 10px;
      border-bottom: 1px solid var(--border);
    }
    .phone-avatar {
      width: 36px; height: 36px; border-radius: 50%;
      background: #E6394620; border: 1px solid #E6394640;
      display: flex; align-items: center; justify-content: center;
      font-size: 16px;
    }
    .phone-name { font-size: 14px; font-weight: 700; }
    .phone-sub { font-size: 11px; color: var(--gray); }
    .phone-status { margin-left: auto; display: flex; align-items: center; gap: 6px; font-size: 11px; color: #4ade80; }
    .status-dot { width: 6px; height: 6px; border-radius: 50%; background: #4ade80; animation: pulse-green 2s infinite; }
    @keyframes pulse-green { 0%,100%{opacity:1} 50%{opacity:.4} }

    .phone-body { padding: 20px; display: flex; flex-direction: column; gap: 14px; }

    .event-pill {
      display: flex; align-items: center; gap: 10px;
      background: #E6394210; border: 1px solid #E6394230;
      border-radius: 8px; padding: 10px 14px;
      font-size: 12px; color: var(--gray);
    }
    .event-pill strong { color: var(--white); }
    .event-icon { font-size: 16px; flex-shrink: 0; }

    .msg-wrap { display: flex; flex-direction: column; gap: 8px; }
    .msg-label-small { font-size: 10px; color: var(--gray); letter-spacing: 1px; text-transform: uppercase; }
    .msg-label-small.right { text-align: right; }

    .bubble {
      max-width: 82%; padding: 11px 15px;
      border-radius: 14px; font-size: 13px; line-height: 1.5;
    }
    .bubble-out {
      align-self: flex-end;
      background: var(--red); color: var(--white);
      border-radius: 14px 14px 3px 14px;
    }
    .bubble-in {
      align-self: flex-start;
      background: var(--dark-3); color: var(--light);
      border-radius: 14px 14px 14px 3px;
    }

    .response-badge {
      display: flex; align-items: center; gap: 8px;
      background: #16803415; border: 1px solid #16803430;
      border-radius: 6px; padding: 8px 12px;
      font-size: 12px; font-weight: 600; color: #4ade80;
      align-self: flex-start;
    }

    /* ── PROBLEM ── */
    .section { padding: 90px 60px; }
    .section-label {
      font-size: 11px; font-weight: 700; letter-spacing: 3px;
      text-transform: uppercase; color: var(--red); margin-bottom: 14px;
    }
    .section-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(36px, 4vw, 54px);
      line-height: 1.05; letter-spacing: 1px; margin-bottom: 18px;
    }
    .section-sub {
      font-size: 16px; color: var(--gray);
      max-width: 520px; line-height: 1.7; margin-bottom: 52px;
    }

    .problem-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1px; background: var(--border); border-radius: 12px; overflow: hidden;
    }
    .problem-item {
      background: var(--dark-2); padding: 36px;
      transition: background .2s;
    }
    .problem-item:hover { background: var(--dark-3); }
    .problem-stat {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 48px; color: var(--red); line-height: 1; margin-bottom: 8px;
    }
    .problem-title { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
    .problem-desc { font-size: 13px; color: var(--gray); line-height: 1.65; }
    .problem-source { font-size: 11px; color: #ffffff30; margin-top: 10px; font-style: italic; }

    /* ── HOW ── */
    .how-section { background: var(--dark-2); padding: 90px 60px; }
    .steps {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0; margin-top: 52px; position: relative;
    }
    .steps::before {
      content: ''; position: absolute;
      top: 44px; left: 8%; right: 8%; height: 1px;
      background: linear-gradient(to right, transparent, #E6394640, transparent);
    }
    .step { padding: 0 28px; text-align: center; }
    .step-num {
      width: 48px; height: 48px; border-radius: 50%;
      background: var(--red); color: var(--white);
      font-family: 'Bebas Neue', sans-serif; font-size: 22px;
      display: flex; align-items: center; justify-content: center;
      margin: 0 auto 20px; position: relative; z-index: 1;
      box-shadow: 0 0 24px #E6394630;
    }
    .step-title { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
    .step-desc { font-size: 13px; color: var(--gray); line-height: 1.65; }

    /* ── DEMO ── */
    .demo-section { padding: 90px 60px; }
    .simulator {
      background: var(--dark-2); border: 1px solid var(--border);
      border-radius: 14px; overflow: hidden; max-width: 900px; margin: 52px auto 0;
    }
    .sim-bar {
      background: var(--dark-3); padding: 14px 20px;
      display: flex; align-items: center; gap: 8px;
      border-bottom: 1px solid var(--border);
    }
    .sim-dot { width: 10px; height: 10px; border-radius: 50%; }
    .sim-bar-title { font-size: 12px; color: var(--gray); margin-left: 8px; }
    .sim-body { display: grid; grid-template-columns: 1fr 1fr; min-height: 400px; }
    .sim-left { padding: 32px; border-right: 1px solid var(--border); }
    .sim-right { padding: 32px; }
    .sim-section-label {
      font-size: 11px; font-weight: 700; letter-spacing: 2px;
      text-transform: uppercase; color: var(--gray); margin-bottom: 20px;
    }
    .call-form { display: flex; flex-direction: column; gap: 12px; }
    .form-input {
      background: var(--dark-3); border: 1px solid var(--border);
      border-radius: 6px; padding: 11px 15px;
      font-family: 'Barlow', sans-serif; font-size: 14px; color: var(--white);
      outline: none; transition: border-color .2s; width: 100%;
    }
    .form-input:focus { border-color: var(--red); }
    .form-input::placeholder { color: var(--gray); }
    .sim-btn {
      background: var(--red); color: var(--white); border: none;
      padding: 13px; border-radius: 6px;
      font-family: 'Barlow', sans-serif; font-size: 14px; font-weight: 700;
      cursor: pointer; transition: all .2s;
    }
    .sim-btn:hover { background: var(--red-dark); }
    .message-thread { display: flex; flex-direction: column; gap: 12px; }
    .sim-msg {
      max-width: 82%; padding: 11px 15px; border-radius: 12px;
      font-size: 13px; line-height: 1.5;
      opacity: 0; animation: fadeUp .35s ease forwards;
    }
    @keyframes fadeUp { from{opacity:0;transform:translateY(6px)} to{opacity:1;transform:translateY(0)} }
    .sim-out { align-self: flex-end; background: var(--red); color: var(--white); border-radius: 12px 12px 3px 12px; }
    .sim-in { align-self: flex-start; background: var(--dark-3); color: var(--light); border-radius: 12px 12px 12px 3px; }
    .sim-meta { font-size: 10px; color: var(--gray); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 2px; }
    .sim-meta.right { text-align: right; }
    .sim-result {
      display: flex; align-items: center; gap: 8px;
      background: #16803415; border: 1px solid #16803430;
      color: #4ade80; font-size: 12px; font-weight: 600;
      padding: 8px 12px; border-radius: 6px; margin-top: 6px;
    }

    /* ── FOUNDER ── */
    .founder-section { background: var(--dark-2); padding: 90px 60px; }
    .founder-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 80px; max-width: 900px; margin: 0 auto; align-items: center;
    }
    .founder-card {
      background: var(--dark); border: 1px solid var(--border);
      border-radius: 14px; padding: 40px; position: relative;
    }
    .founder-card::before {
      content: ''; position: absolute;
      top: 0; left: 40px; right: 40px; height: 2px;
      background: var(--red); border-radius: 0 0 2px 2px;
    }
    .founder-initial {
      width: 64px; height: 64px; border-radius: 50%;
      background: var(--red); color: var(--white);
      font-family: 'Bebas Neue', sans-serif; font-size: 28px;
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 20px;
    }
    .founder-name { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
    .founder-role { font-size: 13px; color: var(--red); margin-bottom: 20px; font-weight: 600; }
    .founder-quote { font-size: 15px; color: var(--gray); line-height: 1.75; font-style: italic; }
    .founder-details { display: flex; flex-direction: column; gap: 16px; }
    .founder-detail { display: flex; align-items: flex-start; gap: 14px; }
    .detail-icon { font-size: 20px; flex-shrink: 0; margin-top: 2px; }
    .detail-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
    .detail-desc { font-size: 13px; color: var(--gray); line-height: 1.6; }

    /* ── PILOT OFFER ── */
    .pilot-section { padding: 90px 60px; }
    .pilot-card {
      max-width: 720px; margin: 0 auto;
      background: var(--dark-2); border: 1px solid var(--border);
      border-radius: 14px; padding: 56px;
      text-align: center; position: relative; overflow: hidden;
    }
    .pilot-card::before {
      content: ''; position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: var(--red);
    }
    .pilot-eyebrow {
      font-size: 11px; font-weight: 700; letter-spacing: 3px;
      text-transform: uppercase; color: var(--red); margin-bottom: 16px;
    }
    .pilot-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 48px; line-height: 1; margin-bottom: 16px;
    }
    .pilot-desc { font-size: 16px; color: var(--gray); line-height: 1.7; max-width: 520px; margin: 0 auto 36px; }
    .pilot-checklist {
      display: flex; flex-direction: column; gap: 12px;
      text-align: left; max-width: 380px; margin: 0 auto 36px;
    }
    .pilot-check { display: flex; align-items: center; gap: 12px; font-size: 14px; color: var(--light); }
    .pilot-check::before { content: '✓'; color: var(--red); font-weight: 700; flex-shrink: 0; }
    .pilot-fine { font-size: 12px; color: var(--gray); margin-top: 16px; }

    /* ── PRICING ── */
    .pricing-section { background: var(--dark-2); padding: 90px 60px; }
    .pricing-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px; max-width: 720px; margin: 52px auto 0;
    }
    .price-card {
      background: var(--dark); border: 1px solid var(--border);
      border-radius: 12px; padding: 36px; transition: all .3s; position: relative;
    }
    .price-card.featured { border-color: var(--red); }
    .price-card.featured::before {
      content: 'MOST POPULAR'; position: absolute;
      top: -11px; left: 50%; transform: translateX(-50%);
      background: var(--red); color: var(--white);
      font-size: 10px; font-weight: 700; letter-spacing: 2px;
      padding: 3px 14px; border-radius: 2px;
    }
    .price-name { font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--gray); margin-bottom: 14px; }
    .price-amount { font-family: 'Bebas Neue', sans-serif; font-size: 56px; color: var(--white); line-height: 1; }
    .price-period { font-size: 13px; color: var(--gray); margin-bottom: 28px; }
    .price-features { list-style: none; margin-bottom: 32px; display: flex; flex-direction: column; gap: 11px; }
    .price-features li { font-size: 13px; color: #cdd9e5; display: flex; align-items: flex-start; gap: 10px; line-height: 1.4; }
    .price-features li::before { content: '✓'; color: var(--red); font-weight: 700; flex-shrink: 0; margin-top: 1px; }

    /* ── CONTACT ── */
    .contact-section { padding: 90px 60px; }
    .contact-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 80px; max-width: 900px; margin: 0 auto; align-items: start;
    }
    .contact-form { display: flex; flex-direction: column; gap: 14px; }
    .form-group { display: flex; flex-direction: column; gap: 7px; }
    .form-label { font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; color: var(--gray); }

    /* ── FOOTER ── */
    footer {
      background: var(--dark-2); border-top: 1px solid var(--border);
      padding: 36px 60px; display: flex; align-items: center;
      justify-content: space-between; flex-wrap: wrap; gap: 14px;
    }
    .footer-logo { font-family: 'Bebas Neue', sans-serif; font-size: 20px; letter-spacing: 3px; }
    .footer-logo span { color: var(--red); }
    .footer-text { font-size: 12px; color: var(--gray); }


    /* ── STATS PANEL ── */
    .stats-panel {
      background: var(--dark); padding: 60px;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
    }
    .stats-inner {
      display: flex; justify-content: center; gap: 0;
      max-width: 700px; margin: 0 auto;
      background: var(--dark-2); border: 1px solid var(--border);
      border-radius: 12px; overflow: hidden;
    }
    .stat-block {
      flex: 1; padding: 32px 28px; text-align: center;
      border-right: 1px solid var(--border);
      transition: background .2s;
    }
    .stat-block:last-child { border-right: none; }
    .stat-block:hover { background: var(--dark-3); }
    .stat-num {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 52px; color: var(--red); line-height: 1;
      margin-bottom: 6px;
    }
    .stat-label { font-size: 12px; color: var(--gray); letter-spacing: 1px; text-transform: uppercase; }
    .stat-note { font-size: 11px; color: #ffffff25; margin-top: 4px; }

    /* ── RESPONSIVE ── */
    @media (max-width: 900px) {
      nav { padding: 16px 24px; }
      .nav-links { display: none; }
      .hero { grid-template-columns: 1fr; padding: 100px 24px 60px; gap: 48px; }
      .hero-right { order: -1; }
      .section { padding: 60px 24px; }
      .how-section { padding: 60px 24px; }
      .steps::before { display: none; }
      .demo-section { padding: 60px 24px; }
      .sim-body { grid-template-columns: 1fr; }
      .sim-left { border-right: none; border-bottom: 1px solid var(--border); }
      .founder-section { padding: 60px 24px; }
      .founder-grid { grid-template-columns: 1fr; gap: 40px; }
      .pilot-section { padding: 60px 24px; }
      .pilot-card { padding: 36px 24px; }
      .pricing-section { padding: 60px 24px; }
      .contact-section { padding: 60px 24px; }
      .contact-grid { grid-template-columns: 1fr; gap: 48px; }
      footer { padding: 28px 24px; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">ROOF<span>PULSE</span></div>
  <div class="nav-links">
    <a href="#how">How It Works</a>
    <a href="#demo">See the Demo</a>
    <a href="#founder">About</a>
    <a href="#contact" class="nav-cta">Talk to Me</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-grid"></div>

  <div class="hero-left">
    <div class="founder-badge">
      <div class="founder-avatar">H</div>
      <div class="founder-badge-text">
        <strong>Hayden</strong> · Collierville, TN · Building in public
      </div>
    </div>

    <h1>
      TURN MISSED CALLS<br>
      INTO BOOKED<br>
      <span class="accent">ROOFING JOBS.</span>
    </h1>

    <p class="hero-sub">
      When your crew is on a roof, RoofPulse texts missed callers back automatically, keeps the conversation going, and helps book the inspection — <strong>without you lifting a finger.</strong>
    </p>

    <div class="hero-actions">
      <a href="#demo" class="btn-primary">See the Demo</a>
      <a href="#contact" class="btn-ghost">Talk to Me →</a>
    </div>

    <div class="hero-trust">
      <div class="trust-item">
        <div class="trust-dot"></div>
        Built locally in Collierville, TN
      </div>
      <div class="trust-item">
        <div class="trust-dot"></div>
        14-day free pilot for local roofers
      </div>
      <div class="trust-item">
        <div class="trust-dot"></div>
        No contracts, ever
      </div>
    </div>
  </div>

  <!-- Conversation mockup -->
  <div class="hero-right">
    <div class="mockup-label">What happens when you miss a call</div>
    <div class="phone-mockup">
      <div class="phone-header">
        <div class="phone-avatar">🏠</div>
        <div>
          <div class="phone-name">Homeowner — (901) 555-0142</div>
          <div class="phone-sub">Called 47 seconds ago · went to voicemail</div>
        </div>
        <div class="phone-status">
          <div class="status-dot"></div>
          Live
        </div>
      </div>
      <div class="phone-body">
        <div class="event-pill">
          <div class="event-icon">📞</div>
          <div><strong>Missed call detected</strong> — RoofPulse texted back in 47 seconds</div>
        </div>

        <div class="msg-wrap">
          <div class="sim-meta right">RoofPulse sent automatically</div>
          <div class="bubble bubble-out">
            Hey! Sorry we missed your call — this is Smith Roofing Co. Can we help with a roof repair or inspection? We're local and usually available within a day or two. 🏠
          </div>
        </div>

        <div class="msg-wrap">
          <div class="sim-meta">Homeowner replied 3 minutes later</div>
          <div class="bubble bubble-in">
            Yes! Storm damage from last week. Can someone come Thursday?
          </div>
        </div>

        <div class="msg-wrap">
          <div class="sim-meta right">RoofPulse confirmed automatically</div>
          <div class="bubble bubble-out">
            Thursday works great! I'll have someone there at 10am for a free inspection. You'll get a reminder the night before. 👍
          </div>
        </div>

        <div class="response-badge">
          ✓ Appointment booked — zero manual work
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PROBLEM -->
<section class="section" id="problem">
  <div class="section-label">Why This Matters</div>
  <h2 class="section-title">Most Roofing Jobs Are Lost<br>Before You Even Know About Them</h2>
  <p class="section-sub">Industry research consistently shows that missed calls are one of the biggest silent revenue drains for home service businesses.</p>

  <div class="problem-grid">
    <div class="problem-item">
      <div class="problem-stat">85%</div>
      <div class="problem-title">Won't Call Back</div>
      <div class="problem-desc">Of callers who reach voicemail move on to the next contractor immediately — they don't leave a message and they don't try again.</div>
      <div class="problem-source">Source: Invoca Home Services Research</div>
    </div>
    <div class="problem-item">
      <div class="problem-stat">27%</div>
      <div class="problem-title">Of Calls Go Unanswered</div>
      <div class="problem-desc">Nearly one in three calls to home service businesses goes unanswered — that's a significant slice of potential revenue walking out the door daily.</div>
      <div class="problem-source">Source: Invoca Platform Data</div>
    </div>
    <div class="problem-item">
      <div class="problem-stat">5 min</div>
      <div class="problem-title">Response Window</div>
      <div class="problem-desc">Leads contacted within 5 minutes are significantly more likely to book than those reached later. Most roofing companies take hours — or days.</div>
      <div class="problem-source">Source: Harvard Business Review lead response study</div>
    </div>
    <div class="problem-item">
      <div class="problem-stat">400%</div>
      <div class="problem-title">Storm Surge</div>
      <div class="problem-desc">After a major storm, call volume can spike 400%. Without an automated system, most of those high-value calls go unanswered at the worst possible time.</div>
      <div class="problem-source">Source: Industry contractor reports</div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="how-section" id="how">
  <div class="section-label">How It Works</div>
  <h2 class="section-title">Simple Setup.<br>Runs Itself.</h2>
  <p class="section-sub">You set it up once with me. After that it handles missed calls automatically — day or night, on the job site or not.</p>

  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-title">Call Comes In</div>
      <div class="step-desc">A homeowner calls your number. You're busy — on a roof, with a customer, or after hours. The call goes unanswered.</div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-title">Instant Text Back</div>
      <div class="step-desc">Within seconds the caller gets a personalized text from your business number. Friendly, natural — not robotic.</div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-title">Automatic Follow-Up</div>
      <div class="step-desc">The system answers questions, qualifies what they need, and keeps following up until they book or opt out.</div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div class="step-title">You Show Up</div>
      <div class="step-desc">The appointment lands in your calendar. The lead is in your pipeline. You just show up and do what you're good at.</div>
    </div>
  </div>
</section>


<!-- LIVE STATS PANEL -->
<div class="stats-panel">
  <div class="stats-inner">
    <div class="stat-block">
      <div class="stat-num" id="stat-recovered">{{ recovered }}</div>
      <div class="stat-label">Demo Leads Recovered</div>
      <div class="stat-note">increments with each simulation</div>
    </div>
    <div class="stat-block">
      <div class="stat-num" id="stat-days">{{ days_live }}</div>
      <div class="stat-label">Days Live</div>
      <div class="stat-note">and counting</div>
    </div>
    <div class="stat-block">
      <div class="stat-num">&lt;60s</div>
      <div class="stat-label">Response Time</div>
      <div class="stat-note">every missed call</div>
    </div>
  </div>
</div>

<!-- DEMO SIMULATOR -->
<section class="demo-section" id="demo">
  <div class="section-label">Live Demo</div>
  <h2 class="section-title">Try It Yourself.</h2>
  <p class="section-sub">Enter a name and number below and watch exactly what a missed caller would receive — in real time.</p>

  <div class="simulator">
    <div class="sim-bar">
      <div class="sim-dot" style="background:#ff5f57"></div>
      <div class="sim-dot" style="background:#ffbd2e"></div>
      <div class="sim-dot" style="background:#28c840"></div>
      <span class="sim-bar-title">RoofPulse — Interactive Demo</span>
    </div>
    <div class="sim-body">
      <div class="sim-left">
        <div class="sim-section-label">📞 Simulate a Missed Call</div>
        <div class="call-form">
          <input class="form-input" id="sim-name" type="text" placeholder="Caller's name (e.g. Mike Johnson)">
          <input class="form-input" id="sim-phone" type="text" placeholder="Their number (e.g. 901-555-0142)">
          <input class="form-input" id="sim-issue" type="text" placeholder="Roofing issue (e.g. storm damage)">
          <button class="sim-btn" onclick="runDemo()">Simulate Missed Call →</button>
        </div>
        <div id="sim-result" style="display:none;margin-top:18px;">
          <div class="sim-result">⚡ Text sent in under 60 seconds</div>
          <div style="margin-top:12px;font-size:12px;color:var(--gray);line-height:1.8;">
            ✓ Lead captured automatically<br>
            ✓ Follow-up sequence started<br>
            ✓ You notified instantly
          </div>
        </div>
      </div>
      <div class="sim-right">
        <div class="sim-section-label">💬 Automated Response</div>
        <div class="message-thread" id="sim-thread">
          <p style="font-size:13px;color:var(--gray);">Fill in the form and hit simulate to see what your missed caller receives →</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOUNDER SECTION -->
<section class="founder-section" id="founder">
  <div class="section-label">Who's Behind This</div>
  <h2 class="section-title">Local. Hands-On.<br>Accountable.</h2>

  <div class="founder-grid">
    <div class="founder-card">
      <div class="founder-initial">H</div>
      <div class="founder-name">Hayden Keithley</div>
      <div class="founder-role">Founder · RoofPulse · Collierville, TN</div>
      <p class="founder-quote">"I'm 17, I'm local, and I built this specifically for roofing companies in the Memphis area. I'm not a call center or a software company — I'm one person who set up a system that actually works and I want to prove it to one local roofer at a time."</p>
    </div>

    <div class="founder-details">
      <div class="founder-detail">
        <div class="detail-icon">📍</div>
        <div>
          <div class="detail-title">Actually Local</div>
          <div class="detail-desc">Based in Collierville, TN. I serve Memphis metro roofing companies. If something needs fixing, you can reach me directly — not a support ticket.</div>
        </div>
      </div>
      <div class="founder-detail">
        <div class="detail-icon">🔧</div>
        <div>
          <div class="detail-title">I Do the Setup</div>
          <div class="detail-desc">You don't touch any software. I configure everything for your business — your number, your script, your booking process. Takes about 48 hours.</div>
        </div>
      </div>
      <div class="founder-detail">
        <div class="detail-icon">📊</div>
        <div>
          <div class="detail-title">Looking for My First Success Story</div>
          <div class="detail-desc">I'm offering a free 14-day pilot to one or two local roofing companies. I want to prove the numbers — and I need a real example to do that.</div>
        </div>
      </div>
      <div class="founder-detail">
        <div class="detail-icon">🔒</div>
        <div>
          <div class="detail-title">No Lock-In</div>
          <div class="detail-desc">Month to month. If it's not working after 30 days I don't want your money. Your data is always yours — I'll export everything if you ever leave.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PILOT OFFER -->
<section class="pilot-section" id="pilot">
  <div class="pilot-card">
    <div class="pilot-eyebrow">Limited Pilot Offer</div>
    <h2 class="pilot-title">FREE 14-DAY PILOT<br>FOR LOCAL ROOFERS</h2>
    <p class="pilot-desc">I'm looking for one or two roofing companies in the Memphis area willing to try this free. You get a fully working system. I get a real case study. Everyone wins.</p>

    <div class="pilot-checklist">
      <div class="pilot-check">Full missed call text back system — live in 48hrs</div>
      <div class="pilot-check">5-step automated follow-up sequence</div>
      <div class="pilot-check">Appointment booking built in</div>
      <div class="pilot-check">I set everything up — you do nothing technical</div>
      <div class="pilot-check">14 days completely free — no card needed</div>
      <div class="pilot-check">Cancel or continue — your choice at day 14</div>
    </div>

    <a href="#contact" class="btn-primary" style="font-size:15px;padding:16px 40px;">Claim the Free Pilot →</a>
    <p class="pilot-fine">After the pilot: $297–$497/month depending on what you need. Month to month, no contracts.</p>
  </div>
</section>

<!-- PRICING -->
<section class="pricing-section" id="pricing">
  <div style="text-align:center;">
    <div class="section-label">Early Access Pricing</div>
    <h2 class="section-title">Pilot Tiers</h2>
    <p class="section-sub" style="margin:0 auto 12px;">
      You're getting in early. These are introductory rates for the first few roofers
      who try this — you can upgrade, downgrade, or pause any time, no questions asked.
    </p>
    <p style="font-size:13px;color:var(--red);font-weight:600;margin-bottom:0;">
      Built and run by a local developer in Collierville, TN — no offshore call centers, no scripts, no lock-in.
    </p>
  </div>

  <div class="pricing-grid">
    <div class="price-card">
      <div class="price-name">Early Access — Starter</div>
      <div class="price-amount">$297</div>
      <div class="price-period">/month · limited slots · cancel anytime</div>
      <ul class="price-features">
        <li>Missed call text back</li>
        <li>3-step follow-up sequence</li>
        <li>CRM — up to 200 leads</li>
        <li>Appointment booking</li>
        <li>Direct line to me — always</li>
      </ul>
      <a href="#contact" class="btn-primary" style="width:100%;text-align:center;display:block;">Claim a Slot</a>
      <p style="font-size:11px;color:var(--gray);text-align:center;margin-top:10px;">Pilot pricing — locked in for your first 6 months</p>
    </div>

    <div class="price-card featured">
      <div class="price-name">Early Access — Storm Ready</div>
      <div class="price-amount">$497</div>
      <div class="price-period">/month · limited slots · cancel anytime</div>
      <ul class="price-features">
        <li>Everything in Starter</li>
        <li>5-step follow-up sequence</li>
        <li>Storm surge call handling</li>
        <li>Unlimited leads in CRM</li>
        <li>Review request automation</li>
        <li>Monthly results summary — your numbers, plainly explained</li>
      </ul>
      <a href="#contact" class="btn-primary" style="width:100%;text-align:center;display:block;">Start Free Pilot</a>
      <p style="font-size:11px;color:var(--gray);text-align:center;margin-top:10px;">Pilot pricing — locked in for your first 6 months</p>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact-section" id="contact">
  <div class="contact-grid">
    <div>
      <div class="section-label">Get in Touch</div>
      <h2 class="section-title" style="font-size:44px;">Let's Talk.</h2>
      <p style="font-size:16px;color:var(--gray);line-height:1.75;margin-bottom:32px;">
        Fill out the form and I'll reach out personally — usually within a few hours. No sales team, no scripts. Just me.
      </p>
      <div style="display:flex;flex-direction:column;gap:16px;">
        <div class="founder-detail">
          <div class="detail-icon">📍</div>
          <div>
            <div class="detail-title">Collierville, TN</div>
            <div class="detail-desc">Serving Memphis metro roofing companies</div>
          </div>
        </div>
        <div class="founder-detail">
          <div class="detail-icon">⚡</div>
          <div>
            <div class="detail-title">Live in 48 Hours</div>
            <div class="detail-desc">System goes live within two days of our setup call</div>
          </div>
        </div>
        <div class="founder-detail">
          <div class="detail-icon">🎯</div>
          <div>
            <div class="detail-title">14-Day Free Pilot</div>
            <div class="detail-desc">No card required. No commitment. Just results.</div>
          </div>
        </div>
      </div>
    </div>

    <div>
      <form class="contact-form" id="contact-form">
        <div class="form-group">
          <label class="form-label">Your Name</label>
          <input class="form-input" type="text" name="name" placeholder="John Smith" required>
        </div>
        <div class="form-group">
          <label class="form-label">Company Name</label>
          <input class="form-input" type="text" name="company" placeholder="Smith Roofing Co." required>
        </div>
        <div class="form-group">
          <label class="form-label">Phone Number</label>
          <input class="form-input" type="tel" name="phone" placeholder="(901) 555-0000" required>
        </div>
        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input class="form-input" type="email" name="email" placeholder="you@smithroofing.com" required>
        </div>
        <div class="form-group">
          <label class="form-label">How many calls do you think you miss per week?</label>
          <select class="form-input" name="missed_calls" style="cursor:pointer;">
            <option value="">Rough estimate</option>
            <option>1–5 calls</option>
            <option>5–15 calls</option>
            <option>15–30 calls</option>
            <option>30+ calls</option>
            <option>Honestly not sure</option>
          </select>
        </div>
        <button type="submit" class="btn-primary" style="width:100%;text-align:center;font-size:15px;padding:16px;">
          Claim My Free Pilot →
        </button>
        <p style="font-size:11px;color:var(--gray);text-align:center;margin-top:4px;">No card. No commitment. I'll reach out personally.</p>
      </form>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-logo">ROOF<span>PULSE</span></div>
  <div style="display:flex;flex-direction:column;gap:4px;text-align:right;">
    <div class="footer-text">© <span id="yr"></span> RoofPulse · Collierville, TN · Built for local roofers</div>
    <div style="font-size:11px;color:#ffffff20;">v0.1.0 · Early access · {{ days_live }} days live</div>
  </div>
</footer>

<script>
// Year
document.getElementById('yr').textContent = new Date().getFullYear();

// Demo simulator
function runDemo() {
  const name  = document.getElementById('sim-name').value  || 'Mike Johnson';
  const phone = document.getElementById('sim-phone').value || '(901) 555-0142';
  const issue = document.getElementById('sim-issue').value || 'storm damage';
  const first = name.split(' ')[0];
  const thread = document.getElementById('sim-thread');
  const result = document.getElementById('sim-result');

  thread.innerHTML = `<p style="font-size:13px;color:var(--gray)">⚡ Missed call detected from ${phone}...</p>`;
  result.style.display = 'none';

  const msgs = [
    { dir:'out', label:'RoofPulse sent automatically (47s later)', text:`Hey ${first}! Sorry we missed your call — this is Smith Roofing Co. Are you dealing with ${issue}? We're local and can usually get someone out within a day or two for a free look. Just reply here and we'll sort it out. 🏠` },
    { dir:'in',  label:`${name} replied`,                          text:'Yes, I need someone to look at my roof. Can you come Thursday?' },
    { dir:'out', label:'RoofPulse replied automatically',          text:`Thursday works great, ${first}! I'll have someone there at 10am for a free inspection. You'll get a reminder the night before. Does that work for you?` },
    { dir:'in',  label:`${name} confirmed`,                        text:'Perfect, see you then!' },
    { dir:'out', label:'RoofPulse confirmed & logged',             text:`Awesome — you're all set for Thursday at 10am. We're looking forward to helping you out. See you then! ✅` },
  ];

  setTimeout(() => {
    thread.innerHTML = '';
    msgs.forEach((m, i) => {
      setTimeout(() => {
        const lbl = document.createElement('div');
        lbl.className = 'sim-meta' + (m.dir==='out' ? ' right' : '');
        lbl.textContent = m.label;

        const el = document.createElement('div');
        el.className = `sim-msg sim-${m.dir}`;
        el.textContent = m.text;
        el.style.animationDelay = '0s';

        thread.appendChild(lbl);
        thread.appendChild(el);
        thread.scrollTop = thread.scrollHeight;

        if (i === 0) {
          result.style.display = 'flex';
          // Update live stat counter
          const el = document.getElementById('stat-recovered');
          if (el) el.textContent = parseInt(el.textContent || 0) + 1;
        }
      }, i * 1000);
    });
  }, 1000);
}

// Contact form — Formspree fetch + redirect to thank you
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = contactForm.querySelector('button[type="submit"]');
    btn.textContent = 'Sending...';
    btn.disabled = true;

    try {
      const response = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      });
      if (response.ok) {
        window.location.href = '/thank-you';
      } else {
        btn.textContent = 'Claim My Free Pilot →';
        btn.disabled = false;
        alert('Something went wrong — message me directly at Hayesscale500@gmail.com');
      }
    } catch(err) {
      btn.textContent = 'Claim My Free Pilot →';
      btn.disabled = false;
      alert('Something went wrong — message me directly at Hayesscale500@gmail.com');
    }
  });
}
</script>

</body>
</html>
