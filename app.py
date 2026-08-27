
import streamlit as st
from urllib.parse import quote_plus
from datetime import datetime
import json

st.set_page_config(
    page_title="Gramado 2026 — Premium",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =========================
# TEMA / CSS
# =========================
st.markdown("""
<style>
:root {
    --radius: 20px;
}
.block-container {
    padding-top: 0.8rem;
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
.muted { opacity: .74; font-size: .92rem; }
.badge {
    display: inline-block;
    padding: 4px 9px;
    border-radius: 999px;
    border: 1px solid rgba(128,128,128,.25);
    margin-right: 5px;
    margin-bottom: 5px;
    font-size: .82rem;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(128,128,128,.18);
    border-radius: 16px;
    padding: 10px;
}
[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,.14);
}
.stButton>button, .stLinkButton>a {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

HOTEL = "Hotel Laghetto Premio, Gramado, RS"

ROTEIRO = {
    "Dia 2": {
        "titulo": "Chegada + Centro de Gramado",
        "icone": "✨",
        "resumo": "Primeiro contato com Gramado, caminhando pelo centro sem pressa.",
        "itens": [
            ("14:00", "Check-in no Hotel Laghetto Premio", HOTEL),
            ("15:30", "Lago Joaquina Rita Bier", "Lago Joaquina Rita Bier, Gramado RS"),
            ("16:10", "Rótula das Bandeiras", "Rótula das Bandeiras, Gramado RS"),
            ("16:30", "Rua Torta", "Rua Torta, Gramado RS"),
            ("17:00", "Praça das Etnias / Casa do Colono", "Praça das Etnias, Gramado RS"),
            ("17:40", "Igreja Matriz São Pedro", "Igreja Matriz São Pedro, Gramado RS"),
            ("18:00", "Fonte do Amor Eterno", "Fonte do Amor Eterno, Gramado RS"),
            ("18:20", "Palácio dos Festivais", "Palácio dos Festivais, Gramado RS"),
            ("18:40", "Rua Coberta", "Rua Coberta, Gramado RS"),
            ("19:30", "Jantar econômico no centro", "Centro de Gramado RS"),
            ("21:00", "Passeio noturno pela Borges de Medeiros", "Avenida Borges de Medeiros, Gramado RS"),
            ("21:30", "Chocolate quente / sobremesa", "Rua Coberta, Gramado RS"),
        ],
    },
    "Dia 3": {
        "titulo": "City Tour Gramado + Canela",
        "icone": "🚌",
        "resumo": "Dia de conhecer as principais atrações com logística pronta.",
        "itens": [
            ("Manhã", "Café da manhã no hotel", HOTEL),
            ("Dia", "City Tour Gramado + Canela com a Turistur", "Gramado RS"),
            ("Paradas", "Lago Negro, Mini Mundo e atrações do roteiro", "Lago Negro, Gramado RS"),
            ("Canela", "Caracol / Bondinhos conforme o pacote", "Bondinhos Aéreos Parques da Serra, Canela RS"),
            ("18:30", "Retorno ao hotel e descanso", HOTEL),
            ("20:00", "Noite do fondue", "Centro de Gramado RS"),
            ("21:45", "Rua Coberta e centro iluminado", "Rua Coberta, Gramado RS"),
        ],
    },
    "Dia 4": {
        "titulo": "Maria Fumaça + Noite da Pizza",
        "icone": "🚂",
        "resumo": "Passeio clássico da Serra Gaúcha e noite especial de pizza.",
        "itens": [
            ("Manhã", "Café da manhã no hotel", HOTEL),
            ("Dia", "Passeio Maria Fumaça", "Maria Fumaça, Bento Gonçalves RS"),
            ("18:30", "Retorno para Gramado / hotel", HOTEL),
            ("19:30", "Banho e descanso", HOTEL),
            ("21:00", "Pizza: Scur ou experiência Cara de Mau", "Centro de Gramado RS"),
            ("Após", "Caminhada leve pelo centro", "Rua Coberta, Gramado RS"),
        ],
    },
    "Dia 5": {
        "titulo": "Nova Petrópolis + Churrasco",
        "icone": "🌲",
        "resumo": "Dia inteiro em Nova Petrópolis e fechamento com churrasco gaúcho.",
        "itens": [
            ("Manhã", "Saída para Nova Petrópolis", "Nova Petrópolis RS"),
            ("Parada 1", "Praça das Flores", "Praça das Flores, Nova Petrópolis RS"),
            ("Parada 2", "Labirinto Verde", "Labirinto Verde, Nova Petrópolis RS"),
            ("Parada 3", "Parque Aldeia do Imigrante", "Aldeia do Imigrante, Nova Petrópolis RS"),
            ("Almoço", "Almoço econômico em Nova Petrópolis", "Centro, Nova Petrópolis RS"),
            ("Tarde", "Parque Pedras do Silêncio", "Parque Pedras do Silêncio, Nova Petrópolis RS"),
            ("Fim de tarde", "Ninho das Águias", "Ninho das Águias, Nova Petrópolis RS"),
            ("19:00", "Retorno para Gramado", HOTEL),
            ("20:30", "Noite de churrasco gaúcho", "Centro de Gramado RS"),
            ("22:00", "Última grande caminhada pelo centro", "Rua Coberta, Gramado RS"),
        ],
    },
    "Dia 6": {
        "titulo": "Manhã Livre + Aeroporto",
        "icone": "✈️",
        "resumo": "Últimas compras, passeio leve e retorno.",
        "itens": [
            ("08:00", "Café da manhã no hotel", HOTEL),
            ("09:00", "Última caminhada pelo centro", "Centro de Gramado RS"),
            ("09:30", "Compras de chocolates e lembranças", "Rua Coberta, Gramado RS"),
            ("10:30", "Rua Coberta / Igreja São Pedro", "Igreja Matriz São Pedro, Gramado RS"),
            ("Depois", "Retorno ao hotel", HOTEL),
            ("Saída", "Transfer para o aeroporto", "Aeroporto Salgado Filho, Porto Alegre RS"),
        ],
    },
}

RESTAURANTES = [
    {
        "nome": "La Grotta Prime",
        "tipo": "Fondue",
        "icone": "🫕",
        "preco": "≈ R$ 70–110 por pessoa em promoções",
        "perfil": "Custo-benefício para sequência de fondue.",
        "endereco": "Gramado RS",
        "premium": False,
    },
    {
        "nome": "Pizzaria Scur",
        "tipo": "Pizza",
        "icone": "🍕",
        "preco": "≈ R$ 80–120 por pessoa",
        "perfil": "Tradicional, central e mais econômica que pizzarias-show.",
        "endereco": "Rua São Pedro, 660, Centro, Gramado RS",
        "premium": False,
    },
    {
        "nome": "Cara de Mau",
        "tipo": "Pizza temática",
        "icone": "🏴‍☠️",
        "preco": "≈ R$ 250–300 por pessoa",
        "perfil": "Experiência premium com pizza, personagens e espetáculo.",
        "endereco": "Rua Coronel João Corrêa, 394, Gramado RS",
        "premium": True,
    },
    {
        "nome": "Gramado e Brasa",
        "tipo": "Churrasco",
        "icone": "🥩",
        "preco": "≈ R$ 90–130 por pessoa em promoções",
        "perfil": "Boa opção de churrasco/rodízio com foco em custo-benefício.",
        "endereco": "Rua Garibaldi, 271, Centro, Gramado RS",
        "premium": False,
    },
]

LOOKS = {
    "Dia 2": "Polo preta + jeans slim lavado + Nike preto. Moletom preto na mão. À noite, bomber preta se esfriar.",
    "Dia 3": "Oxford azul-clara + calça azul-escura + casaco sarja cáqui/oliva + Nike preto.",
    "Dia 4": "Camisa salmão ou suéter bege + calça cinza/chumbo + bomber preta + tênis marrom/camurçado.",
    "Dia 5": "Camiseta preta + suéter preto/bege + calça escura + Nike preto. Segunda pele se amanhecer frio.",
    "Dia 6": "Polo/camiseta básica + jeans + Nike preto + moletom preto conforme a temperatura.",
}

def fmt_money(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def maps_walk(dest):
    return (
        "https://www.google.com/maps/dir/?api=1"
        f"&origin={quote_plus(HOTEL)}"
        f"&destination={quote_plus(dest)}"
        "&travelmode=walking"
    )

def maps_place(dest):
    return f"https://www.google.com/maps/search/?api=1&query={quote_plus(dest)}"

def init_state():
    st.session_state.setdefault("saldo_inicial", 1000.0)
    st.session_state.setdefault("gastos", [])
    st.session_state.setdefault("checks", {})
    st.session_state.setdefault("favoritos", [])

def total_yuo():
    return sum(g["valor"] for g in st.session_state.gastos if g.get("yuo"))

def total_geral():
    return sum(g["valor"] for g in st.session_state.gastos)

def saldo():
    return st.session_state.saldo_inicial - total_yuo()

def backup_json():
    return json.dumps({
        "saldo_inicial": st.session_state.saldo_inicial,
        "gastos": st.session_state.gastos,
        "checks": st.session_state.checks,
        "favoritos": st.session_state.favoritos,
        "gerado_em": datetime.now().isoformat()
    }, ensure_ascii=False, indent=2)

init_state()

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <div class="muted">MINHA VIAGEM</div>
    <h1 style="margin:.2rem 0 .3rem 0;">🏔️ Gramado 2026</h1>
    <div>2 a 6 de setembro • Hotel Laghetto Premio</div>
    <div style="margin-top:8px;">
        <span class="badge">🗺️ Roteiro</span>
        <span class="badge">🍽️ Gastronomia</span>
        <span class="badge">💳 YUO</span>
        <span class="badge">👕 Looks</span>
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Saldo YUO", fmt_money(st.session_state.saldo_inicial))
with m2:
    st.metric("Usado no YUO", fmt_money(total_yuo()))
with m3:
    st.metric("Disponível", fmt_money(saldo()))

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🏔️ Gramado 2026")
dia = st.sidebar.radio("Dia da viagem", list(ROTEIRO.keys()))

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
        st.sidebar.success("Backup restaurado.")
    except Exception:
        st.sidebar.error("Backup inválido.")

# =========================
# TABS
# =========================
tabs = st.tabs(["🏠 Hoje", "🗺️ Roteiro", "🍽️ Comer", "💳 Gastos", "💡 Economia", "👕 Look"])

with tabs[0]:
    info = ROTEIRO[dia]
    st.subheader(f"{info['icone']} {dia} — {info['titulo']}")
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
                <div class="muted">PRÓXIMA ATIVIDADE</div>
                <h4>{prox[0]} — {prox[1]}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.link_button("📍 Abrir no Maps", maps_place(prox[2]), use_container_width=True)

    st.markdown("### 💳 Situação do orçamento")
    st.write(f"Você ainda tem **{fmt_money(saldo())}** disponíveis no YUO.")

    st.markdown("### 👕 Look sugerido")
    st.info(LOOKS[dia])

with tabs[1]:
    info = ROTEIRO[dia]
    st.subheader(f"{info['icone']} {dia} — {info['titulo']}")

    for i, (hora, atividade, destino) in enumerate(info["itens"]):
        key = f"{dia}_{i}"
        current = st.session_state.checks.get(key, False)

        st.markdown(
            f"""
            <div class="card">
                <div class="muted">{hora}</div>
                <h4>{atividade}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns([1,1,1])
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
                <div class="muted">{premium}</div>
                <h4>{r['icone']} {r['nome']}</h4>
                <div>{r['perfil']}</div>
                <div style="margin-top:8px;"><b>{r['preco']}</b></div>
                <div class="muted" style="margin-top:6px;">Confirmar YUO/Elo Voucher antes de ir.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        a,b,c = st.columns([1,1,1])
        with a:
            st.link_button("🚶 Rota", maps_walk(r["endereco"]), use_container_width=True)
        with b:
            st.link_button("📍 Maps", maps_place(r["nome"] + ", Gramado RS"), use_container_width=True)
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
        st.markdown("### Lançamentos")
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
    st.subheader("💡 Economia")
    st.markdown("""
**Aplicativos úteis**
- **Laçador de Ofertas** — procure fondue, churrasco, restaurantes e atrações.
- **Prime Gourmet** — pode compensar bastante para duas pessoas em ofertas de 2 por 1.
- **Google Maps** — compare avaliação recente, distância e horário antes de sair.

**Estratégia prática**
- Use o centro de Gramado a pé sempre que der.
- No City Tour, escolha as atrações pagas que realmente interessam.
- Compare preço direto do restaurante com cupom antes de fechar.
- Trate a **Cara de Mau** como gasto de experiência premium.
- Confirme diretamente se o estabelecimento aceita **YUO / Elo Voucher**, porque aceitar Elo comum não garante saldo alimentação.
""")
    st.warning("Os valores do app são estimativas para planejamento e podem mudar.")

with tabs[5]:
    st.subheader("👕 Look do dia")
    st.markdown(f"""
    <div class="card">
        <h4>{dia}</h4>
        {LOOKS[dia]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌡️ Camadas para 11–21 °C")
    st.write("**18–21 °C:** polo/camisa/camiseta")
    st.write("**15–18 °C:** + casaco")
    st.write("**11–15 °C:** + suéter")
    st.write("**Perto de 11 °C com vento:** segunda pele + suéter + casaco")

st.divider()
st.caption("Gramado 2026 • Guia pessoal de viagem • preços e condições sujeitos a alteração.")
