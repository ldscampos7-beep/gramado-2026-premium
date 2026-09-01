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
        "summary": "Chegada, preparação para o frio, centro de Gramado e jantar com bom custo-benefício.",
        "tip": "Faça as compras de inverno logo após chegar, antes do passeio pelo centro.",
        "sections": {
            "Manhã": [("Viagem", "Deslocamento para Gramado", HOTEL["address"])],
            "Almoço": [
                ("Após a chegada", "Almoço no Sabor da Nonna / buffet livre", "Restaurante Sabor da Nonna Gramado"),
                ("Plano B", "Churrascaria Gramadense, se o horário for mais conveniente", "Churrascaria Gramadense Gramado"),
            ],
            "Tarde": [
                ("14h", "Check-in no Laghetto Premio", HOTEL["address"]),
                ("Logo após", "Aluguel de casaco pesado na Top 50", "Top 50 aluguel de roupas Gramado"),
                ("Em seguida", "Lojinhas locais: comprar gorro, cachecol e luvas", "Lojas de roupas de inverno Centro Gramado"),
                ("17h", "Rua Coberta, Igreja São Pedro, Fonte do Amor Eterno e Borges", "Rua Coberta Gramado"),
            ],
            "Lanche": [("Fim da tarde", "Chocolate ou café no centro, se houver vontade", "Centro Gramado")],
            "Noite/Jantar": [
                ("20h", "Jantar de bom custo-benefício · Campo & Vinho (rodízio de pizza)", "Campo e Vinho Gramado"),
                ("Alternativa", "Churrascaria Gramadense", "Churrascaria Gramadense Gramado"),
                ("Depois", "Caminhada noturna e retorno ao hotel", HOTEL["address"]),
            ],
        },
    },
    "03/09 · City Tour Gramado + Canela": {
        "date": date(2026, 9, 3),
        "summary": "City Tour completo, almoço livre, pausa para hambúrguer e massas no jantar.",
        "tip": "Jantar obrigatório no Galeto Itália; confirme o horário de retorno antes de reservar.",
        "sections": {
            "Manhã": [
                ("Manhã", "Café da manhã no hotel", HOTEL["address"]),
                ("Saída", "City Tour Gramado + Canela · Turistur", "Gramado Canela RS"),
            ],
            "Almoço": [("Durante o tour", "Almoço livre no passeio", "Gramado Canela RS")],
            "Tarde": [("Passeio", "Lago Negro, atrações de Gramado, Canela e região do Caracol", "Parque do Caracol Canela")],
            "Lanche": [("Pausa da tarde", "Hambúrguer no Burguer do Geraldo", "Burguer do Geraldo Gramado")],
            "Noite/Jantar": [
                ("Após o retorno", "Descanso e troca de roupa no hotel", HOTEL["address"]),
                ("20h", "Jantar obrigatório · Massas no Galeto Itália", "Galeto Itália Gramado"),
                ("Depois", "Rua Coberta e centro iluminado", "Rua Coberta Gramado"),
            ],
        },
    },
    "04/09 · Maria Fumaça + Fondue": {
        "date": date(2026, 9, 4),
        "summary": "Maria Fumaça, almoço livre, chocolate à tarde e fondue no Versoi.",
        "tip": "Noite de fondue obrigatória no Versoi; reserve com antecedência.",
        "sections": {
            "Manhã": [
                ("Manhã", "Café da manhã no hotel", HOTEL["address"]),
                ("Saída", "Passeio Maria Fumaça", "Maria Fumaça Bento Gonçalves"),
            ],
            "Almoço": [("Durante o passeio", "Almoço livre no passeio", "Bento Gonçalves RS")],
            "Tarde": [("Passeio", "Continuação da experiência da Maria Fumaça e retorno", "Maria Fumaça Bento Gonçalves")],
            "Lanche": [("Pausa da tarde", "Chocolate e café na Chocolate Lugano", "Chocolate Lugano Gramado")],
            "Noite/Jantar": [
                ("Após o retorno", "Descanso no hotel", HOTEL["address"]),
                ("20h", "Noite obrigatória de fondue · Versoi", "Versoi Gramado")
            ],
        },
    },
    "05/09 · Nova Petrópolis + Kongo": {
        "date": date(2026, 9, 5),
        "summary": "Nova Petrópolis, almoço livre, pausa para caldo e pizzaria temática Kongo.",
        "tip": "Jantar temático obrigatório na Kongo; confirme a sessão e faça reserva.",
        "sections": {
            "Manhã": [
                ("Manhã", "Saída para Nova Petrópolis", "Nova Petrópolis RS"),
                ("Passeio", "Praça das Flores, Labirinto Verde e Aldeia do Imigrante", "Parque Aldeia do Imigrante")
            ],
            "Almoço": [("Durante a excursão", "Almoço livre no passeio", "Centro Nova Petrópolis")],
            "Tarde": [
                ("Tarde", "Parque Pedras do Silêncio", "Parque Pedras do Silêncio"),
                ("Fim da tarde", "Ninho das Águias, se o clima permitir", "Ninho das Águias Nova Petrópolis")
            ],
            "Lanche": [("Pausa da tarde", "Caldos na Sopas da Serra", "Sopas da Serra Gramado")],
            "Noite/Jantar": [
                ("Após o retorno", "Banho e descanso no hotel", HOTEL["address"]),
                ("20h30", "Pizzaria temática obrigatória · Kongo", "Kongo Pizzaria Temática Gramado"),
                ("Depois", "Última caminhada pelo centro", "Rua Coberta Gramado")
            ],
        },
    },
    "06/09 · Manhã livre + Aeroporto": {
        "date": date(2026, 9, 6),
        "summary": "Compras finais, uma única refeição antes da partida e retorno.",
        "tip": "Escolha almoço ou lanche conforme o transfer; não planeje jantar.",
        "sections": {
            "Manhã": [
                ("8h", "Café da manhã e fechamento das malas", HOTEL["address"]),
                ("9h", "Última caminhada, chocolates e lembranças", "Rua Coberta Gramado")
            ],
            "Almoço": [("Antes da partida", "Almoço leve ou buffet livre, conforme o horário do transfer", "Centro Gramado")],
            "Tarde": [("Com margem", "Retorno ao hotel e transfer para o aeroporto", HOTEL["address"])],
            "Lanche": [("Alternativa ao almoço", "Lanche rápido antes da partida", "Centro Gramado")],
            "Noite/Jantar": [("Retorno", "Sem jantar programado em Gramado", "Aeroporto Internacional Salgado Filho")],
        },
    },
}

RESTAURANTS = [
    ("Versoi", "Fondue", "Especial", "Jantar fixado para o dia 4"),
    ("Cara de Mau", "Pizza temática", "Premium", "Experiência; reservar e conferir sessão"),
    ("Pizzaria Scur", "Pizza", "Intermediário", "Alternativa mais racional à temática"),
    ("Sabor da Nonna / Campo & Vinho", "Buffet caseiro", "Econômico", "Boa escolha de almoço"),
    ("Empório Benetti", "Refeição rápida", "Econômico", "Plano B para a chegada"),
    ("Churrascaria Gramadense", "Churrasco", "Intermediário", "Opção para a última noite"),
    ("Sopas da Serra", "Sopas", "Econômico", "Boa alternativa em noite fria"),
    ("Kongo", "Pizza temática", "Premium", "Compare com Cara de Mau antes de reservar"),
    ("Burguer do Geraldo", "Hambúrguer", "Econômico", "Lanche planejado para o dia 3"),
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
