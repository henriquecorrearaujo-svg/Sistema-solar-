import streamlit as st

st.set_page_config(
    page_title="Sistema Solar App",
    page_icon="🪐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.stApp {
    background: radial-gradient(circle at top, #1b2735 0%, #090a0f 100%);
    color: #ffffff;
}
.planet-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 24px;
    padding: 24px 18px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
    margin-bottom: 18px;
}
.planet-emoji {
    font-size: 76px;
    line-height: 1.1;
    margin-bottom: 8px;
}
.planet-title {
    font-size: 30px;
    font-weight: 800;
    margin: 0;
    color: #ffffff;
}
.planet-subtitle {
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #f39c12;
    font-weight: 700;
    margin-top: 4px;
    margin-bottom: 14px;
}
.planet-desc {
    font-size: 15px;
    color: #cfd8dc;
    line-height: 1.5;
    margin-bottom: 20px;
}
.stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    text-align: left;
}
.stat-box {
    background: rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 12px;
}
.stat-label {
    font-size: 12px;
    color: #90a4ae;
    margin-bottom: 4px;
}
.stat-value {
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

planetas = {
    "☀️ Sol": {
        "nome": "Sol", "icone": "☀️", "sub": "A Nossa Estrela",
        "desc": "Concentra 99,86% de toda a massa do Sistema Solar e gera a energia que mantém a vida na Terra.",
        "dist": "Centro do Sistema", "ano": "230 milhões de anos",
        "temp": "5.500 °C", "luas": "8 Planetas", "grav": 27.9
    },
    "🪨 Mercúrio": {
        "nome": "Mercúrio", "icone": "🪨", "sub": "O Menor e Mais Rápido",
        "desc": "O planeta mais próximo do Sol. Tem dias escaldantes e noites congelantes por quase não ter atmosfera.",
        "dist": "57,9 milhões km", "ano": "88 dias terrestres",
        "temp": "167 °C (Média)", "luas": "0", "grav": 0.38
    },
    "🌕 Vénus": {
        "nome": "Vénus", "icone": "🌕", "sub": "O Mais Quente",
        "desc": "A sua densa atmosfera cria um efeito de estufa extremo, tornando-o mais quente que Mercúrio.",
        "dist": "108,2 milhões km", "ano": "225 dias terrestres",
        "temp": "464 °C (Média)", "luas": "0", "grav": 0.91
    },
    "🌍 Terra": {
        "nome": "Terra", "icone": "🌍", "sub": "Nosso Mundo Azul",
        "desc": "O maior dos planetas rochosos e o único local conhecido no universo com água líquida estável na superfície e vida ativa.",
        "dist": "149,6 milhões km", "ano": "365,25 dias",
        "temp": "15 °C (Média)", "luas": "1 (Lua)", "grav": 1.0
    },
    "🔴 Marte": {
        "nome": "Marte", "icone": "🔴", "sub": "O Planeta Vermelho",
        "desc": "Rico em óxido de ferro na superfície, abriga o Monte Olimpo, o maior vulcão de todo o Sistema Solar.",
        "dist": "227,9 milhões km", "ano": "687 dias terrestres",
        "temp": "-65 °C (Média)", "luas": "2 (Fobos e Deimos)", "grav": 0.38
    },
    "🟠 Júpiter": {
        "nome": "Júpiter", "icone": "🟠", "sub": "O Gigante Gasoso",
        "desc": "O maior planeta do Sistema Solar. A sua Grande Mancha Vermelha é uma tempestade maior que a própria Terra.",
        "dist": "778,5 milhões km", "ano": "11,86 anos terrestres",
        "temp": "-110 °C (Média)", "luas": "95 conhecidas", "grav": 2.34
    },
    "🪐 Saturno": {
        "nome": "Saturno", "icone": "🪐", "sub": "O Senhor dos Anéis",
        "desc": "Famoso pelo seu deslumbrante sistema de anéis formados por biliões de pedaços de gelo e rocha espacial.",
        "dist": "1,43 mil milhões km", "ano": "29,45 anos terrestres",
        "temp": "-140 °C (Média)", "luas": "146 conhecidas", "grav": 1.06
    },
    "🔵 Úrano": {
        "nome": "Úrano", "icone": "🔵", "sub": "O Gigante de Gelo",
        "desc": "Roda praticamente deitado sobre a sua órbita e tem uma atmosfera gelada rica em metano que lhe dá a cor azul-celeste.",
        "dist": "2,87 mil milhões km", "ano": "84 anos terrestres",
        "temp": "-195 °C (Média)", "luas": "28 conhecidas", "grav": 0.92
    },
    "🌀 Neptuno": {
        "nome": "Neptuno", "icone": "🌀", "sub": "O Planeta dos Ventos",
        "desc": "O planeta mais distante do Sol, varrido pelos ventos supersónicos mais rápidos de todo o Sistema Solar.",
        "dist": "4,50 mil milhões km", "ano": "164,8 anos terrestres",
        "temp": "-200 °C
