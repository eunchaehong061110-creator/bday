import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="For my favorite person ❤️", page_icon="🎂", layout="centered")

bg_illustration_html = """
<div class="bg-illustration">
<svg xmlns="http://w3.org" width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
  <defs>
    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <linearGradient id="cloud-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#ffe5ec" stop-opacity="0.25"/>
    </linearGradient>
  </defs>

  <g transform="translate(65, 35) rotate(-14)" filter="url(#soft-glow)">
    <path d="M95 165 C95 165 15 112 15 58 C15 24 42 5 68 5 C84 5 95 18 95 18 C95 18 106 5 122 5 C148 5 175 24 175 58 C175 112 95 165 95 165 Z" fill="rgba(255,255,255,0.22)" stroke="#e56b96" stroke-width="2.8" stroke-linecap="round"/>
    <path d="M95 148 C95 148 29 102 29 59 C29 33 50 18 70 18 C83 18 95 29 95 29 C95 29 107 18 120 18 C140 18 161 33 161 59 C161 102 95 148 95 148 Z" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="6,7" stroke-linecap="round"/>
    <path d="M185 35 C185 35 170 25 170 15 C170 8 175 4 180 4 C183 4 185 7 185 7 C185 7 187 4 190 4 C195 4 200 8 200 15 C200 25 185 35 185 35 Z" fill="#f48fb1" opacity="0.75"/>
    <path d="M208 58 C208 58 198 51 198 44 C198 39 201 37 205 37 C207 37 208 39 208 39 C208 39 209 37 211 37 C215 37 218 39 218 44 C218 51 208 58 208 58 Z" fill="#f48fb1" opacity="0.6"/>
  </g>

  <g transform="translate(1155, 535) rotate(12)" filter="url(#soft-glow)">
    <path d="M105 180 C105 180 15 122 15 62 C15 25 45 5 74 5 C92 5 105 19 105 19 C105 19 118 5 136 5 C165 5 195 25 195 62 C195 122 105 180 105 180 Z" fill="rgba(255,255,255,0.22)" stroke="#e56b96" stroke-width="2.8" stroke-linecap="round"/>
    <path d="M105 162 C105 162 30 112 30 63 C30 34 53 18 76 18 C90 18 105 30 105 30 C105 30 120 18 134 18 C157 18 180 34 180 63 C180 112 105 162 105 162 Z" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="6,7" stroke-linecap="round"/>
    <path d="M-10 120 C-10 120 -25 110 -25 100 C-25 93 -20 89 -15 89 C-12 89 -10 92 -10 92 C-10 92 -8 89 -5 89 C0 89 5 93 5 100 C5 110 -10 120 -10 120 Z" fill="#f48fb1" opacity="0.7"/>
  </g>

  <g opacity="0.75">
    <path d="M -10 430 C 70 430, 145 390, 145 355 C 145 330, 115 330, 115 355 C 115 395, 195 435, 295 395" fill="none" stroke="#e56b96" stroke-width="2.3" stroke-dasharray="7,7" stroke-linecap="round"/>
    <path d="M312 396 C312 396 300 388 300 380 C300 375 304 372 308 372 C310 372 312 374 312 374 C312 374 314 372 316 372 C320 372 324 375 324 380 C324 388 312 396 312 396 Z" fill="#e56b96" transform="rotate(20 312 384)"/>
  </g>

  <g opacity="0.75">
    <path d="M 1450 430 C 1370 430, 1295 390, 1295 355 C 1295 330, 1325 330, 1325 355 C 1325 395, 1245 435, 1145 395" fill="none" stroke="#e56b96" stroke-width="2.3" stroke-dasharray="7,7" stroke-linecap="round"/>
    <path d="M1128 396 C1128 396 1116 388 1116 380 C1116 375 1120 372 1124 372 C1126 372 1128 374 1128 374 C1128 374 1130 372 1132 372 C1136 372 1140 375 1140 380 C1140 388 1128 396 1128 396 Z" fill="#e56b96" transform="rotate(-20 1128 384)"/>
  </g>

  <g transform="translate(1160, 45)" opacity="0.8">
    <path d="M45 105 C25 105 10 90 10 73 C10 57 22 44 38 42 C45 20 66 5 90 5 C118 5 141 25 145 52 C161 55 173 68 173 85 C173 103 158 117 140 117 L45 117 Z" fill="url(#cloud-grad)" stroke="#e56b96" stroke-width="2.3"/>
    <line x1="65" y1="117" x2="65" y2="148" stroke="#e56b96" stroke-width="1.8" stroke-dasharray="4,4"/>
    <path d="M65 148 L69 158 L79 162 L69 166 L65 176 L61 166 L51 162 L61 158 Z" fill="#f48fb1"/>
    <line x1="120" y1="117" x2="120" y2="138" stroke="#e56b96" stroke-width="1.8" stroke-dasharray="4,4"/>
    <circle cx="120" cy="144" r="4" fill="#f48fb1"/>
  </g>

  <g transform="translate(65, 625)" opacity="0.8">
    <path d="M45 105 C25 105 10 90 10 73 C10 57 22 44 38 42 C45 20 66 5 90 5 C118 5 141 25 145 52 C161 55 173 68 173 85 C173 103 158 117 140 117 L45 117 Z" fill="url(#cloud-grad)" stroke="#e56b96" stroke-width="2.3"/>
    <line x1="95" y1="117" x2="95" y2="145" stroke="#e56b96" stroke-width="1.8" stroke-dasharray="4,4"/>
    <path d="M95 162 C95 162 85 155 85 148 C85 144 88 141 91 141 C93 141 95 143 95 143 C95 143 97 141 99 141 C102 141 105 144 105 148 C105 155 95 162 95 162 Z" fill="#f48fb1"/>
  </g>

  <g fill="#e56b96" opacity="0.65">
    <path d="M310 55 L317 77 L339 84 L317 91 L310 113 L303 91 L281 84 L303 77 Z"/>
    <path d="M1080 155 L1085 170 L1100 175 L1085 180 L1080 195 L1075 180 L1060 175 L1075 170 Z"/>
    <path d="M295 755 L302 777 L324 784 L302 791 L295 813 L288 791 L266 784 L288 777 Z"/>
    <path d="M1040 740 L1046 758 L1064 764 L1046 770 L1040 788 L1034 770 L1016 764 L1034 758 Z"/>
  </g>
  <circle cx="255" cy="155" r="5" fill="#f48fb1" opacity="0.65"/>
  <circle cx="345" cy="130" r="6" fill="none" stroke="#e56b96" stroke-width="1.8" opacity="0.6"/>
  <circle cx="1115" cy="80" r="5" fill="none" stroke="#e56b96" stroke-width="1.8" opacity="0.6"/>
  <circle cx="350" cy="800" r="4.5" fill="#f48fb1" opacity="0.65"/>
  <circle cx="990" cy="610" r="5" fill="none" stroke="#e56b96" stroke-width="1.8" opacity="0.55"/>
</svg>
</div>
"""

