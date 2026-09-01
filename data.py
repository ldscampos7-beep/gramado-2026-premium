"""Conteúdo central do Gramado 2026.

Edite este arquivo para alterar roteiro, lugares, mala, looks e dicas sem tocar
na interface do Streamlit.
"""

from datetime import date

TRIP_START = date(2026, 9, 2)
TRIP_END = date(2026, 9, 6)
YUO_INITIAL_BALANCE = 1000.0

HOTEL = {
    "name": "Hotel Laghetto Premio",
    "address": "Av. Borges de Medeiros, 1533, Planalto, Gramado - RS",
    "check_in": "14h",
}

ITINERARY = {
    "02/09 · Chegada + Centro": {
        "date": date(2026, 9, 2),
        "summary": "Chegada tranquila, primeiro contato com Gramado e fondue à noite.",
        "tip": "O Sabor da Nonna fecha cedo: se houver atraso, use o Plano B.",
        "items": [
            ("14h", "Check-in no Laghetto Premio", HOTEL["address"]),
            ("14h30", "Almoço · Sabor da Nonna (Plano A)", "Restaurante Sabor da Nonna Gramado"),
            ("Se atrasar", "Almoço · Empório Benetti (Plano B)", "Empório Benetti Gramado"),
            ("15h30", "Descanso e organização no hotel", HOTEL["address"]),
            ("17h", "Centro: Rua Coberta e Praça Major Nicoletti", "Rua Coberta Gramado"),
            ("17h30", "Igreja São Pedro e Fonte do Amor Eterno", "Igreja Matriz São Pedro Gramado"),
            ("18h", "Chocolate, café e caminhada pela Borges", "Avenida Borges de Medeiros Gramado"),
            ("20h", "Jantar · Maison de La Fondue", "Maison de La Fondue Gramado"),
            ("22h", "Caminhada noturna e retorno ao hotel", HOTEL["address"]),
        ],
    },
    "03/09 · City Tour Gramado + Canela": {
        "date": date(2026, 9, 3),
        "summary": "Dia completo com a Turistur; escolha apenas as atrações pagas prioritárias.",
        "tip": "Confirme no voucher quais ingressos estão incluídos e leve água e corta-vento.",
        "items": [
            ("Manhã", "Café da manhã e saída para o City Tour", HOTEL["address"]),
            ("Dia", "City Tour Gramado + Canela · Turistur", "Gramado Canela RS"),
            ("Paradas", "Lago Negro, Mini Mundo e atrações do pacote", "Lago Negro Gramado"),
            ("Canela", "Região do Caracol e demais paradas", "Parque do Caracol Canela"),
            ("18h30", "Retorno ao hotel e descanso", HOTEL["address"]),
            ("20h", "Jantar flexível · Versoi, Campo & Vinho ou Sopas da Serra", "Centro Gramado"),
            ("21h45", "Rua Coberta e centro iluminado", "Rua Coberta Gramado"),
        ],
    },
    "04/09 · Maria Fumaça + Cara de Mau": {
        "date": date(2026, 9, 4),
        "summary": "Passeio longo na Serra Gaúcha e experiência temática opcional à noite.",
        "tip": "Cara de Mau é a opção premium; Scur ou Burger do Geraldo reduzem o gasto.",
        "items": [
            ("Manhã", "Café da manhã e saída para a Maria Fumaça", HOTEL["address"]),
            ("Dia", "Passeio Maria Fumaça", "Maria Fumaça Bento Gonçalves"),
            ("18h30", "Retorno a Gramado e descanso", HOTEL["address"]),
            ("21h", "Saída para Cara de Mau (opção experiência)", "Cara de Mau Gramado"),
            ("Alternativa", "Pizzaria Scur ou Burger do Geraldo", "Pizzaria Scur Gramado"),
            ("Após jantar", "Retorno ao hotel", HOTEL["address"]),
        ],
    },
    "05/09 · Nova Petrópolis + Noite especial": {
        "date": date(2026, 9, 5),
        "summary": "Cultura germânica, parques e paisagens; última noite completa em Gramado.",
        "tip": "Dia longo: tênis confortável, camadas e bateria externa.",
        "items": [
            ("Manhã", "Saída para Nova Petrópolis", "Nova Petrópolis RS"),
            ("Parada 1", "Praça das Flores e Labirinto Verde", "Labirinto Verde Nova Petrópolis"),
            ("Parada 2", "Parque Aldeia do Imigrante", "Parque Aldeia do Imigrante"),
            ("Almoço", "Restaurante econômico conforme a excursão", "Centro Nova Petrópolis"),
            ("Tarde", "Parque Pedras do Silêncio", "Parque Pedras do Silêncio"),
            ("Fim de tarde", "Ninho das Águias, se o clima permitir", "Ninho das Águias Nova Petrópolis"),
            ("19h", "Retorno a Gramado e banho", HOTEL["address"]),
            ("20h30", "Jantar · Churrascaria Gramadense ou Galeto Itália", "Centro Gramado"),
            ("22h", "Última caminhada pelo centro", "Rua Coberta Gramado"),
        ],
    },
    "06/09 · Manhã livre + Aeroporto": {
        "date": date(2026, 9, 6),
        "summary": "Manhã sem compromisso rígido para compras e despedida.",
        "tip": "Confirme o transfer na véspera e volte ao hotel com boa margem.",
        "items": [
            ("8h", "Café da manhã e fechamento das malas", HOTEL["address"]),
            ("9h", "Última caminhada pelo centro", "Rua Coberta Gramado"),
            ("9h30", "Chocolates e lembranças", "Centro Gramado"),
            ("10h30", "Igreja São Pedro e Rua Coberta", "Igreja Matriz São Pedro Gramado"),
            ("Depois", "Retorno ao hotel e transfer", HOTEL["address"]),
            ("Saída", "Aeroporto conforme o voucher", "Aeroporto Internacional Salgado Filho"),
        ],
    },
}

