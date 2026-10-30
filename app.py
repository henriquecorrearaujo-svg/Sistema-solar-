# Sistema-solar-
import streamlit as st

# Configuração da página para abrir como App Mobile
st.set_page_config(
    page_title="Sistema Solar App",
    page_icon="🪐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS para deixar com cara de aplicativo nativo de celular
st.markdown("""
<style>
    /* Esconde menus padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fundo escuro espacial */
    .stApp {
        background: radial-gradient(circle at top, #1b2735 0%, #090a0f 100%);
        color: #ffffff;
    }
    
    /* Card Principal do Planeta */
    .planet-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        padding: 24px 18px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 16px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }
    
    .planet-emoji {
        font-size: 75px;
        line-height: 1.1;
        margin-bottom: 8px;
        filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.25));
    }
    
    .planet-title {
        font-size: 28px;
        font-weight: 800;
        margin: 0;
        color: #f8fafc;
    }
    
    .planet-subtitle {
        font-size: 13px;
        color: #ffd166;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .planet-desc {
        font-size: 14.5px;
        color: #cbd5e1;
        line-height: 1.5;
    }
    
    /* Caixas de Estatísticas */
    .stat-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-top: 16px;
    }
    
    .stat-box {
        background: rgba(0, 0, 0, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 12px;
        text-align: left;
    }
    
    .stat-label {
        font-size: 11px;
        color: #94a3b8;
        text-transform: uppercase;
    }
    
    .stat-value {
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 2px;
    }
</style>
""", unsafe_allow_html=True)

# Banco de dados dos planetas
PLANETAS = {
    "☀️ Sol": {
        "nome": "Sol",
        "icone": "☀️",
        "sub": "Estrela Central",
        "desc": "Concentra 99,86% de toda a massa do Sistema Solar. Gera energia através da fusão nuclear de hidrogênio em hélio no seu núcleo.",
        "dist": "0 km (Centro)",
        "ano": "230 mi anos (Galáxia)",
        "temp": "5.500 °C",
        "luas": "8 Planetas",
        "gravidade": 27.9
    },
    "☿️ Mercúrio": {
        "nome": "Mercúrio",
        "icone": "🌑",
        "sub": "Menor Planeta Rochoso",
        "desc": "O planeta mais próximo do Sol e o mais rápido em sua órbita. Sem atmosfera densa, sofre variações extremas de temperatura.",
        "dist": "57,9 milhões km",
        "ano": "88 dias terrestres",
        "temp": "-180°C a 430°C",
        "luas": "0",
        "gravidade": 0.38
    },
    "♀️ Vênus": {
        "nome": "Vênus",
        "icone": "🌕",
        "sub": "O Planeta Mais Quente",
        "desc": "Possui uma atmosfera densa de dióxido de carbono com nuvens de ácido sulfúrico, criando o efeito estufa mais forte do Sistema Solar.",
        "dist": "108,2 milhões km",
        "ano": "225 dias terrestres",
        "temp": "465 °C",
        "luas": "0",
        "gravidade": 0.90
    },
    "🌍 Terra": {
        "nome": "Terra",
        "icone": "🌍",
        "sub": "Nosso Mundo Azul",
        "desc": "O maior dos planetas rochosos e o único local conhecido no universo com água líquida estável na superfície e vida ativa.",
        "dist": "149,6 milhões km",
        "ano": "365,25 dias",
        "temp": "15 °C (Média)",
        "luas": "1 (Lua)",
        "gravidade": 1.00
    },
    "♂️ Marte": {
        "nome": "Marte",
        "icone": "🔴",
        "sub": "O Planeta Vermelho",
        "desc": "Sua cor avermelhada vem do óxido de ferro (ferrugem) no solo. Abriga o Monte Olimpo, um vulcão três vezes mais alto que o Everest.",
        "dist": "227,9 milhões km",
        "ano": "687 dias terrestres",
        "temp": "-63 °C (Média)",
        "luas": "2 (Fobos e Deimos)",
        "gravidade": 0.38
    },
    "♃ Júpiter": {
        "nome": "Júpiter",
        "icone": "🟠",
        "sub": "Gigante Gasoso",
        "desc": "O maior planeta do Sistema Solar. Sua Grande Mancha Vermelha é uma tempestade gigante que dura há séculos e cabe a Terra dentro.",
        "dist": "778,5 milhões km",
        "ano": "11,8 anos terrestres",
        "temp": "-110 °C",
        "luas": "95 confirmadas",
        "gravidade": 2.53
    },
    "♄ Saturno": {
        "nome": "Saturno",
        "icone": "🪐",
        "sub": "O Senhor dos Anéis",
        "desc": "Conhecido pelo seu brilhante e complexo sistema de anéis formados por bilhões de blocos de gelo e poeira cósmica.",
        "dist": "1,43 bilhão km",
        "ano": "29,4 anos terrestres",
        "temp": "-140 °C",
        "luas": "146 confirmadas",
        "gravidade": 1.06
    },
    "♅ Urano": {
        "nome": "Urano",
        "icone": "🔵",
        "sub": "Gigante de Gelo",
        "desc": "Tem a atmosfera mais fria do Sistema Solar e uma inclinação única: ele gira praticamente deitado de lado em relação à sua órbita.",
        "dist": "2,87 bilhões km",
        "ano": "84 anos terrestres",
        "temp": "-195 °C",
        "luas": "28 confirmadas",
        "gravidade": 0.89
    },
    "♆ Netuno": {
        "nome": "Netuno",
        "icone": "🌀",
        "sub": "Mundo dos Ventos Supersônicos",
        "desc": "O planeta mais distante do Sol. Possui os ventos mais fortes do Sistema Solar, podendo atingir mais de 2.100 km/h.",
        "dist": "4,50 bilhões km",
        "ano": "165 anos terrestres",
        "temp": "-201 °C",
        "luas": "16 confirmadas",
        "gravidade": 1.14
    }
}

# Cabeçalho do App
st.markdown("<h2 style='text-align: center; margin-bottom: 2px;'>🌌 Explorador Solar</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px; margin-bottom: 15px;'>Selecione um astro abaixo para inspecionar</p>", unsafe_allow_html=True)

# Seletor de Planetas
escolha = st.selectbox(
    "Escolha o Astro:",
    options=list(PLANETAS.keys()),
    index=3, # Inicia na Terra
    label_visibility="collapsed"
)

dados = PLANETAS[escolha]

# Renderização do Card com HTML/CSS
st.markdown(f"""
<div class="planet-card">
    <div class="planet-emoji">{dados['icone']}</div>
    <div class="planet-title">{dados['nome']}</div>
    <div class="planet-subtitle">{dados['sub']}</div>
    <div class="planet-desc">{dados['desc']}</div>
    
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">📏 Distância do Sol</div>
            <div class="stat-value">{dados['dist']}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">🗓️ Duração do Ano</div>
            <div class="stat-value">{dados['ano']}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">🌡️ Temperatura</div>
            <div class="stat-value">{dados['temp']}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">🌙 Satélites</div>
            <div class="stat-value">{dados['luas']}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Ferramenta Interativa: Simulador de Gravidade
with st.expander("⚖️ Simulador de Gravidade: Quanto você pesaria lá?"):
    peso_terra = st.slider("Seu peso na Terra (kg):", min_value=10, max_value=150, value=75, step=1)
    peso_astro = peso_terra * dados["gravidade"]
    st.metric(
        label=f"Seu peso em {dados['nome']}",
        value=f"{peso_astro:.1f} kg",
        delta=f"{dados['gravidade']}x a gravidade da Terra"
    )
