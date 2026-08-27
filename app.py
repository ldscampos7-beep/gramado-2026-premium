
import streamlit as st
from urllib.parse import quote_plus
from datetime import datetime, date
from zoneinfo import ZoneInfo
import json

# =========================================================
# CONFIGURAÇÃO
# =========================================================
st.set_page_config(
    page_title="Gramado 2026 — Meu Guia",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="expanded"
)

TRIP_START = date(2026, 9, 2)
TRIP_END = date(2026, 9, 6)
TZ = ZoneInfo("America/Sao_Paulo")

HOTEL_NAME = "Hotel Laghetto Premio"
HOTEL_ADDRESS = "Av. Borges de Medeiros, 1533, Gramado, RS"
HOTEL = f"{HOTEL_NAME}, {HOTEL_ADDRESS}"

# =========================================================
# VISUAL
# =========================================================
st.markdown("""
<style>
.block-container {
    padding-top: .8rem;
    padding-bottom: 4rem;
    max-width: 980px;
}
.hero {
    padding: 22px;
    border-radius: 24px;
    border: 1px solid rgba(128,128,128,.18);
    margin-bottom: 16px;
}
.card {
    padding: 16px 18px;
    border-radius: 18px;
    border: 1px solid rgba(128,128,128,.20);
    margin: 8px 0 12px 0;
}
.card h4 { margin: 0 0 6px 0; }
.muted { opacity: .72; font-size: .92rem; }
.badge {
    display:inline-block;
    padding:4px 9px;
    border-radius:999px;
    border:1px solid rgba(128,128,128,.25);
    margin-right:5px;
    margin-bottom:5px;
    font-size:.82rem;
}
div[data-testid="stMetric"] {
    border:1px solid rgba(128,128,128,.18);
    border-radius:16px;
    padding:10px;
}
.stButton>button, .stLinkButton>a { border-radius:12px !important; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# DADOS DO ROTEIRO
# =========================================================
ROTEIRO = {
    "Dia 2": {
        "data": "02/09/2026",
        "titulo": "Chegada + Centro + Fondue",
        "icone": "✨",
        "resumo": "Chegada tranquila, almoço econômico, primeiro passeio pelo centro e fondue à noite.",
        "jantar": "Maison de La Fondue",
        "look": "Viagem/chegada: polo preta + jeans slim + Adidas ou Nike preto. Moletom preto na mão. Para o centro e fondue: camisa social marrom + calça escura + bomber preta Marfino; tênis marrom acamurçado. Se esfriar mais, acrescente suéter.",
        "itens": [
            ("14:00", "Check-in no Hotel Laghetto Premio", HOTEL, "hotel"),
            ("14:30", "Almoço — Sabor da Nonna (Plano A; chegar antes do encerramento do almoço)", "Restaurante Sabor da Nonna, Gramado RS", "a pé/Uber"),
            ("14:40+", "Plano B se atrasar — Empório Benetti", "Empório Benetti, Gramado RS", "a pé/Uber"),
            ("15:30", "Retorno ao hotel / descanso e organização", HOTEL, "hotel"),
            ("17:00", "Rua Coberta", "Rua Coberta, Gramado RS", "a pé"),
            ("17:30", "Igreja Matriz São Pedro", "Igreja Matriz São Pedro, Gramado RS", "a pé"),
            ("17:45", "Fonte do Amor Eterno", "Fonte do Amor Eterno, Gramado RS", "a pé"),
            ("18:00", "Chocolate / café no centro", "Centro de Gramado RS", "a pé"),
            ("18:30", "Palácio dos Festivais + Borges de Medeiros", "Palácio dos Festivais, Gramado RS", "a pé"),
            ("20:00", "Jantar — Maison de La Fondue", "Maison de La Fondue, Gramado RS", "a pé/Uber"),
            ("22:00", "Caminhada noturna pelo centro / Rua Coberta", "Rua Coberta, Gramado RS", "a pé"),
            ("22:30", "Retorno ao Hotel Laghetto Premio", HOTEL, "a pé/Uber"),
        ]
    },
    "Dia 3": {
        "data": "03/09/2026",
        "titulo": "City Tour Gramado + Canela",
        "icone": "🚌",
        "resumo": "Dia completo com a Turistur; à noite, jantar leve e centro iluminado.",
        "jantar": "Jantar leve / livre no centro",
        "look": "City Tour Gramado/Canela: camiseta básica preta ou marrom + calça escura + Nike preto + casaco cáqui. Leve o suéter na mochila. À noite: polo preta + calça azul-escura/chumbo + casaco marrom Bluestel + tênis marrom acamurçado.",
        "itens": [
            ("Manhã", "Café da manhã no hotel", HOTEL, "hotel"),
            ("Dia", "City Tour Gramado + Canela com a Turistur", "Gramado RS", "transfer"),
            ("Paradas", "Lago Negro, Mini Mundo e atrações do roteiro", "Lago Negro, Gramado RS", "city tour"),
            ("Canela", "Caracol / Bondinhos conforme o pacote", "Bondinhos Aéreos Parques da Serra, Canela RS", "city tour"),
            ("18:30", "Retorno ao hotel e descanso", HOTEL, "transfer"),
            ("20:00", "Jantar leve / escolha livre no centro", "Centro de Gramado RS", "a pé/Uber"),
            ("21:45", "Rua Coberta e centro iluminado", "Rua Coberta, Gramado RS", "a pé"),
        ]
    },
    "Dia 4": {
        "data": "04/09/2026",
        "titulo": "Maria Fumaça + Noite da Pizza",
        "icone": "🚂",
        "resumo": "Passeio clássico da Serra Gaúcha e noite especial de pizza em Gramado.",
        "jantar": "Pizzaria Scur ou Cara de Mau",
        "look": "Maria Fumaça: polo preta ou camiseta básica marrom + calça jeans/escura + Adidas + bomber preta Marfino. À noite para pizza/Cara de Mau: camisa social preta + calça chumbo/preta + suéter + casaco marrom Bluestel ou bomber preta + tênis marrom acamurçado.",
        "itens": [
            ("Manhã", "Café da manhã no hotel", HOTEL, "hotel"),
            ("Dia", "Passeio Maria Fumaça", "Maria Fumaça, Bento Gonçalves RS", "transfer"),
            ("18:30", "Retorno para Gramado / hotel", HOTEL, "transfer"),
            ("19:30", "Banho e descanso", HOTEL, "hotel"),
            ("21:00", "Pizza — Scur ou Cara de Mau", "Centro de Gramado RS", "a pé/Uber"),
            ("Após", "Caminhada leve pelo centro", "Rua Coberta, Gramado RS", "a pé"),
        ]
    },
    "Dia 5": {
        "data": "05/09/2026",
        "titulo": "Nova Petrópolis + Churrasco",
        "icone": "🌲",
        "resumo": "Dia inteiro em Nova Petrópolis e fechamento da noite com churrasco gaúcho.",
        "jantar": "Gramado e Brasa ou similar",
        "look": "Nova Petrópolis: camiseta básica preta + segunda pele se necessário + suéter + calça escura + Nike preto + casaco cáqui. Leve o casaco marrom Bluestel se a previsão indicar frio/vento. À noite: camisa social marrom ou terceira camisa social + calça escura + bomber preta Marfino + tênis marrom acamurçado.",
        "itens": [
            ("Manhã", "Saída para Nova Petrópolis", "Nova Petrópolis RS", "transfer"),
            ("Parada 1", "Praça das Flores", "Praça das Flores, Nova Petrópolis RS", "passeio"),
            ("Parada 2", "Labirinto Verde", "Labirinto Verde, Nova Petrópolis RS", "passeio"),
            ("Parada 3", "Parque Aldeia do Imigrante", "Aldeia do Imigrante, Nova Petrópolis RS", "passeio"),
            ("Almoço", "Almoço econômico em Nova Petrópolis", "Centro, Nova Petrópolis RS", "passeio"),
            ("Tarde", "Parque Pedras do Silêncio", "Parque Pedras do Silêncio, Nova Petrópolis RS", "passeio"),
            ("Fim de tarde", "Ninho das Águias", "Ninho das Águias, Nova Petrópolis RS", "passeio"),
            ("19:00", "Retorno para Gramado", HOTEL, "transfer"),
            ("20:30", "Noite de churrasco gaúcho", "Centro de Gramado RS", "a pé/Uber"),
            ("22:00", "Última grande caminhada pelo centro", "Rua Coberta, Gramado RS", "a pé"),
        ]
    },
    "Dia 6": {
        "data": "06/09/2026",
        "titulo": "Manhã Livre + Aeroporto",
        "icone": "✈️",
        "resumo": "Últimas compras, café tranquilo e retorno.",
        "jantar": "Sem jantar programado",
        "look": "Manhã livre/retorno: segunda polo preta ou camiseta marrom + jeans/calça confortável + Adidas ou Nike preto + moletom preto. Casaco na mão conforme o frio. Bermuda/short apenas se a manhã estiver realmente amena.",
        "itens": [
            ("08:00", "Café da manhã no hotel", HOTEL, "hotel"),
            ("09:00", "Última caminhada pelo centro", "Centro de Gramado RS", "a pé"),
            ("09:30", "Compras de chocolates e lembranças", "Rua Coberta, Gramado RS", "a pé"),
            ("10:30", "Rua Coberta / Igreja São Pedro", "Igreja Matriz São Pedro, Gramado RS", "a pé"),
            ("Depois", "Retorno ao hotel", HOTEL, "a pé"),
            ("Saída", "Transfer para o aeroporto", "Aeroporto Salgado Filho, Porto Alegre RS", "transfer"),
        ]
    },
}

RESTAURANTES = [
    {
        "nome": "Sabor da Nonna",
        "tipo": "Almoço / buffet",
        "icone": "🍛",
        "preco": "≈ R$ 55 por pessoa (confirmar valor na data)",
        "perfil": "Plano A para o almoço de chegada: comida caseira e bom custo-benefício. Como você chega às 14h, vá logo após o check-in.",
        "endereco": "Restaurante Sabor da Nonna, Gramado RS",
        "premium": False,
        "noite": "Dia 2 — almoço"
    },
    {
        "nome": "Empório Benetti",
        "tipo": "Almoço tardio / Plano B",
        "icone": "🍽️",
        "preco": "≈ R$ 40–60 por pessoa (estimativa; confirmar no local)",
        "perfil": "Alternativa para o dia da chegada se o check-in ou transfer atrasar e você perder o horário do buffet.",
        "endereco": "Empório Benetti, Gramado RS",
        "premium": False,
        "noite": "Dia 2 — almoço"
    },
    {
        "nome": "Maison de La Fondue",
        "tipo": "Fondue",
        "icone": "🫕",
        "preco": "≈ R$ 115 por pessoa em oferta consultada (confirmar antes da viagem)",
        "perfil": "Escolha para a primeira noite: sequência de fondue e clima clássico de Gramado.",
        "endereco": "Maison de La Fondue, Gramado RS",
        "premium": False,
        "noite": "Dia 2"
    },
    {
        "nome": "La Grotta Prime",
        "tipo": "Fondue",
        "icone": "🫕",
        "preco": "≈ R$ 70–110 por pessoa em promoções",
        "perfil": "Boa opção para sequência de fondue sem ir para casas mais caras.",
        "endereco": "Gramado RS",
        "premium": False,
        "noite": "Dia 3"
    },
    {
        "nome": "Pizzaria Scur",
        "tipo": "Pizza",
        "icone": "🍕",
        "preco": "≈ R$ 80–120 por pessoa",
        "perfil": "Tradicional, central e mais econômica que pizzarias-show.",
        "endereco": "Rua São Pedro, 660, Centro, Gramado RS",
        "premium": False,
        "noite": "Dia 4"
    },
    {
        "nome": "Cara de Mau",
        "tipo": "Pizza temática",
        "icone": "🏴‍☠️",
        "preco": "≈ R$ 250–300 por pessoa",
        "perfil": "Experiência premium com pizza, personagens e espetáculo.",
        "endereco": "Rua Coronel João Corrêa, 394, Gramado RS",
        "premium": True,
        "noite": "Dia 4"
    },
    {
        "nome": "Gramado e Brasa",
        "tipo": "Churrasco",
        "icone": "🥩",
        "preco": "≈ R$ 90–130 por pessoa em promoções",
        "perfil": "Boa opção de churrasco/rodízio com foco em custo-benefício.",
        "endereco": "Rua Garibaldi, 271, Centro, Gramado RS",
        "premium": False,
        "noite": "Dia 5"
    },
]

MALA = [
    "Documento / CNH / cartões",
    "Reserva do hotel e vouchers dos passeios",
    "Cartão YUO / Elo",
    "Carregador do celular",
    "Power bank",
    "Bomber preta Marfino tipo corta-vento",
    "Casaco marrom Bluestel",
    "Casaco sarja cáqui/oliva",
    "Moletom preto com capuz",
    "2 suéteres",
    "2 polos pretas",
    "2 camisetas básicas: preta e marrom",
    "2 camisas sociais: preta e marrom",
    "Opcional: 1 terceira camisa social para variar os looks",
    "3 a 4 calças (jeans + azul-escura/chumbo/preta)",
    "Bermuda e shorts para hotel/dia ameno",
    "Segunda pele (parte de cima e, se tiver, parte de baixo)",
    "Nike preto",
    "Adidas",
    "Tênis marrom acamurçado",
    "Meias extras",
    "Roupa íntima",
    "Pijama / roupa confortável",
    "Guarda-chuva compacto",
    "Medicamentos e itens de higiene pessoal",
    "Comprar em Gramado se necessário: gorro, cachecol e luvas",
    "Plano para frio forte: considerar alugar/comprar casaco mais pesado somente se a previsão justificar",
]

ECONOMIA = [
    "Pesquisar Laçador de Ofertas antes de fondue, churrasco e atrações.",
    "Pesquisar Prime Gourmet para promoções 2 por 1.",
    "Comparar preço direto com cupom antes de fechar.",
    "Confirmar YUO / Elo Voucher antes de pedir.",
    "Priorizar caminhada no centro para economizar Uber.",
    "No City Tour, comprar ingresso só das atrações realmente desejadas.",
    "Tratar Cara de Mau como experiência premium, não como opção econômica.",
]

# =========================================================
# HELPERS
# =========================================================
def fmt_money(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def maps_walk(dest):
    return (
        "https://www.google.com/maps/dir/?api=1"
        f"&origin={quote_plus(HOTEL)}"
        f"&destination={quote_plus(dest)}"
        "&travelmode=walking"
    )

def maps_drive(dest):
    return (
        "https://www.google.com/maps/dir/?api=1"
        f"&origin={quote_plus(HOTEL)}"
        f"&destination={quote_plus(dest)}"
        "&travelmode=driving"
    )

def maps_place(dest):
    return f"https://www.google.com/maps/search/?api=1&query={quote_plus(dest)}"

def weather_url():
    return "https://www.google.com/search?q=" + quote_plus("previsão do tempo Gramado RS")

def init_state():
    st.session_state.setdefault("saldo_inicial", 1000.0)
    st.session_state.setdefault("gastos", [])
    st.session_state.setdefault("checks", {})
    st.session_state.setdefault("favoritos", [])
    st.session_state.setdefault("mala", {})

def total_yuo():
    return sum(g["valor"] for g in st.session_state.gastos if g.get("yuo"))

def total_geral():
    return sum(g["valor"] for g in st.session_state.gastos)

def saldo():
    return st.session_state.saldo_inicial - total_yuo()

def gasto_dia(dia):
    return sum(g["valor"] for g in st.session_state.gastos if g["dia"] == dia)

def backup_json():
    return json.dumps({
        "saldo_inicial": st.session_state.saldo_inicial,
        "gastos": st.session_state.gastos,
        "checks": st.session_state.checks,
        "favoritos": st.session_state.favoritos,
        "mala": st.session_state.mala,
        "gerado_em": datetime.now(TZ).isoformat()
    }, ensure_ascii=False, indent=2)

def trip_status():
    today = datetime.now(TZ).date()
    if today < TRIP_START:
        return f"Faltam {(TRIP_START - today).days} dias para a viagem"
    if TRIP_START <= today <= TRIP_END:
        return "Você está em viagem 🎉"
    return "Viagem concluída"

def suggested_day():
    today = datetime.now(TZ).date()
    mapping = {
        date(2026,9,2): "Dia 2",
        date(2026,9,3): "Dia 3",
        date(2026,9,4): "Dia 4",
        date(2026,9,5): "Dia 5",
        date(2026,9,6): "Dia 6",
    }
    return mapping.get(today, "Dia 2")

init_state()

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">
    <div class="muted">MEU GUIA DE VIAGEM</div>
    <h1 style="margin:.2rem 0 .3rem 0;">🏔️ Gramado 2026</h1>
    <div>2 a 6 de setembro • Hotel Laghetto Premio</div>
    <div style="margin-top:8px;">
        <span class="badge">🗺️ Roteiro</span>
        <span class="badge">🍽️ Gastronomia</span>
        <span class="badge">💳 YUO</span>
        <span class="badge">🧳 Mala</span>
        <span class="badge">🌦️ Tempo</span>
        <span class="badge">👕 Looks</span>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Saldo YUO", fmt_money(st.session_state.saldo_inicial))
with c2:
    st.metric("Usado no YUO", fmt_money(total_yuo()))
with c3:
    st.metric("Disponível", fmt_money(saldo()))

st.caption("📅 " + trip_status())

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🏔️ Gramado 2026")
dia = st.sidebar.radio("Dia da viagem", list(ROTEIRO.keys()), index=list(ROTEIRO.keys()).index(suggested_day()))

st.sidebar.divider()
st.sidebar.markdown("**🏨 Hotel**")
st.sidebar.write(HOTEL_NAME)
st.sidebar.caption(HOTEL_ADDRESS)
st.sidebar.link_button("📍 Abrir hotel no Maps", maps_place(HOTEL), use_container_width=True)
st.sidebar.link_button("🌦️ Ver previsão do tempo", weather_url(), use_container_width=True)

st.sidebar.divider()
st.sidebar.markdown("**💳 Cartão alimentação**")
st.session_state.saldo_inicial = st.sidebar.number_input(
    "Saldo inicial YUO",
    min_value=0.0,
    value=float(st.session_state.saldo_inicial),
    step=50.0
)

st.sidebar.download_button(
    "⬇️ Backup da viagem",
    data=backup_json(),
    file_name="gramado_2026_backup.json",
    mime="application/json",
    use_container_width=True
)

upload = st.sidebar.file_uploader("Restaurar backup", type=["json"])
if upload:
    try:
        data = json.load(upload)
        st.session_state.saldo_inicial = float(data.get("saldo_inicial", 1000))
        st.session_state.gastos = data.get("gastos", [])
        st.session_state.checks = data.get("checks", {})
        st.session_state.favoritos = data.get("favoritos", [])
        st.session_state.mala = data.get("mala", {})
        st.sidebar.success("Backup restaurado.")
    except Exception:
        st.sidebar.error("Backup inválido.")

# =========================================================
# TABS
# =========================================================
tabs = st.tabs([
    "🏠 Hoje", "🗺️ Roteiro", "🍽️ Comer", "💳 Gastos",
    "🧳 Mala", "🌦️ Tempo", "💡 Economia", "👕 Look"
])

with tabs[0]:
    info = ROTEIRO[dia]
    st.subheader(f"{info['icone']} {dia} — {info['titulo']}")
    st.caption(info["data"])
    st.write(info["resumo"])

    feitos = sum(
        1 for i in range(len(info["itens"]))
        if st.session_state.checks.get(f"{dia}_{i}", False)
    )
    total = len(info["itens"])
    st.progress(feitos / max(total, 1))
    st.caption(f"{feitos}/{total} atividades concluídas")

    prox = None
    for i, item in enumerate(info["itens"]):
        if not st.session_state.checks.get(f"{dia}_{i}", False):
            prox = item
            break

    if prox:
        st.markdown(
            f"""
            <div class="card">
                <div class="muted">O QUE FAZER AGORA</div>
                <h4>{prox[0]} — {prox[1]}</h4>
                <div class="muted">Deslocamento sugerido: {prox[3]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        a,b = st.columns(2)
        with a:
            st.link_button("🚶 Como ir", maps_walk(prox[2]), use_container_width=True)
        with b:
            st.link_button("📍 Maps", maps_place(prox[2]), use_container_width=True)

    st.markdown("### 🍽️ Noite")
    st.info(info["jantar"])

    st.markdown("### 💳 Orçamento")
    media_diaria = st.session_state.saldo_inicial / 5 if st.session_state.saldo_inicial > 0 else 0
    usado = gasto_dia(dia)
    a,b = st.columns(2)
    with a:
        st.metric("Média diária", fmt_money(media_diaria))
    with b:
        st.metric("Gasto do dia", fmt_money(usado))
    if usado > media_diaria and media_diaria > 0:
        st.warning("Gasto acima da média diária sugerida.")
    elif usado > 0:
        st.success("Gasto dentro da média diária.")

    st.markdown("### 👕 Look")
    st.info(info["look"])

with tabs[1]:
    info = ROTEIRO[dia]
    st.subheader(f"{info['icone']} {dia} — {info['titulo']}")

    for i, (hora, atividade, destino, deslocamento) in enumerate(info["itens"]):
        key = f"{dia}_{i}"
        current = st.session_state.checks.get(key, False)

        st.markdown(
            f"""
            <div class="card">
                <div class="muted">{hora} • {deslocamento}</div>
                <h4>{atividade}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1,c2,c3 = st.columns(3)
        with c1:
            checked = st.checkbox("Feito", value=current, key=f"check_{key}")
            st.session_state.checks[key] = checked
        with c2:
            st.link_button("🚶 Rota", maps_walk(destino), use_container_width=True)
        with c3:
            st.link_button("📍 Maps", maps_place(destino), use_container_width=True)

with tabs[2]:
    st.subheader("🍽️ Gastronomia")
    filtro = st.segmented_control(
        "Filtrar",
        ["Todos", "Fondue", "Pizza", "Pizza temática", "Churrasco"],
        default="Todos"
    )

    for r in RESTAURANTES:
        if filtro != "Todos" and r["tipo"] != filtro:
            continue

        premium = "⭐ Experiência premium" if r["premium"] else "💚 Custo-benefício"
        st.markdown(
            f"""
            <div class="card">
                <div class="muted">{premium} • sugerido para {r['noite']}</div>
                <h4>{r['icone']} {r['nome']}</h4>
                <div>{r['perfil']}</div>
                <div style="margin-top:8px;"><b>{r['preco']}</b></div>
                <div class="muted" style="margin-top:6px;">Confirmar YUO / Elo Voucher antes de ir.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        a,b,c = st.columns(3)
        with a:
            st.link_button("🚶 A pé", maps_walk(r["endereco"]), use_container_width=True)
        with b:
            st.link_button("🚗 Uber", maps_drive(r["endereco"]), use_container_width=True)
        with c:
            fav = r["nome"] in st.session_state.favoritos
            if st.button("★ Favorito" if not fav else "✓ Favorito", key=f"fav_{r['nome']}", use_container_width=True):
                if fav:
                    st.session_state.favoritos.remove(r["nome"])
                else:
                    st.session_state.favoritos.append(r["nome"])
                st.rerun()

with tabs[3]:
    st.subheader("💳 Controle de gastos")
    with st.form("gasto_form", clear_on_submit=True):
        c1,c2 = st.columns(2)
        with c1:
            desc = st.text_input("Descrição", placeholder="Ex.: Fondue")
        with c2:
            valor = st.number_input("Valor", min_value=0.0, step=5.0)

        gdia = st.selectbox("Dia", list(ROTEIRO.keys()))
        yuo = st.checkbox("Pago com YUO", value=True)
        ok = st.form_submit_button("Adicionar gasto", use_container_width=True)

        if ok and desc and valor > 0:
            st.session_state.gastos.append({
                "descricao": desc,
                "valor": float(valor),
                "dia": gdia,
                "yuo": yuo,
            })
            st.success("Gasto registrado.")

    if st.session_state.gastos:
        for idx, g in enumerate(st.session_state.gastos):
            st.markdown(
                f"""
                <div class="card">
                    <b>{g['dia']} — {g['descricao']}</b><br>
                    {fmt_money(g['valor'])}
                    <div class="muted">{'YUO' if g.get('yuo') else 'Outro pagamento'}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("🗑️ Excluir", key=f"del_{idx}"):
                st.session_state.gastos.pop(idx)
                st.rerun()
    else:
        st.info("Nenhum gasto lançado.")

    st.divider()
    x1,x2,x3 = st.columns(3)
    with x1:
        st.metric("Total geral", fmt_money(total_geral()))
    with x2:
        st.metric("No YUO", fmt_money(total_yuo()))
    with x3:
        st.metric("Saldo YUO", fmt_money(saldo()))

with tabs[4]:
    st.subheader("🧳 Checklist da mala")
    feitos_mala = 0
    for idx, item in enumerate(MALA):
        key = f"mala_{idx}"
        current = st.session_state.mala.get(key, False)
        checked = st.checkbox(item, value=current, key=f"mala_ui_{idx}")
        st.session_state.mala[key] = checked
        if checked:
            feitos_mala += 1

    st.progress(feitos_mala / len(MALA))
    st.caption(f"{feitos_mala}/{len(MALA)} itens preparados")

with tabs[5]:
    st.subheader("🌦️ Tempo em Gramado")
    st.write("Use a previsão para decidir as camadas antes de sair do hotel.")
    st.link_button("🌦️ Abrir previsão atual", weather_url(), use_container_width=True)
    st.markdown("### Guia rápido")
    st.write("**18–21 °C:** polo/camisa/camiseta")
    st.write("**15–18 °C:** + casaco")
    st.write("**11–15 °C:** + suéter")
    st.write("**Frio com vento:** segunda pele + suéter + casaco")
    st.info("No início de setembro, leve camadas: a temperatura pode variar bastante entre manhã, tarde e noite.")

with tabs[6]:
    st.subheader("💡 Economia")
    for item in ECONOMIA:
        st.checkbox(item, key=f"eco_{hash(item)}")
    st.warning("Preços e promoções no app são estimativas. Confirme perto da viagem.")

with tabs[7]:
    st.subheader("👕 Look do dia")
    st.markdown(
        f"""
        <div class="card">
            <div class="muted">{ROTEIRO[dia]['data']}</div>
            <h4>{dia}</h4>
            {ROTEIRO[dia]['look']}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("### 🧥 Estratégia da mala")
    st.write("**Casacos:** bomber preta Marfino + marrom Bluestel + cáqui + moletom preto.")
    st.write("**Camadas:** 2 suéteres + segunda pele. Isso permite adaptar sem levar casaco pesado demais.")
    st.write("**Calçados:** Nike preto para caminhar, Adidas como alternativo e marrom acamurçado para looks mais arrumados.")
    st.write("**Social:** camisa preta + marrom; uma terceira é opcional, não obrigatória.")
    st.write("**Frio excepcional:** gorro, cachecol e luvas podem ser comprados em Gramado; casaco pesado só se a previsão próxima da viagem indicar necessidade.")

st.divider()
st.caption("Gramado 2026 • versão final do guia pessoal • preços, horários e condições sujeitos a alteração.")
