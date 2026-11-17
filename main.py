import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="For my favorite person ❤️", page_icon="🎂", layout="centered")

# ==========================================
# 🎨 可愛矢量背景插畫（雙層虛線愛心、雲朵、菱形星星、弧形虛線）
# ==========================================
bg_svg = """<svg xmlns="http://w3.org" width="1440" height="900" viewBox="0 0 1440 900">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe5ec"/>
      <stop offset="50%" stop-color="#ffd6e0"/>
      <stop offset="100%" stop-color="#ffc2d1"/>
    </linearGradient>
  </defs>
  <rect width="1440" height="900" fill="url(#bg-grad)"/>

  <g transform="translate(80, 40) rotate(-12)">
    <path d="M80 140 C80 140 15 95 15 50 C15 22 38 5 60 5 C73 5 80 15 80 15 C80 15 87 5 100 5 C122 5 145 22 145 50 C145 95 80 140 80 140 Z" fill="none" stroke="#f497b6" stroke-width="2.5" opacity="0.7"/>
    <path d="M80 126 C80 126 27 88 27 51 C27 30 44 17 61 17 C72 17 80 26 80 26 C80 26 88 17 99 17 C116 17 133 30 133 51 C133 88 80 126 80 126 Z" fill="none" stroke="#f497b6" stroke-width="2" stroke-dasharray="6,6" opacity="0.7"/>
  </g>

  <g transform="translate(1180, 560) rotate(10)">
    <path d="M90 160 C90 160 15 108 15 56 C15 24 42 5 67 5 C82 5 90 17 90 17 C90 17 98 5 113 5 C138 5 165 24 165 56 C165 108 90 160 90 160 Z" fill="none" stroke="#f497b6" stroke-width="2.5" opacity="0.7"/>
    <path d="M90 144 C90 144 29 100 29 57 C29 33 49 18 68 18 C80 18 90 28 90 28 C90 28 100 18 112 18 C131 18 151 33 151 57 C151 100 90 144 90 144 Z" fill="none" stroke="#f497b6" stroke-width="2" stroke-dasharray="6,6" opacity="0.7"/>
  </g>

  <path d="M1210 150 C1190 150 1175 135 1175 118 C1175 102 1187 89 1203 87 C1210 65 1231 50 1255 50 C1283 50 1306 70 1310 97 C1326 100 1338 113 1338 130 C1338 148 1323 162 1305 162 L1210 162 Z" fill="rgba(255,255,255,0.35)" stroke="#f497b6" stroke-width="2.2" opacity="0.7"/>

  <path d="M95 730 C75 730 60 715 60 698 C60 682 72 669 88 667 C95 645 116 630 140 630 C168 630 191 650 195 677 C211 680 223 693 223 710 C223 728 208 742 190 742 L95 742 Z" fill="rgba(255,255,255,0.35)" stroke="#f497b6" stroke-width="2.2" opacity="0.7"/>

  <path d="M 30 410 Q 170 360 310 420" fill="none" stroke="#f497b6" stroke-width="2.2" stroke-dasharray="8,8" opacity="0.65"/>
  <path d="M 1130 410 Q 1270 360 1410 420" fill="none" stroke="#f497b6" stroke-width="2.2" stroke-dasharray="8,8" opacity="0.65"/>

  <path d="M280 50 L287 72 L309 79 L287 86 L280 108 L273 86 L251 79 L273 72 Z" fill="#f497b6" opacity="0.6"/>
  <path d="M1110 180 L1116 198 L1134 204 L1116 210 L1110 228 L1104 210 L1086 204 L1104 198 Z" fill="#f497b6" opacity="0.55"/>
  <path d="M260 760 L267 782 L289 789 L267 796 L260 818 L253 796 L231 789 L253 782 Z" fill="#f497b6" opacity="0.6"/>
  <path d="M1070 730 L1075 745 L1090 750 L1075 755 L1070 770 L1065 755 L1050 750 L1065 745 Z" fill="#f497b6" opacity="0.55"/>
  <circle cx="220" cy="180" r="5" fill="#f497b6" opacity="0.55"/>
  <circle cx="310" cy="805" r="4" fill="#f497b6" opacity="0.55"/>
  <circle cx="1160" cy="70" r="4.5" fill="#f497b6" opacity="0.55"/>
  <circle cx="960" cy="560" r="4" fill="#f497b6" opacity="0.5"/>
</svg>"""

