import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="For my favorite person ❤️", page_icon="🎂", layout="centered")

bg_svg = """
<div class="bg-illu"><svg xmlns="http://w3.org" width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
<defs>
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="3" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/>
  </filter>
</defs>
<g transform="translate(65,35) rotate(-14)" filter="url(#glow)">
  <path d="M95 165 C95 165 15 112 15 58 C15 24 42 5 68 5 C84 5 95 18 95 18 C95 18 106 5 122 5 C148 5 175 24 175 58 C175 112 95 165 95 165 Z" fill="rgba(255,255,255,0.25)" stroke="#e56b96" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M95 148 C95 148 29 102 29 59 C29 33 50 18 70 18 C83 18 95 29 95 29 C95 29 107 18 120 18 C140 18 161 33 161 59 C161 102 95 148 95 148 Z" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="6,7" stroke-linecap="round"/>
  <path d="M185 35 C185 35 170 25 170 15 C170 8 175 4 180 4 C183 4 185 7 185 7 C185 7 187 4 190 4 C195 4 200 8 200 15 C200 25 185 35 185 35 Z" fill="#f48fb1" opacity="0.75"/>
</g>
<g transform="translate(1155,535) rotate(12)" filter="url(#glow)">
  <path d="M105 180 C105 180 15 122 15 62 C15 25 45 5 74 5 C92 5 105 19 105 19 C105 19 118 5 136 5 C165 5 195 25 195 62 C195 122 105 180 105 180 Z" fill="rgba(255,255,255,0.25)" stroke="#e56b96" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M105 162 C105 162 30 112 30 63 C30 34 53 18 76 18 C90 18 105 30 105 30 C105 30 120 18 134 18 C157 18 180 34 180 63 C180 112 105 162 105 162 Z" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="6,7" stroke-linecap="round"/>
</g>
<path d="M-10 430 C70 430 145 390 145 355 C145 330 115 330 115 355 C115 395 195 435 295 395" fill="none" stroke="#e56b96" stroke-width="2.3" stroke-dasharray="7,7" opacity="0.75"/>
<path d="M1450 430 C1370 430 1295 390 1295 355 C1295 330 1325 330 1325 355 C1325 395 1245 435 1145 395" fill="none" stroke="#e56b96" stroke-width="2.3" stroke-dasharray="7,7" opacity="0.75"/>
<path d="M1205 150 C1185 150 1170 135 1170 118 C1170 102 1182 89 1198 87 C1205 65 1226 50 1250 50 C1278 50 1301 70 1305 97 C1321 100 1333 113 1333 130 C1333 148 1318 162 1300 162 Z" fill="rgba(255,255,255,0.42)" stroke="#e56b96" stroke-width="2.3" opacity="0.8"/>
<path d="M110 730 C90 730 75 715 75 698 C75 682 87 669 103 667 C110 645 131 630 155 630 C183 630 206 650 210 677 C226 680 238 693 238 710 C238 728 223 742 205 742 Z" fill="rgba(255,255,255,0.42)" stroke="#e56b96" stroke-width="2.3" opacity="0.8"/>
<g fill="#e56b96" opacity="0.65">
  <path d="M310 55 L317 77 L339 84 L317 91 L310 113 L303 91 L281 84 L303 77 Z"/>
  <path d="M1080 155 L1085 170 L1100 175 L1085 180 L1080 195 L1075 180 L1060 175 L1075 170 Z"/>
  <path d="M295 755 L302 777 L324 784 L302 791 L295 813 L288 791 L266 784 L288 777 Z"/>
  <path d="M1040 740 L1046 758 L1064 764 L1046 770 L1040 788 L1034 770 L1016 764 L1034 758 Z"/>
</g>
</svg></div>
"""

icons = ("❄️", "❤️", "🌸", "✨", "🎈")
random.seed(520)
falling_html = "".join(f'<div class="falling-item" style="left:{random.randint(2, 96)}%;font-size:{random.randint(15, 24)}px;animation-duration:{round(random.uniform(7.0, 13.0), 1)}s;animation-delay:{round(random.uniform(-12.0, 0.0), 1)}s;">{random.choice(icons)}</div>' for _ in range(30))

