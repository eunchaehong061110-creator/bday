import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="For my loml ❤️", page_icon="🎂", layout="centered")

@st.cache_data
def get_song(path):
    with open(path, "rb") as f: return base64.b64encode(f.read()).decode()

b64_audio = get_song("song01.m4a")

svg_a = '<div class="bg-illu"><svg xmlns="http://w3.org" width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">'
svg_b = '<defs><filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter></defs>'
svg_c = '<g transform="translate(65,35) rotate(-14)" filter="url(#glow)"><path d="M95 165 C95 165 15 112 15 58 C15 24 42 5 68 5 C84 5 95 18 95 18 C95 18 106 5 122 5 C148 5 175 24 175 58 C175 112 95 165 95 165 Z" fill="rgba(255,255,255,0.28)" stroke="#e56b96" stroke-width="2.5" stroke-linecap="round"/><path d="M95 148 C95 148 29 102 29 59 C29 33 50 18 70 18 C83 18 95 29 95 29 C95 29 107 18 120 18 C140 18 161 33 161 59 C161 102 95 148 95 148 Z" fill="none" stroke="#e56b96" stroke-width="2" stroke-dasharray="6,7" stroke-linecap="round"/><path d="M185 35 C185 35 170 25 170 15 C170 8 175 4 180 4 C183 4 185 7 185 7 C185 7 187 4 190 4 C195 4 200 8 200 15 C200 25 185 35 185 35 Z" fill="#f48fb1" opacity="0.75"/></g>'
svg_d = '<g transform="translate(1155,535) rotate(12)" filter="url(#glow)"><path d="M105 180 C105 180 15 122 15 62 C15 25 45 5 74 5 C92 5 105 19 105 19 C105 19 118 5 136 5 C165 5 195 25 195 62 C195 122 105 180 105 180 Z" fill="rgba(255,255,255,0.28)" stroke="#e56b96" stroke-width="2.5" stroke-linecap="round"/><path d="M105 162 C105 162 30 112 30 63 C30 34 53 18 76 18 C90 18 105 30 105 30 C105 30 120 18 134 18 C157 18 180 34 180 63 C180 112 105 162 105 162 Z" fill="none" stroke="#e56b96" stroke-width="2" stroke-dasharray="6,7" stroke-linecap="round"/></g>'
svg_e = '<path d="M-10 430 C70 430 145 390 145 355 C145 330 115 330 115 355 C115 395 195 435 295 395" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="7,7" opacity="0.7"/><path d="M1450 430 C1370 430 1295 390 1295 355 C1295 330 1325 330 1325 355 C1325 395 1245 435 1145 395" fill="none" stroke="#e56b96" stroke-width="2.2" stroke-dasharray="7,7" opacity="0.7"/>'
svg_f = '<path d="M1205 150 C1185 150 1170 135 1170 118 C1170 102 1182 89 1198 87 C1205 65 1226 50 1250 50 C1278 50 1301 70 1305 97 C1321 100 1333 113 1333 130 C1333 148 1318 162 1300 162 Z" fill="rgba(255,255,255,0.45)" stroke="#e56b96" stroke-width="2.2" opacity="0.8"/><path d="M110 730 C90 730 75 715 75 698 C75 682 87 669 103 667 C110 645 131 630 155 630 C183 630 206 650 210 677 C226 680 238 693 238 710 C238 728 223 742 205 742 Z" fill="rgba(255,255,255,0.45)" stroke="#e56b96" stroke-width="2.2" opacity="0.8"/>'
svg_g = '<g fill="#e56b96" opacity="0.65"><path d="M310 55 L317 77 L339 84 L317 91 L310 113 L303 91 L281 84 L303 77 Z"/><path d="M1080 155 L1085 170 L1100 175 L1085 180 L1080 195 L1075 180 L1060 175 L1075 170 Z"/><path d="M295 755 L302 777 L324 784 L302 791 L295 813 L288 791 L266 784 L288 777 Z"/><path d="M1040 740 L1046 758 L1064 764 L1046 770 L1040 788 L1034 770 L1016 764 L1034 758 Z"/></g></svg></div>'

bg_svg = svg_a + svg_b + svg_c + svg_d + svg_e + svg_f + svg_g

icons = ("❄️", "❤️", "🌸", "✨", "🎈")
random.seed(520)
falling_html = "".join(f'<div class="falling-item" style="left:{random.randint(2, 96)}%;font-size:{random.randint(15, 24)}px;animation-duration:{round(random.uniform(7.0, 13.0), 1)}s;animation-delay:{round(random.uniform(-12.0, 0.0), 1)}s;">{random.choice(icons)}</div>' for _ in range(30))

