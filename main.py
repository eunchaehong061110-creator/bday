import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="For my favorite person ❤️", page_icon="🎂", layout="centered")

# 精簡無換行的純淨 SVG 背景，確保所有瀏覽器 100% 正常顯示
bg_svg = '<svg xmlns="http://w3.org" width="1200" height="800" viewBox="0 0 1200 800"><g transform="translate(50, 20) rotate(-10)"><path d="M70,40 C70,15 35,15 35,40 C35,65 70,90 70,105 C70,90 105,65 105,40 C105,15 70,15 70,40 Z" fill="none" stroke="#f4acb7" stroke-width="2.5"/><path d="M70,46 C70,26 42,26 42,46 C42,66 70,86 70,98 C70,86 98,66 98,46 C98,26 70,26 70,46 Z" fill="none" stroke="#f4acb7" stroke-width="1.5" stroke-dasharray="4,4"/></g><g transform="translate(1010, 520) rotate(12)"><path d="M70,40 C70,15 35,15 35,40 C35,65 70,90 70,105 C70,90 105,65 105,40 C105,15 70,15 70,40 Z" fill="none" stroke="#f4acb7" stroke-width="2.5"/><path d="M70,46 C70,26 42,26 42,46 C42,66 70,86 70,98 C70,86 98,66 98,46 C98,26 70,26 70,46 Z" fill="none" stroke="#f4acb7" stroke-width="1.5" stroke-dasharray="4,4"/></g><path d="M1040,120 Q1040,95 1065,95 Q1085,75 1110,95 Q1135,95 1135,120 Q1150,120 1150,138 Q1150,155 1130,155 L1045,155 Q1025,155 1025,138 Q1025,120 1040,120 Z" fill="none" stroke="#f4acb7" stroke-width="2"/><path d="M60,610 Q60,585 85,585 Q105,565 130,585 Q155,585 155,610 Q170,610 170,628 Q170,645 150,645 L65,645 Q45,645 45,628 Q45,610 60,610 Z" fill="none" stroke="#f4acb7" stroke-width="2"/><path d="M230,70 Q235,95 260,100 Q235,105 230,130 Q225,105 200,100 Q225,95 230,70 Z" fill="#ffccd5"/><path d="M960,420 Q965,445 990,450 Q965,455 960,480 Q955,455 930,450 Q955,445 960,420 Z" fill="#ffccd5"/><path d="M190,710 Q194,730 214,734 Q194,738 190,758 Q186,738 166,734 Q186,730 190,710 Z" fill="#ffccd5"/><path d="M1060,290 Q1063,305 1078,308 Q1063,311 1060,326 Q1057,311 1042,308 Q1057,305 1060,290 Z" fill="#ffccd5"/><path d="M-20,380 Q90,340 190,410" fill="none" stroke="#f4acb7" stroke-width="2" stroke-dasharray="6,6"/><path d="M1010,360 Q1110,320 1220,380" fill="none" stroke="#f4acb7" stroke-width="2" stroke-dasharray="6,6"/><circle cx="310" cy="40" r="4" fill="#ffccd5"/><circle cx="980" cy="210" r="4" fill="#ffccd5"/><circle cx="240" cy="740" r="4" fill="#ffccd5"/><circle cx="920" cy="680" r="4" fill="#ffccd5"/></svg>'
bg_b64 = base64.b64encode(bg_svg.encode("utf-8")).decode("utf-8")

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
    background-color: #ffe3e8 !important;
    background-image: url("data:image/svg+xml;base64,{bg_b64}"), linear-gradient(135deg, #fff0f3 0%, #ffe3e8 50%, #ffd6e0 100%) !important;
    background-size: cover, cover !important;
    background-position: center, center !important;
    background-attachment: fixed, fixed !important;
    overflow-x: hidden;
}}
header {{visibility: hidden;}}

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
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 32px;
    font-style: italic;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
    text-shadow: 1px 1px 3px rgba(255, 117, 143, 0.3);
}}
.loading-box {{
    text-align: center;
    color: #ff4d6d;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 16px;
    font-weight: 600;
    margin-top: 40px;
    margin-bottom: 15px;
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
    margin: 25px auto;
}}
.baby-footer {{
    text-align: center;
    color: #a4133c;
    font-size: 32px;
    font-weight: 900;
    margin-top: 25px;
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
    status_placeholder.markdown(f'<div class="loading-box">💖 Loading babe\'s Birthday Surprise... {i + 1}%</div>',
                                unsafe_allow_html=True)
    progress_bar.progress(i + 1)
    time.sleep(0.02)

progress_bar.empty()
status_placeholder.markdown('<div class="status-box">✨ You &amp; Me ✨</div>', unsafe_allow_html=True)

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
<p>This is my first time celebrating your birthday with u. To me, today isn't just about your birthday, it's also a celebration of us.</p>
<p>I still remember that one time u looked so adorable when u blushed looking into my eyes (I freaking felt it). Moments like that actually make me crazy 'bout u even more. I thought to myself, I just really wanted to cuddle with u. O~M~G. 🥺</p>
<p>Every day in the future, I also wanna make new memories with u, and just hope u can let go of all your stress whenever u're with me.</p>
<p class="secret-letter-sign">Having u in my life makes everything better. Happy Birthday, babe!</p>
</div>""", unsafe_allow_html=True)