css = """<style>
.stApp, [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #ffe5ec 0%, #ffd6e0 50%, #ffc2d1 100%) !important; overflow-x: hidden; }
header, [data-testid="stHeader"] { background: transparent !important; visibility: hidden; }
@keyframes gfloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
.bg-illu { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; animation: gfloat 6s ease-in-out infinite; }
[data-testid="stMain"] { position: relative; z-index: 1; }
@keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 0.9; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0.2; } }
.falling-item { position: fixed; top: -10%; z-index: 9999; pointer-events: none; animation: fall linear infinite; }
.status-box { text-align: center; color: #c9184a; font-family: Georgia, serif; font-size: 32px; font-style: italic; font-weight: bold; margin-top: 30px; margin-bottom: 15px; text-shadow: 1px 1px 6px rgba(255,255,255,0.8); }
.love-letter-card { background: rgba(255,255,255,0.88); backdrop-filter: blur(10px); color: #590d22; padding: 28px 24px; border-radius: 18px; text-align: center; font-family: Georgia, serif; font-size: 22px; font-style: italic; font-weight: bold; box-shadow: 0 10px 25px rgba(201,24,74,0.12); border: 1.5px solid rgba(255,117,143,0.45); margin: 25px auto; }
.baby-footer { text-align: center; color: #a4133c; font-size: 30px; font-weight: 900; margin-top: 20px; text-shadow: 1px 1px 4px rgba(255,255,255,0.7); }
.secret-letter-box { background: rgba(255,255,255,0.96); backdrop-filter: blur(12px); color: #590d22; padding: 34px 36px; border-radius: 22px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 16.5px; line-height: 1.9; text-align: left; box-shadow: 0 14px 35px rgba(201,24,74,0.22); border: 2px solid #ffb3c1; border-top: 6px solid #ff4d6d; margin-top: 26px; margin-bottom: 40px; }
.secret-letter-header { text-align: center; color: #ff4d6d; font-family: Georgia, serif; font-style: italic; font-size: 20px; font-weight: bold; margin-bottom: 18px; letter-spacing: 1px; }
.secret-letter-box p { margin-bottom: 15px; }
.secret-letter-sign { text-align: right; font-weight: 800; color: #c9184a; font-size: 18px; margin-top: 16px; margin-bottom: 0 !important; }
div[data-testid="stProgress"] > div > div > div > div { background-color: #ff4d6d !important; }
div.stButton > button { background: linear-gradient(90deg, #ff758f 0%, #ff4d6d 100%); color: white !important; border: none; border-radius: 25px; padding: 12px 24px; font-weight: bold; line-height: 1.4; box-shadow: 0 4px 15px rgba(255,77,109,0.35); transition: all 0.3s ease; }
div.stButton > button:hover { transform: scale(1.03); box-shadow: 0 6px 20px rgba(255,77,109,0.5); }
</style>"""

st.markdown(css + bg_svg + falling_html, unsafe_allow_html=True)

progress_bar = st.progress(0)
status_placeholder = st.empty()

_ = list(map(lambda i: (status_placeholder.markdown(f'<div style="text-align:center;color:#ff4d6d;font-weight:600;margin-top:40px;">💖 Loading babe\'s Birthday Surprise... {i + 1}%</div>', unsafe_allow_html=True), progress_bar.progress(i + 1), time.sleep(0.02)), range(100)))

progress_bar.empty()
status_placeholder.markdown('<div class="status-box">✨ You & Me ✨</div>', unsafe_allow_html=True)

st.balloons()
st.snow()

st.markdown('<div class="love-letter-card">“You are forever in my heart.” ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="baby-footer">HAPPY BIRTHDAY, MY GIRL. ❤️</div>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)
clicked = col2.button("ポチッとな！\n\nBoop me~ 🐾", use_container_width=True)

letter_html = """<div class="secret-letter-box">
<div class="secret-letter-header">💌 A Little Letter For You 💌</div>
<p>This is my first time celebrating your birthday with u. To me, today isn't just about your birthday, it's also about us being together for 5 months.</p>
<p>I still remember that one time u looked so adorable when u blushed looking into my eyes (I freaking felt it). Moments like that actually make me crazy 'bout u even more. I thought to myself, I just really wanted to cuddle with u. O~M~G. 🥺</p>
<p>Every day in the future, I also wanna make new memories with u, and just hope u can let go of all your stress whenever u're with me.</p>
<p class="secret-letter-sign">Having u in my life makes everything better. Happy Birthday, babe!</p>
</div>"""

if clicked: st.balloons(); st.snow(); st.markdown(letter_html, unsafe_allow_html=True)

b64_audio = base64.b64encode(open("song01.m4a", "rb").read()).decode() if clicked else ""
if b64_audio: st.markdown(f'<audio autoplay loop style="display:none;"><source src="data:audio/mp4;base64,{b64_audio}" type="audio/mp4"></audio>', unsafe_allow_html=True)
