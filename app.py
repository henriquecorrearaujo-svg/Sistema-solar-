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
    "Sol": {
        "nome": "Sol", "icone": "☀️", "sub": "A Nossa Estrela",
        "desc": "Concentra 99,86% de toda a massa do Sistema Solar e gera a energia que mantém a vida na Terra.",
        "dist": "Centro do Sistema", "ano": "230 milhoes de anos",
        "temp": "5.500 graus C", "luas": "8 Planetas", "grav": 27.9
    },
    "Mercurio": {
        "nome": "Mercurio", "icone": "🪨", "sub": "O Menor e Mais Rapido",
        "desc": "O planeta mais proximo do Sol. Tem dias escaldantes e noites congelantes por quase nao ter atmosfera.",
        "dist": "57,9 milhoes km", "ano": "88 dias terrestres",
        "temp": "167 graus C (Media)", "luas": "0", "grav": 0.38
    },
    "Venus": {
        "nome": "Venus", "icone": "🌕", "sub": "O Mais Quente",
        "desc": "A sua densa atmosfera cria um efeito de estufa extremo, tornando-o mais quente que Mercurio.",
        "dist": "108,2 milhoes km", "ano": "225 dias terrestres",
        "temp": "464 graus C (Media)", "luas": "0", "grav": 0.91
    },
    "Terra": {
        "nome": "Terra", "icone": "🌍", "sub": "Nosso Mundo Azul",
        "desc": "O maior dos planetas rochosos e o unico local conhecido no universo com agua liquida estavel na superficie e vida ativa.",
        "dist": "149,6 milhoes km", "ano": "365,25 dias",
        "temp": "15 graus C (Media)", "luas": "1 (Lua)", "grav": 1.0
    },
    "Marte": {
        "nome": "Marte", "icone": "🔴", "sub": "O Planeta Vermelho",
        "desc": "Rico em oxido de ferro na superficie, abriga o Monte Olimpo, o maior vulcao de todo o Sistema Solar.",
        "dist": "227,9 milhoes km", "ano": "687 dias terrestres",
        "temp": "-65 graus C (Media)", "luas": "2 (Fobos e Deimos)", "grav": 0.38
    },
    "Jupter": {
        "nome": "Jupter", "icone": "🟠", "sub": "O Gigante Gasoso",
        "desc": "O maior planeta do Sistema Solar. A sua Grande Mancha Vermelha e uma tempestade maior que a propria Terra.",
        "dist": "778,5 milhoes km", "ano": "11,86 anos terrestres",
        "temp": "-110 graus C (Media)", "luas": "95 conhecidas", "grav": 2.34
    },
    "Saturno": {
        "nome": "Saturno", "icone": "🪐", "sub": "O Senhor dos Aneis",
        "desc": "Famoso pelo seu deslumbrante sistema de aneis formados por bilioes de pedacos de gelo e rocha espacial.",
        "dist": "1,43 mil milhoes km", "ano": "29,45 anos terrestres",
        "temp": "-140 graus C (Media)", "luas": "146 conhecidas", "grav": 1.06
    },
    "Urano": {
        "nome": "Urano", "icone": "🔵", "sub": "O Gigante de Gelo",
        "desc": "Roda praticamente deitado sobre a sua orbita e tem uma atmosfera gelada rica em metano que lhe da a cor azul-celeste.",
        "dist": "2,87 mil milhoes km", "ano": "84 anos terrestres",
        "temp": "-195 graus C (Media)", "luas": "28 conhecidas", "grav": 0.92
    },
    "Neptuno": {
        "nome": "Neptuno", "icone": "🌀", "sub": "O Planeta dos Ventos",
        "desc": "O planeta mais distante do Sol, varrido pelos ventos supersonicos mais rapidos de todo o Sistema Solar.",
        "dist": "4,50 mil milhoes km", "ano": "164,8 anos terrestres",
        "temp": "-200 graus C (Media)", "luas": "16 conhecidas", "grav": 1.19
    }
}

escolha = st.selectbox("Escolha um astro para explorar:", list(planetas.keys()), index=3, label_visibility="collapsed")
dados = planetas[escolha]

html_card = (
    f'<div class="planet-card">'
    f'<div class="planet-emoji">{dados["icone"]}</div>'
    f'<div class="planet-title">{dados["nome"]}</div>'
    f'<div class="planet-subtitle">{dados["sub"]}</div>'
    f'<div class="planet-desc">{dados["desc"]}</div>'
    f'<div class="stat-grid">'
    f'<div class="stat-box"><div class="stat-label">📏 Distancia do Sol</div><div class="stat-value">{dados["dist"]}</div></div>'
    f'<div class="stat-box"><div class="stat-label">🗓️ Duracao do Ano</div><div class="stat-value">{dados["ano"]}</div></div>'
    f'<div class="stat-box"><div class="stat-label">🌡️ Temperatura</div><div class="stat-value">{dados["temp"]}</div></div>'
    f'<div class="stat-box"><div class="stat-label">🌙 Satelites</div><div class="stat-value">{dados["luas"]}</div></div>'
    f'</div></div>'
)

st.markdown(html_card, unsafe_allow_html=True)

with st.expander("⚖️ Simulador de Gravidade: Quanto voce pesaria la?"):
    peso = st.slider("Seu peso na Terra (kg):", 10, 