RESTAURANTS = [
    ("Maison de La Fondue", "Fondue", "Especial", "Centro · jantar do dia 2"),
    ("Cara de Mau", "Pizza temática", "Premium", "Experiência; reservar e conferir sessão"),
    ("Pizzaria Scur", "Pizza", "Intermediário", "Alternativa mais racional à temática"),
    ("Sabor da Nonna / Campo & Vinho", "Buffet caseiro", "Econômico", "Boa escolha de almoço"),
    ("Empório Benetti", "Refeição rápida", "Econômico", "Plano B para a chegada"),
    ("Churrascaria Gramadense", "Churrasco", "Intermediário", "Opção para a última noite"),
    ("Sopas da Serra", "Sopas", "Econômico", "Boa alternativa em noite fria"),
    ("Kongo", "Pizza temática", "Premium", "Compare com Cara de Mau antes de reservar"),
    ("Burger do Geraldo", "Hambúrguer", "Econômico", "Jantar simples após passeio longo"),
    ("Galeto Itália", "Galeto", "Intermediário", "Alternativa ao churrasco"),
    ("Hard Rock Cafe Gramado", "Americana / música", "Especial", "Rua Wilma Dinnebier, 180"),
]

MARKETS = [
    ("Carrefour Gramado", "Av. Borges de Medeiros, 2300, Centro", "Mercado principal"),
    ("Rissul", "Gramado, RS", "Compare itens básicos"),
    ("Supermercado Berti", "Gramado, RS", "Alternativa local"),
    ("Dia Após Dia", "Gramado, RS", "Alternativa econômica"),
]

PACKING = {
    "Agasalhos": ["Bomber preta Marfino / corta-vento", "Casaco marrom Bluestel", "Casaco cáqui", "Moletom preto", "Casaco pesado: alugar/comprar só se necessário"],
    "Partes de cima": ["2 suéteres", "2 polos pretas", "Básica preta", "Básica marrom", "Social preta", "Social marrom", "3ª social opcional"],
    "Partes de baixo": ["3–4 calças", "Bermuda e shorts", "Calça/segunda pele"],
    "Calçados e acessórios": ["Nike", "Adidas", "Tênis marrom acamurçado", "Gorro, cachecol e luvas: comprar se a previsão justificar"],
}

LOOKS = {
    "02/09": "Básica marrom + casaco cáqui + calça + Nike. Para o fondue, social preta e tênis marrom.",
    "03/09": "Segunda pele + polo preta + bomber Marfino + calça + Adidas; leve o moletom na mochila.",
    "04/09": "Básica preta + casaco marrom Bluestel + calça + Nike. À noite, suéter + tênis marrom.",
    "05/09": "Segunda pele + suéter + casaco cáqui + calça + Adidas. Social marrom para o jantar.",
    "06/09": "Polo preta + bomber Marfino + calça confortável + Nike/Adidas.",
}

PRACTICAL_TIPS = [
    "Use camadas: segunda pele + peça intermediária + corta-vento funciona melhor que uma peça única.",
    "No começo de setembro, não trate Gramado como primavera quente; leve proteção para frio e chuva.",
    "Confira a previsão 48–72 horas antes e novamente a cada manhã.",
    "Use Nike/Adidas nos passeios longos e preserve o tênis acamurçado para noites secas.",
    "Compre água, frutas, snacks e bebidas no mercado para preservar o YUO.",
    "Confirme reservas, horários, preços e cupons diretamente com o estabelecimento.",
    "Faça backup dos gastos e checklists ao fim de cada dia.",
]