icons = ["❄️", "❤️", "🌸", "✨", "🎈"]
falling_html = ""
random.seed(520)

for _ in range(30):
    icon = random.choice(icons)
    left = random.randint(2, 96)
    size = random.randint(15, 24)
    duration = round(random.uniform(7.0, 13.0), 1)
    delay = round(random.uniform(-12.0, 0.0), 1)
    falling_html += f'<div class="falling-item" style="left:{left}%;font-size:{size}px;animation-duration:{duration}s;animation-delay:{delay}s;">{icon}</div>'

custom_css = """
<style>
.stApp, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffe5ec 0%, #ffd6e0 50%, #ffc2d1 100%) !important;
    overflow-x: hidden;
}
header, [data-testid="stHeader"] {
    background: transparent !important;
    visibility: hidden;
}
@keyframes gentle-float {
    0%, 100% { transform: translateY(0px) scale(1); opacity: 0.92; }
    50% { transform: translateY(-6px) scale(1.008); opacity: 1; }
}
.bg-illustration {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    pointer-events: none;
    animation: gentle-float 6s ease-in-out infinite;
}
[data-testid="stMain"] {
    position: relative;
    z-index: 1;
}
@keyframes fall {
    0% { transform: translateY(-10vh) translateX(0px) rotate(0deg); opacity: 0.9; }
    50% { transform: translateY(50vh) translateX(15px) rotate(180deg); opacity: 0.7; }
    100% { transform: translateY(110vh) translateX(-15px) rotate(360deg); opacity: 0.2; }
}
.falling-item {
    position: fixed;
    top: -10%;
    z-index: 9999;
    pointer-events: none;
    animation: fall linear infinite;
}
.status-box {
    text-align: center;
    color: #c9184a;
    font-family: 'Georgia', 'Brush Script MT', cursive, serif;
    font-size: 32px;
    font-style: italic;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
    text-shadow: 1px 1px 6px rgba(255, 255, 255, 0.8);
}
.love-letter-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(10px);
    color: #590d22;
    padding: 28px 24px;
    border-radius: 16px;
    text-align: center;
    font-family: 'Georgia', serif;
    font-size: 22px;
    font-style: italic;
    font-weight: bold;
    box-shadow: 0 10px 25px rgba(201, 24, 74, 0.12);
    border: 1.5px solid rgba(255, 117, 143, 0.4);
    margin: 25px auto;
}
.baby-footer {
    text-align: center;
    color: #a4133c;
    font-size: 30px;
    font-weight: 900;
    margin-top: 20px;
    text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.7);
}
.secret-letter-box {
    background: rgba(255, 255, 255, 0.94);
    color: #590d22;
    padding: 28px 30px;
    border-radius: 18px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 16.5px;
    line-height: 1.85;
    text-align: left;
    box-shadow: 0 10px 28px rgba(201, 24, 74, 0.18);
    border: 1.5px solid #ffb3c1;
    margin-top: 20px;
}
.secret-letter-box p { margin-bottom: 14px; }
.secret-letter-sign {
    text-align: right;
    font-weight: 800;
    color: #c9184a;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 0 !important;
}
div[data-testid="stProgress"] > div > div > div > div { background-color: #ff4d6d !important; }
div.stButton > button {
    background: linear-gradient(90deg, #ff758f 0%, #ff4d6d 100%);
    color: white !important;
    border: none;
    border-radius: 25px;
    padding: 12px 24px;
    font-weight: bold;
    line-height: 1.4;
    box-shadow: 0 4px 15px rgba(255, 77, 109, 0.35);
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 20px rgba(255, 77, 109, 0.5);
}
</style>
"""

st.markdown(custom_css + bg_illustration_html + falling_html, unsafe_allow_html=True)

progress_bar = st.progress(0)
status_placeholder = st.empty()

for i in range(100):
    status_placeholder.markdown(f'<div style="text-align:center;color:#ff4d6d;font-weight:600;margin-top:40px;">💖 Loading babe\'s Birthday Surprise... {i + 1}%</div>', unsafe_allow_html=True)
    progress_bar.progress(i + 1)
    time.sleep(0.02)

progress_bar.empty()
status_placeholder.markdown('<div class="status-box">✨ You & Me ✨</div>', unsafe_allow_html=True)

st.balloons()
st.snow()

st.markdown('<div class="love-letter-card">“You are forever in my heart.” ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="baby-footer">HAPPY BIRTHDAY, MY GIRL. ❤️</div>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
