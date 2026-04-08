import streamlit as st
import time
import random
from voice.listen import ouvir
from voice.speak import falar
from core.brain import perguntar_ia

st.set_page_config(layout="wide")

# 🎨 CSS LIMPO SEM RADAR
st.markdown("""
<style>
/* 🌌 FUNDO + PARTÍCULAS */
.stApp {
    background: radial-gradient(circle at center, #020617 0%, #000000 100%);
    overflow: hidden;
}
.particle {
    position: absolute;
    width: 3px;
    height: 3px;
    background: #22d3ee;
    border-radius: 50%;
    opacity: 0.6;
    animation: float 10s infinite linear;
}
@keyframes float {
    from { transform: translateY(100vh); opacity: 0; }
    to { transform: translateY(-10vh); opacity: 1; }
}

/* 🧠 título */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #22d3ee;
    text-shadow: 0 0 20px #22d3ee;
}

/* 🔵 CORE */
.core {
    position: relative;
    width: 300px;
    height: 300px;
    margin: auto;
}
.ring1, .ring2, .ring3, .center { border-radius: 50%; position: absolute; }
.ring1 { width: 100%; height: 100%; border: 2px solid rgba(34,211,238,0.4); animation: spin 20s linear infinite; }
.ring2 { width: 240px; height: 240px; top: 30px; left: 30px; border: 2px dashed #22d3ee; animation: spinReverse 12s linear infinite; }
.ring3 { width: 180px; height: 180px; top: 60px; left: 60px; border: 2px solid #22c55e; box-shadow: 0 0 40px #22c55e; }
.center { width: 80px; height: 80px; top: 110px; left: 110px; background: radial-gradient(circle, #22d3ee, #020617); box-shadow: 0 0 30px #22d3ee; }

/* animações */
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes spinReverse { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }

/* 🎤 estados */
.listening .ring3 { box-shadow: 0 0 100px #22d3ee; }
.speaking .ring3 { box-shadow: 0 0 120px #22c55e; }

/* 🔊 equalizador */
.equalizer { display: flex; justify-content: center; gap: 5px; margin-top: 20px; }
.bar { width: 6px; background: #22d3ee; box-shadow: 0 0 10px #22d3ee; animation: bounce 1s infinite ease-in-out; }
@keyframes bounce { 0%,100% { height: 10px; } 50% { height: 40px; } }

/* cards */
.card {
    border: 1px solid rgba(34,211,238,0.3);
    padding: 15px; border-radius: 12px;
    background: rgba(0,0,0,0.3);
    box-shadow: 0 0 15px rgba(34,211,238,0.3);
}

/* 🔘 BOTÃO FIXO */
div[data-testid="stButton"] > button {
    position: fixed; bottom: 40px; left: 50%; transform: translateX(-50%);
    z-index: 9999; background: rgba(0,0,0,0.6);
    border: 1px solid #22d3ee; padding: 12px 30px; border-radius: 10px;
    color: #22d3ee; font-size: 16px; box-shadow: 0 0 15px #22d3ee;
    transition: 0.3s;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 0 30px #22d3ee; transform: translateX(-50%) scale(1.05);
}

/* resposta */
.resposta-box {
    position: fixed; bottom: 120px; left: 50%; transform: translateX(-50%);
    width: 500px; background: rgba(0,0,0,0.7);
    border: 1px solid #22d3ee; border-radius: 12px;
    padding: 15px; color: #22d3ee; box-shadow: 0 0 20px #22d3ee;
}
</style>
""", unsafe_allow_html=True)

# ⚡ partículas
particles = ""
for _ in range(40):
    left = random.randint(0, 100)
    delay = random.uniform(0, 10)
    particles += f'<div class="particle" style="left:{left}%; animation-delay:{delay}s;"></div>'
st.markdown(particles, unsafe_allow_html=True)

# 🧠 estado
if "status" not in st.session_state: st.session_state.status = "idle"
if "resposta" not in st.session_state: st.session_state.resposta = ""
if "comando" not in st.session_state: st.session_state.comando = ""
if "volume" not in st.session_state: st.session_state.volume = 0

# 🧱 layout
col1, col2, col3 = st.columns([1,2,1])

# 🔹 esquerda
with col1:
    st.markdown('<div class="card">⚙️ Sistema OK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">🧠 IA conectada</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">🎤 Microfone ativo</div>', unsafe_allow_html=True)

# 🔸 centro
with col2:
    resposta_box = st.empty()
    st.markdown('<div class="title">JARVIS</div>', unsafe_allow_html=True)

    # 🔵 CORE
    st.markdown(f"""
    <div class="core {st.session_state.status}">
        <div class="ring1"></div>
        <div class="ring2"></div>
        <div class="ring3"></div>
        <div class="center"></div>
    </div>
    """, unsafe_allow_html=True)

    # 🔊 equalizador
    bars = ""
    for i in range(10):
        height = int(st.session_state.volume * 300 + random.randint(10, 40))
        bars += f'<div class="bar" style="height:{height}px"></div>'
    st.markdown(f'<div class="equalizer">{bars}</div>', unsafe_allow_html=True)

    # botão
    if st.button("🎤 ATIVAR"):
        st.session_state.status = "listening"

    # LISTENING
    if st.session_state.status == "listening":
        resultado = ouvir(duracao=5)
        if resultado:
            st.session_state.comando = resultado[0]
            st.session_state.volume = resultado[1]
        else:
            st.session_state.comando = ""
            st.session_state.volume = 0
        st.session_state.status = "thinking"

    # THINKING
    if st.session_state.status == "thinking":
        if not st.session_state.comando:
            st.session_state.resposta = "Não entendi o que você disse."
        else:
            st.session_state.resposta = perguntar_ia(st.session_state.comando)
        st.session_state.status = "speaking"

    # SPEAKING
    if st.session_state.status == "speaking":
        resposta_box.markdown(f"""
        <div class="resposta-box">
            <p><b>Você:</b> {st.session_state.comando}</p>
            <p><b>Jarvis:</b> {st.session_state.resposta}</p>
        </div>
        """, unsafe_allow_html=True)
        falar(st.session_state.resposta)
        time.sleep(1)
        st.session_state.status = "idle"

# 🔹 direita
import psutil  # pip install psutil

# 🔹 direita
with col3:
    # CPU
    cpu_percent = psutil.cpu_percent(interval=0.5)
    st.markdown(f'<div class="card">⚡ CPU: {cpu_percent}%</div>', unsafe_allow_html=True)
    
    # Memória
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    st.markdown(f'<div class="card">🧠 Memória: {mem_percent}%</div>', unsafe_allow_html=True)