import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_new = '''    /* focus visibility */
    .choice-card:focus-visible,
    .seal-btn:focus-visible,
    .send-btn:focus-visible,
    .back-btn:focus-visible {
      outline: 2.5px solid var(--maroon);
      outline-offset: 3px;
    }

    /* ===== PREMIUM UI/UX ENHANCEMENTS ===== */
    .envelope-wrapper {
      position: fixed; inset: 0; z-index: 100;
      background: var(--cream);
      display: flex; align-items: center; justify-content: center;
      transition: opacity 0.8s ease, visibility 0.8s;
    }
    .envelope {
      position: relative; width: 300px; height: 180px;
      background: #e6c587; border-radius: 6px;
      box-shadow: 0 20px 40px rgba(59,34,51,0.2);
      cursor: pointer; transition: transform 0.4s ease;
    }
    .envelope:hover { transform: translateY(-5px) scale(1.02); }
    .env-flap {
      position: absolute; top: 0; left: 0; width: 0; height: 0;
      border-left: 150px solid transparent; border-right: 150px solid transparent;
      border-top: 100px solid #dcb56c;
      transform-origin: top; transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 3;
    }
    .env-body {
      position: absolute; bottom: 0; left: 0; width: 0; height: 0;
      border-left: 150px solid #f1d9a0; border-right: 150px solid #f1d9a0;
      border-bottom: 90px solid #e2c07c;
      z-index: 2;
    }
    .env-seal {
      position: absolute; top: 40px; left: 50%; transform: translateX(-50%);
      width: 54px; height: 54px; background: var(--maroon);
      border-radius: 50%; color: #fff; display: flex; align-items: center; justify-content: center;
      font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;
      box-shadow: 0 4px 10px rgba(122, 46, 59, 0.4);
      z-index: 4; transition: opacity 0.3s; text-align: center; line-height: 1.2;
    }
    .envelope.open .env-flap { transform: rotateX(180deg); z-index: 1; }
    .envelope.open .env-seal { opacity: 0; }
    .envelope.open {
      transform: translateY(150px); opacity: 0; pointer-events: none;
      transition: transform 0.8s ease 0.6s, opacity 0.8s ease 0.6s;
    }
    .envelope-wrapper.hidden {
      opacity: 0; visibility: hidden; pointer-events: none;
    }

    .ticket-scene { width: 100%; perspective: 1400px; }
    .ticket-container {
      position: relative; width: 100%;
      transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      transform-style: preserve-3d;
    }
    .ticket-container.is-flipped { transform: rotateY(180deg) !important; }
    .ticket-face {
      position: relative; width: 100%; backface-visibility: hidden;
      background: #fffaf2; border-radius: 22px; box-shadow: var(--paper-shadow);
      border: 1px solid rgba(122, 46, 59, 0.08); overflow: hidden;
    }
    .ticket-back {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      transform: rotateY(180deg); padding: 30px; display: flex; flex-direction: column;
      align-items: center; justify-content: center; text-align: center;
      background: linear-gradient(180deg, #fffaf2, #fdf6ea);
    }
    .flip-btn-front {
      position: absolute; top: 20px; right: 20px;
      background: rgba(217,140,149,0.15); color: var(--rose);
      border: none; padding: 6px 12px; border-radius: 100px;
      font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em;
      cursor: pointer; z-index: 10; transition: background 0.2s, transform 0.2s;
    }
    .flip-btn-front:hover { background: rgba(217,140,149,0.25); transform: translateY(-1px); }
    .flip-btn-back {
      background: none; border: none; color: var(--maroon); opacity: 0.65;
      font-family: 'Quicksand', sans-serif; font-weight: 600; font-size: 13px;
      cursor: pointer; display: flex; align-items: center; gap: 6px; padding: 6px 0; margin-top: auto;
    }
    .flip-btn-back:hover { opacity: 1; }
    
    .polaroid {
      background: #fff; padding: 10px 10px 30px; box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      transform: rotate(-3deg); margin-bottom: 24px; width: 70%; max-width: 220px;
    }
    .polaroid img { width: 100%; height: auto; display: block; aspect-ratio: 1; object-fit: cover; background: #eee; }
    .polaroid-text { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 16px; color: var(--maroon); margin-top: 10px; text-align: center; }
    .back-msg { font-size: 14px; line-height: 1.6; color: var(--plum); margin-bottom: 24px; font-weight: 500; }
    .countdown { display: flex; gap: 18px; margin-bottom: 20px; }
    .cd-item { display: flex; flex-direction: column; align-items: center; }
    .cd-val { font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; color: var(--maroon); line-height: 1; }
    .cd-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--rose); font-weight: 600; margin-top: 4px; }
    
    .glare {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(105deg, rgba(255,255,255,0) 20%, rgba(255,255,255,0.4) 50%, rgba(255,255,255,0) 80%);
      transform: translateX(-100%); transition: transform 0.1s; pointer-events: none; z-index: 5;
    }
  </style>'''

html = html.replace('''    /* focus visibility */
    .choice-card:focus-visible,
    .seal-btn:focus-visible,
    .send-btn:focus-visible,
    .back-btn:focus-visible {
      outline: 2.5px solid var(--maroon);
      outline-offset: 3px;
    }
  </style>''', css_new)

html = html.replace('''<body>

  <div class="stage">''', '''<body>

  <!-- Envelope Overlay -->
  <div class="envelope-wrapper" id="envelope-wrapper">
    <div class="envelope" id="envelope" onclick="openEnvelope()">
      <div class="env-flap"></div>
      <div class="env-body"></div>
      <div class="env-seal">Tap to<br>Open</div>
    </div>
  </div>

  <div class="stage">''')

