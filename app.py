import json
from datetime import date, datetime
from urllib.parse import quote_plus

import streamlit as st

from data import (
    HOTEL, ITINERARY, LOOKS, MARKETS, PACKING, PRACTICAL_TIPS, RESTAURANTS,
    TRIP_END, TRIP_START, YUO_INITIAL_BALANCE,
)

st.set_page_config(page_title="Gramado 2026", page_icon="🏔️", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.block-container{max-width:760px;padding:1rem 1rem 5rem}.hero{padding:1.15rem;border-radius:20px;background:linear-gradient(135deg,#173f35,#2c6b57);color:white;margin-bottom:1rem}.hero h1{margin:0;font-size:1.8rem}.hero p{margin:.35rem 0 0;opacity:.9}.card{padding:1rem;border:1px solid rgba(128,128,128,.22);border-radius:16px;margin:.55rem 0}.eyebrow{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;opacity:.72}.stButton a{width:100%}div[data-testid="stMetric"]{border:1px solid rgba(128,128,128,.18);padding:.7rem;border-radius:14px}@media(max-width:640px){.block-container{padding-top:.65rem}.hero h1{font-size:1.55rem}button[data-baseweb="tab"]{padding-left:.55rem;padding-right:.55rem}}
</style>
""", unsafe_allow_html=True)


def money(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def maps_url(destination, mode="walking"):
    return "https://www.google.com/maps/dir/?api=1&origin={}&destination={}&travelmode={}".format(
        quote_plus(HOTEL["address"]), quote_plus(destination), mode
    )


def init_state():
    st.session_state.setdefault("expenses", [])
    st.session_state.setdefault("favorites", [])


def backup_payload():
    checks = {k: v for k, v in st.session_state.items() if k.startswith(("route_", "bag_"))}
    return json.dumps({"version": 1, "expenses": st.session_state.expenses, "favorites": st.session_state.favorites, "checks": checks}, ensure_ascii=False, indent=2)


def restore(upload):
    try:
        payload = json.load(upload)
        st.session_state.expenses = payload.get("expenses", [])
        st.session_state.favorites = payload.get("favorites", [])
        for key, value in payload.get("checks", {}).items():
            st.session_state[key] = bool(value)
        st.success("Backup restaurado.")
    except (ValueError, TypeError, AttributeError):
        st.error("Arquivo de backup inválido.")


init_state()
today = date.today()
if today < TRIP_START:
    status = f"Faltam {(TRIP_START - today).days} dias"
elif today <= TRIP_END:
    status = f"Dia {(today - TRIP_START).days + 1} de 5"
else:
    status = "Viagem concluída"

st.markdown(f'<div class="hero"><div class="eyebrow">Seu guia pessoal</div><h1>🏔️ Gramado 2026</h1><p>02 a 06 de setembro · {HOTEL["name"]}</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Minha viagem")
    selected_day = st.selectbox("Dia", list(ITINERARY), index=max(0, min(4, (today - TRIP_START).days)))
    st.caption(f"🏨 {HOTEL['name']} · check-in {HOTEL['check_in']}")
    st.link_button("📍 Abrir hotel no Maps", maps_url(HOTEL["address"]))
    st.divider()
    st.download_button("⬇️ Baixar backup", backup_payload(), "gramado-2026-backup.json", "application/json", use_container_width=True)
    upload = st.file_uploader("Restaurar backup", type="json")
    if upload and st.button("Restaurar agora", use_container_width=True):
        restore(upload)
        st.rerun()

expenses_total = sum(float(item["amount"]) for item in st.session_state.expenses)
you_total = sum(float(item["amount"]) for item in st.session_state.expenses if item["payment"] == "YUO")
col1, col2, col3 = st.columns(3)
col1.metric("Viagem", status)
col2.metric("YUO disponível", money(YUO_INITIAL_BALANCE - you_total))
col3.metric("Registrado", money(expenses_total))

tabs = st.tabs(["🗓️ Roteiro", "🍽️ Comer", "💳 Gastos", "🧳 Mala", "💡 Dicas"])

with tabs[0]:
    day = ITINERARY[selected_day]
    st.subheader(selected_day)
    st.write(day["summary"])
    st.info(day["tip"])
    all_items = [(section, item) for section, items in day["sections"].items() for item in items]
    completed = sum(st.session_state.get(f"route_{selected_day}_{section}_{i}", False) for i, (section, _) in enumerate(all_items))
    st.progress(completed / len(all_items), text=f"{completed} de {len(all_items)} etapas concluídas")
    for section, items in day["sections"].items():
        st.markdown(f"### {section}")
        for hour, activity, place in items:
            item_index = all_items.index((section, (hour, activity, place)))
            st.markdown(f'<div class="card"><div class="eyebrow">{hour}</div><strong>{activity}</strong></div>', unsafe_allow_html=True)
            c1, c2 = st.columns([1.25, 1])
            c1.checkbox("Concluído", key=f"route_{selected_day}_{section}_{item_index}")
            c2.link_button("Como chegar", maps_url(place), use_container_width=True)
    look_key = selected_day[:5]
    st.markdown("#### Look sugerido")
    st.write(LOOKS[look_key])

with tabs[1]:
    st.subheader("Restaurantes")
    category = st.selectbox("Filtrar", ["Todos"] + sorted({x[1] for x in RESTAURANTS}))
    for name, kind, level, note in RESTAURANTS:
        if category != "Todos" and kind != category:
            continue
        st.markdown(f'<div class="card"><div class="eyebrow">{kind} · {level}</div><strong>{name}</strong><br>{note}</div>', unsafe_allow_html=True)
        st.link_button(f"Abrir {name} no Maps", maps_url(f"{name}, Gramado RS"), use_container_width=True)
    st.subheader("🛒 Mercados para economizar")
    for name, address, note in MARKETS:
        with st.expander(name):
            st.write(f"{note} · {address}")
            st.link_button("Abrir no Maps", maps_url(f"{name}, {address}"), use_container_width=True)
    st.caption("Preços, horários, aceitação do YUO e disponibilidade podem mudar. Confirme antes de sair ou reservar.")

with tabs[2]:
    st.subheader("Controle do YUO e gastos")
    with st.form("expense_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        expense_date = c1.date_input("Data", min_value=TRIP_START, max_value=TRIP_END, value=min(max(today, TRIP_START), TRIP_END))
        amount = c2.number_input("Valor (R$)", min_value=0.0, step=5.0)
        description = st.text_input("Descrição", placeholder="Ex.: jantar, Uber, ingresso")
        payment = st.selectbox("Pagamento", ["YUO", "Outro"])
        if st.form_submit_button("Adicionar gasto", use_container_width=True) and amount > 0 and description.strip():
            st.session_state.expenses.append({"id": datetime.now().isoformat(), "date": expense_date.isoformat(), "description": description.strip(), "amount": amount, "payment": payment})
            st.rerun()
    st.metric("Saldo real do YUO", money(YUO_INITIAL_BALANCE - you_total))
    for item in reversed(st.session_state.expenses):
        c1, c2 = st.columns([4, 1])
        c1.write(f"**{item['description']}** · {item['date']} · {item['payment']} · {money(item['amount'])}")
        if c2.button("Excluir", key=f"delete_{item['id']}"):
            st.session_state.expenses = [x for x in st.session_state.expenses if x["id"] != item["id"]]
            st.rerun()
    if not st.session_state.expenses:
        st.caption("Nenhum gasto registrado ainda.")

with tabs[3]:
    st.subheader("Mala real")
    for group, items in PACKING.items():
        with st.expander(group, expanded=group == "Agasalhos"):
            for i, item in enumerate(items):
                st.checkbox(item, key=f"bag_{group}_{i}")
    st.subheader("Looks por dia")
    for day_key, look in LOOKS.items():
        st.markdown(f"**{day_key}** — {look}")

with tabs[4]:
    st.subheader("Clima e orientação prática")
    st.link_button("🌦️ Ver previsão de Gramado", "https://www.google.com/search?q=previs%C3%A3o+do+tempo+Gramado+RS", use_container_width=True)
    for tip in PRACTICAL_TIPS:
        st.markdown(f"- {tip}")
    st.subheader("Economia")
    st.write("Consulte Laçador de Ofertas e Prime Gourmet, mas confira validade, dias permitidos, reserva e preço final. Priorize o mercado para água e lanches e deixe o YUO para refeições que valham a experiência.")

st.divider()
st.caption("Gramado 2026 · Base consolidada para uso pessoal · Faça backup ao fim de cada dia")