c1 = '<style>@import url("https://googleapis.com");'
c2 = '.stApp, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at top left, #fff0f4 0%, #ffe0e9 45%, #ffd1df 100%) !important; overflow-x: hidden; } header, [data-testid="stHeader"] { background: transparent !important; visibility: hidden; } [data-testid="stDecoration"], canvas, .stBalloons, .stSnow { pointer-events: none !important; }'
c3 = '@keyframes gfloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-6px); } } .bg-illu { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; animation: gfloat 6s ease-in-out infinite; } [data-testid="stMain"] { position: relative; z-index: 10; }'
c4 = '@keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 0.9; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0.2; } } .falling-item { position: fixed; top: -10%; z-index: 9999; pointer-events: none; animation: fall linear infinite; }'
c5 = '.title-wrap { display: flex; align-items: center; justify-content: center; gap: 16px; margin-top: 22px; margin-bottom: 10px; } .title-line-l { width: 85px; height: 1.5px; background: linear-gradient(90deg, transparent, #e06388); } .title-line-r { width: 85px; height: 1.5px; background: linear-gradient(270deg, transparent, #e06388); } .title-ornament { color: #d94673; font-size: 16px; letter-spacing: 4px; opacity: 0.85; }'
c6 = '.status-box { text-align: center; color: #b52b55; font-family: "Great Vibes", cursive; font-size: 54px; font-weight: 400; text-shadow: 0 2px 12px rgba(255,255,255,0.95); letter-spacing: 2px; line-height: 1.1; }'
c7 = '.love-letter-card { background: linear-gradient(145deg, rgba(255,252,253,0.92), rgba(255,240,245,0.82)); backdrop-filter: blur(14px); color: #8c1d40; padding: 34px 28px; border-radius: 24px; text-align: center; font-family: "Playfair Display", Georgia, serif; font-size: 25px; font-style: italic; font-weight: 500; letter-spacing: 0.6px; box-shadow: 0 15px 35px rgba(181,43,85,0.12); border: 1.5px solid rgba(235,130,162,0.5); margin: 20px auto; }'
c8 = '.baby-footer { text-align: center; background: linear-gradient(90deg, #a81c46, #d94673, #a81c46); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: "Playfair Display", serif; font-size: 28px; font-weight: 700; letter-spacing: 2.5px; margin-top: 22px; }'
c9 = '.secret-letter-box { background: linear-gradient(180deg, rgba(255,253,254,0.97) 0%, rgba(255,244,247,0.95) 100%); backdrop-filter: blur(16px); color: #6e1832; padding: 38px 40px; border-radius: 26px; font-family: "Lora", Georgia, serif; font-size: 17px; line-height: 1.95; text-align: left; box-shadow: 0 18px 45px rgba(181,43,85,0.16); border: 1.5px solid #f5a3bc; margin-top: 28px; margin-bottom: 45px; }'
c10 = '.secret-letter-header { text-align: center; color: #c93863; font-family: "Great Vibes", cursive; font-size: 38px; margin-bottom: 18px; border-bottom: 1px dashed rgba(229,107,150,0.4); padding-bottom: 10px; } .secret-letter-box p { margin-bottom: 16px; } .secret-letter-sign { text-align: right; font-family: "Playfair Display", serif; font-style: italic; font-weight: 600; color: #b52b55; font-size: 18.5px; margin-top: 20px; margin-bottom: 0 !important; }'
c11 = 'div[data-testid="stProgress"] > div > div > div > div { background-color: #e0527d !important; } div.stButton { position: relative; z-index: 99999 !important; } div.stButton > button { background: linear-gradient(135deg, #f2799b 0%, #d9436e 100%); color: #fff8fa !important; font-family: "Lora", serif; letter-spacing: 0.8px; border: 1px solid rgba(255,255,255,0.5); border-radius: 30px; padding: 14px 26px; font-weight: 600; line-height: 1.45; box-shadow: 0 8px 22px rgba(217,67,110,0.3); cursor: pointer !important; }</style>'

css = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11

st.markdown(css + bg_svg + falling_html, unsafe_allow_html=True)

if "loaded" not in st.session_state: st.session_state.loaded = False

progress_bar = st.progress(0) if not st.session_state.loaded else None
status_placeholder = st.empty()

if not st.session_state.loaded: _ = list(map(lambda i: (status_placeholder.markdown(f'<div style="text-align:center;color:#d9436e;font-family:Lora,serif;font-style:italic;font-size:17px;margin-top:40px;">💖 Loading babe\'s Birthday Surprise... {i + 1}%</div>', unsafe_allow_html=True), progress_bar.progress(i + 1), time.sleep(0.015)), range(100))); progress_bar.empty(); st.session_state.loaded = True

title_html = '<div class="title-wrap"><span class="title-line-l"></span><span class="title-ornament">✦ ♡</span><span class="status-box">You &amp; Me</span><span class="title-ornament">♡ ✦</span><span class="title-line-r"></span></div>'
status_placeholder.markdown(title_html, unsafe_allow_html=True)

if "first_fx" not in st.session_state: st.balloons(); st.snow(); st.session_state.first_fx = True

st.markdown('<div class="love-letter-card">“You are forever in my heart.” ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="baby-footer">HAPPY BIRTHDAY, MY GIRL. ❤️</div>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)
clicked = col2.button("ポチッとな！\n\nBoop me~ 🐾", key="boop_btn", use_container_width=True)

l1 = '<div class="secret-letter-box"><div class="secret-letter-header">A Little Letter For You</div>'
l2 = "<p>This is my first time celebrating your birthday with u. To me, today isn't just about your birthday, it's also a celebration of us.💘</p>"
l3 = "<p>I still remember that one time u looked so adorable when u blushed looking into my eyes (I freaking felt it). Moments like that actually make me crazy 'bout u even more. I thought to myself, I just really wanted to cuddle with u. O~M~G. 🥺</p>"
l4 = "<p>Every day in the future, I also wanna make new memories with u, and just hope u can let go of all your stress whenever u're with me.</p>"
l5 = '<p class="secret-letter-sign">Having u in my life makes everything better. Happy Birthday, babe!</p></div>'

letter_html = l1 + l2 + l3 + l4 + l5