html = html.replace('''<div class="ticket">
      <div class="ticket-top">''', '''<div class="ticket-scene">
      <div class="ticket-container" id="ticket-container">
        <!-- FRONT FACE -->
        <div class="ticket-face ticket-front">
          <div class="glare" id="glare"></div>
          <button class="flip-btn-front" onclick="flipTicket(event)">Flip ↺</button>
          
          <div class="ticket-top">''')

html = html.replace('''<div class="barcode" id="barcode"></div>
        <div class="date-tag"><small>Valid for</small>06 · 07 · 2026</div>
      </div>
    </div>''', '''<div class="barcode" id="barcode"></div>
          <div class="date-tag"><small>Valid for</small>06 · 07 · 2026</div>
        </div>
      </div> <!-- End front face -->

      <!-- BACK FACE -->
      <div class="ticket-face ticket-back">
        <div class="polaroid">
          <!-- PLACEHOLDER PHOTO: Replace the src URL below with your actual photo link! -->
          <img src="https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=600&auto=format&fit=crop" alt="Us" />
          <div class="polaroid-text">Can't wait! 💕</div>
        </div>
        <p class="back-msg">Happy Birthday Chimsuu!<br>I am so excited to spend this special day with you. Here's a little countdown until the fun begins:</p>
        <div class="countdown" id="countdown">
          <div class="cd-item"><span class="cd-val" id="cd-d">00</span><span class="cd-label">Days</span></div>
          <div class="cd-item"><span class="cd-val" id="cd-h">00</span><span class="cd-label">Hrs</span></div>
          <div class="cd-item"><span class="cd-val" id="cd-m">00</span><span class="cd-label">Min</span></div>
          <div class="cd-item"><span class="cd-val" id="cd-s">00</span><span class="cd-label">Sec</span></div>
        </div>
        <button class="flip-btn-back" onclick="flipTicket(event)">‹ Back to front</button>
      </div> <!-- End back face -->
    </div>
  </div>''')

js_additions = '''// ---- state machine ----
    let choice = { main: null, sub: null };

    // ---- sound effects ----
    const popSound = new Audio('https://assets.mixkit.co/active_storage/sfx/2568/2568-preview.mp3');
    const chimeSound = new Audio('https://assets.mixkit.co/active_storage/sfx/1435/1435-preview.mp3');
    popSound.volume = 0.5;
    chimeSound.volume = 0.6;

    function playPop() { popSound.currentTime = 0; popSound.play().catch(()=>{}); }
    function playChime() { chimeSound.currentTime = 0; chimeSound.play().catch(()=>{}); }

    // ---- envelope unboxing ----
    function openEnvelope() {
      const envWrapper = document.getElementById('envelope-wrapper');
      const env = document.getElementById('envelope');
      env.classList.add('open');
      playChime();
      
      // Start bg music upon first interaction (opening envelope)
      if (!musicPlayed) {
        bgMusic.play().catch(e => console.log('Autoplay blocked:', e));
        musicPlayed = true;
      }
      
      setTimeout(() => {
        envWrapper.classList.add('hidden');
      }, 1400);
    }

    // ---- 3D Flip & Tilt ----
    const ticketContainer = document.getElementById('ticket-container');
    const glare = document.getElementById('glare');
    let isFlipped = false;

    function flipTicket(e) {
      if(e) e.stopPropagation();
      playPop();
      isFlipped = !isFlipped;
      if (isFlipped) {
        ticketContainer.classList.add('is-flipped');
      } else {
        ticketContainer.classList.remove('is-flipped');
      }
    }

    // Interactive Tilt on mousemove
    document.addEventListener('mousemove', (e) => {
      if (isFlipped || !ticketContainer) return;
      
      const rect = ticketContainer.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      
      const x = e.clientX - centerX;
      const y = e.clientY - centerY;
      
      const rotateX = -(y / (window.innerHeight/2)) * 10; 
      const rotateY = (x / (window.innerWidth/2)) * 10;
      
      ticketContainer.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      
      const glarePercent = ((e.clientX / window.innerWidth) * 200) - 100;
      if(glare) glare.style.transform = `translateX(${glarePercent}%)`;
    });
    
    document.addEventListener('mouseleave', () => {
      if (!isFlipped && ticketContainer) ticketContainer.style.transform = `rotateX(0deg) rotateY(0deg)`;
      if(glare) glare.style.transform = `translateX(-100%)`;
    });
    
    // ---- countdown logic ----
    const targetDate = new Date('2026-07-06T12:00:00').getTime();
    
    setInterval(() => {
      const now = new Date().getTime();
      const diff = targetDate - now;
      
      if (diff > 0) {
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diff % (1000 * 60)) / 1000);
        
        document.getElementById('cd-d').textContent = days.toString().padStart(2, '0');
        document.getElementById('cd-h').textContent = hours.toString().padStart(2, '0');
        document.getElementById('cd-m').textContent = mins.toString().padStart(2, '0');
        document.getElementById('cd-s').textContent = secs.toString().padStart(2, '0');
      }
    }, 1000);'''
html = html.replace('''// ---- state machine ----
    let choice = { main: null, sub: null };''', js_additions)

html = html.replace('function goMain() {', 'function goMain() {\n      playPop();')
html = html.replace('function goSub(which) {', 'function goSub(which) {\n      playPop();')
html = html.replace('function selectMain(main, sub) {', 'function selectMain(main, sub) {\n      playPop();')
html = html.replace('function celebrate() {', 'function celebrate() {\n      playChime();')

html = html.replace('''document.body.addEventListener('click', () => {
      if (!musicPlayed) {
        bgMusic.play().catch(e => console.log('Autoplay blocked by browser:', e));
        musicPlayed = true;
      }
    });''', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
