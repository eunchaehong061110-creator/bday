import streamlit as st
import streamlit.components.v1 as components
import time
import random

st.set_page_config(page_title="For my favorite person ❤️", page_icon="🎂", layout="centered")

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

bg_illustration_html = """<div class="bg-illust"><svg width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://w3.org"><g fill="none" stroke="#ff4d6d" stroke-linecap="round" stroke-linejoin="round"><path d="M110 160 C 110 115, 175 115, 175 160 C 175 115, 240 115, 240 160 C 240 220, 175 265, 175 265 C 175 265, 110 220, 110 160 Z" stroke-width="3" opacity="0.32" transform="rotate(-15 175 180)"/><path d="M124 166 C 124 132, 175 132, 175 166 C 175 132, 226 132, 226 166 C 226 212, 175 248, 175 248 C 175 248, 124 212, 124 166 Z" stroke-width="2" stroke-dasharray="6 6" opacity="0.28" transform="rotate(-15 175 180)"/><path d="M1200 580 C 1200 530, 1270 530, 1270 580 C 1270 530, 1340 530, 1340 580 C 1340 645, 1270 695, 1270 695 C 1270 695, 1200 645, 1200 580 Z" stroke-width="3" opacity="0.32" transform="rotate(14 1270 610)"/><path d="M1215 586 C 1215 548, 1270 548, 1270 586 C 1270 548, 1325 548, 1325 586 C 1325 636, 1270 676, 1270 676 C 1270 676, 1215 636, 1215 586 Z" stroke-width="2" stroke-dasharray="6 6" opacity="0.28" transform="rotate(14 1270 610)"/><path d="M90 650 Q 90 620, 125 620 Q 145 595, 180 610 Q 215 605, 225 635 Q 250 645, 240 675 Q 230 695, 195 695 L 115 695 Q 80 690, 90 650 Z" stroke-width="2.5" opacity="0.28"/><path d="M1190 190 Q 1190 165, 1220 165 Q 1240 140, 1275 155 Q 1305 150, 1315 178 Q 1340 188, 1330 215 Q 1320 232, 1285 232 L 1210 232 Q 1180 228, 1190 190 Z" stroke-width="2.5" opacity="0.28"/><path d="M310 120 L318 140 L338 148 L318 156 L310 176 L302 156 L282 148 L302 140 Z" fill="#ff758f" stroke="none" opacity="0.38"/><path d="M1120 360 L1127 377 L1144 384 L1127 391 L1120 408 L1113 391 L1096 384 L1113 377 Z" fill="#ff758f" stroke="none" opacity="0.38"/><path d="M290 740 L296 755 L311 761 L296 767 L290 782 L284 767 L269 761 L284 755 Z" fill="#ff758f" stroke="none" opacity="0.35"/><path d="M1080 760 L1086 774 L1100 780 L1086 786 L1080 800 L1074 786 L1060 780 L1074 774 Z" fill="#ff758f" stroke="none" opacity="0.35"/><path d="M60 420 Q 180 350, 290 440" stroke-width="2.5" stroke-dasharray="8 10" opacity="0.32"/><path d="M1130 460 Q 1250 390, 1380 480" stroke-width="2.5" stroke-dasharray="8 10" opacity="0.32"/><circle cx="240" cy="330" r="5" fill="#ff758f" stroke="none" opacity="0.35"/><circle cx="1170" cy="290" r="6" fill="#ff758f" stroke="none" opacity="0.35"/><circle cx="330" cy="560" r="5" fill="#ff758f" stroke="none" opacity="0.32"/><circle cx="1110" cy="670" r="5" fill="#ff758f" stroke="none" opacity="0.32"/></g></svg></div>"""

st.markdown(f"""<style>
.stApp {{
    background: linear-gradient(135deg, #fff0f3 0%, #ffe3e8 50%, #ffd6e0 100%);
    overflow-x: hidden;
}}
header {{visibility: hidden;}}
.bg-illust {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    pointer-events: none;
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
    color: #ff4d6d;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 16px;
    font-weight: 600;
    margin-top: 40px;
    margin-bottom: 15px;
}}
.cursive-header {{
    text-align: center;
    color: #c9184a;
    font-family: 'Snell Roundhand', 'Apple Chancery', 'Brush Script MT', cursive !important;
    font-size: 46px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 10px;
    text-shadow: 1px 1px 6px rgba(255, 117, 143, 0.35);
}}
.love-letter-card {{
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    color: #c9184a;
    padding: 32px 24px;
    border-radius: 20px;
    text-align: center;
    font-family: 'Georgia', serif;
    font-size: 24px;
    font-style: italic;
    font-weight: bold;
    box-shadow: 0 12px 30px rgba(201, 24, 74, 0.12);
    border: 1.5px solid rgba(255, 117, 143, 0.5);
    margin: 30px auto;
}}
.baby-footer {{
    display: block;
    width: 100%;
    text-align: center;
    color: #a4133c;
    font-size: 32px;
    font-weight: 900;
    margin-top: 25px;
    padding-left: 10px;
    text-shadow: 1px 1px 4px rgba(255, 117, 143, 0.4);
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
    margin-top: 12px;
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
</style>{bg_illustration_html}{falling_html}""", unsafe_allow_html=True)

progress_bar = st.progress(0)
status_placeholder = st.empty()

for i in range(100):
    status_placeholder.markdown(f'<div class="status-box">💖 Loading babe\'s Birthday Surprise... {i+1}%</div>', unsafe_allow_html=True)
    progress_bar.progress(i + 1)
    time.sleep(0.02)

progress_bar.empty()
status_placeholder.markdown('<div class="cursive-header">✨ You &amp; Me ✨</div>', unsafe_allow_html=True)

st.balloons()
st.snow()

st.markdown("""<div class="love-letter-card">“You are forever in my heart.” ❤️</div>""", unsafe_allow_html=True)

st.markdown('<div class="baby-footer">HAPPY BIRTHDAY, MY GIRL. ❤️</div>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)
with col2:
    clicked = st.button("ポチッとな！\n\nBoop me~ 🐾", use_container_width=True)

if clicked:
    st.balloons()
    st.snow()
    st.write("")
    components.iframe("https://spotify.com", height=80)
    st.markdown("""<div class="secret-letter-box">
<p>This is my first time celebrating your birthday with u. To me, today isn't just about your birthday, it's also about us being together for 5 months.</p>
<p>I still remember that one time u looked so adorable when u blushed looking into my eyes (I freaking felt it). Moments like that actually make me crazy 'bout u even more. I thought to myself, I just really wanted to cuddle with u. O~M~G. 🥺</p>
<p>Every day in the future, I also wanna make new memories with u, and just hope u can let go of all your stress whenever u're with me.</p>
<p class="secret-letter-sign">Having u in my life makes everything better. Happy Birthday, babe!</p>
</div>""", unsafe_allow_html=True)