# 改用 Base64 編碼，確保所有瀏覽器都能 100% 顯示背景插畫
b64_svg = base64.b64encode(bg_svg.encode("utf-8")).decode("utf-8")

# ==========================================
# 飄落愛心與花瓣特效
# ==========================================
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

st.markdown(f"""<style>
.stApp {{
    background-color: #ffd6e0 !important;
    background-image: url("data:image/svg+xml;base64,{b64_svg}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    overflow-x: hidden;
}}
header, [data-testid="stHeader"] {{
    background: transparent !important;
    visibility: hidden;
}}

@keyframes fall {{
    0% {{ transform: translateY(-10vh) translateX(0px) rotate(0deg); opacity: 0.9; }}
    50% {{ transform: translateY(50vh) translateX(15px) rotate(180deg); opacity: 0.7; }}
    100% {{ transform: translateY(110vh) translateX(-15px) rotate(360deg); opacity: 0.2; }}
}}
.falling-item {{
    position: fixed;
    top: -10%;
    z-index: 9999;
    pointer-events: none;
    animation: fall linear infinite;
}}
.status-box {{
    text-align: center;
    color: #c9184a;
    font-family: 'Georgia', 'Brush Script MT', cursive, serif;
    font-size: 32px;
    font-style: italic;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
    text-shadow: 1px 1px 6px rgba(255, 255, 255, 0.8);
}}
.love-letter-card {{
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
}}
.baby-footer {{
    text-align: center;
    color: #a4133c;
    font-size: 30px;
    font-weight: 900;
    margin-top: 20px;
    text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.7);
}}
.secret-letter-box {{
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
}}
.secret-letter-box p {{ margin-bottom: 14px; }}
.secret-letter-sign {{
    text-align: right;
    font-weight: 800;
    color: #c9184a;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 0 !important;
}}
div[data-testid="stProgress"] > div > div > div > div {{ background-color: #ff4d6d !important; }}
div.stButton > button {{
    background: linear-gradient(90deg, #ff758f 0%, #ff4d6d 100%);
    color: white !important;
    border: none;
    border-radius: 25px;
    padding: 12px 24px;
    font-weight: bold;
    line-height: 1.4;
    box-shadow: 0 4px 15px rgba(255, 77, 109, 0.35);
    transition: all 0.3s ease;
}}
div.stButton > button:hover {{
    transform: scale(1.03);
    box-shadow: 0 6px 20px rgba(255, 77, 109, 0.5);
}}
</style>{falling_html}""", unsafe_allow_html=True)

progress_bar = st.progress(0)
status_placeholder = st.empty()

for i in range(100):
    status_placeholder.markdown(f'<div style="text-align:center;color:#ff4d6d;font-weight:600;margin-top:40px;">💖 Loading babe\'s Birthday Surprise... {i + 1}%</div>',
                                unsafe_allow_html=True)
    progress_bar.progress(i + 1)
    time.sleep(0.02)

progress_bar.empty()
status_placeholder.markdown('<div class="status-box">✨ You & Me ✨</div>', unsafe_allow_html=True)

st.balloons()
st.snow()

st.markdown("""<div class="love-letter-card">“You are forever in my heart.” ❤️</div>""", unsafe_allow_html=True)
st.markdown('<div class="baby-footer">HAPPY BIRTHDAY, MY GIRL. ❤️</div>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    clicked = st.button("ポチッとな！\n\nBoop me~ 🐾", use_container_width=True)

if clicked:
    st.balloons()
    st.snow()

    with open("song01.m4a", "rb") as f:
        b64_audio = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <audio autoplay loop style="display:none;">
            <source src="data:audio/mp4;base64,{b64_audio}" type="audio/mp4">
        </audio>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="secret-letter-box">
<p>This is my first time celebrating your birthday with u. To me, today isn't just about your birthday, it's also about us being together for 5 months.</p>
<p>I still remember that one time u looked so adorable when u blushed looking into my eyes (I freaking felt it). Moments like that actually make me crazy 'bout u even more. I thought to myself, I just really wanted to cuddle with u. O~M~G. 🥺</p>
<p>Every day in the future, I also wanna make new memories with u, and just hope u can let go of all your stress whenever u're with me.</p>
<p class="secret-letter-sign">Having u in my life makes everything better. Happy Birthday, babe!</p>
</div>""", unsafe_allow_html=True)
