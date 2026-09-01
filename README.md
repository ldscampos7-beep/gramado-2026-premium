# Gramado 2026

Guia pessoal em Streamlit para a viagem de 02 a 06/09/2026, otimizado para celular.

## Estrutura

- `app.py`: interface, navegação, checklists, gastos e backup.
- `data.py`: roteiro, hotel, restaurantes, mercados, mala, looks e dicas.
- `requirements.txt`: dependência usada pelo Streamlit Community Cloud.

Para futuras alterações de conteúdo, edite primeiro `data.py`. A interface só
precisa ser alterada quando houver uma nova função ou mudança visual.

## Rodar localmente

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Publicar

Envie os três arquivos para a raiz do repositório GitHub e configure `app.py`
como arquivo principal no Streamlit Community Cloud. Os registros ficam na
sessão do navegador; use o backup JSON regularmente.
