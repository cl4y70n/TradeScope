# VendasInteligentes — Painel de Vendas Inteligente

**VendasInteligentes** é um painel leve e extensível para análise de vendas, geração de KPIs, sugestões de estoque e insights automáticos usando técnicas de NLP/IA (estrutura preparada para integrar LangGraph/LangChain). Projeto feito para rodar localmente com datasets pequenos (CSV) e pronto para subir no GitHub.

---

## 🚀 Principais funcionalidades
- Cálculo de KPIs: receita, lucro estimado, ticket médio, volume de vendas.
- Sugestões simples de reposição de estoque.
- Visualizações interativas com **Plotly Dash**.
- Módulo de insights (placeholder para LangGraph/Hugging Face).
- Exemplo de dataset CSV para testes.

---

## 📁 Estrutura do repositório

```
VendasInteligentes/
├── data/
│   └── vendas_exemplo.csv
├── src/
│   ├── data_loader.py
│   ├── kpi_calculator.py
│   ├── insights_generator.py
│   └── visualizer.py
├── assets/
│   └── architecture.png
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Como rodar localmente

1. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate     # Windows
```

2. Instale dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação (Dash):
```bash
python app.py
```

Abra no navegador: http://localhost:8050

---

## 🧾 Exemplo de CSV (data/vendas_exemplo.csv)
Formato esperado: `date,order_id,product,category,quantity,unit_price,region`

Veja `data/vendas_exemplo.csv` para dados de exemplo.

---

## 🔧 Como o projeto funciona (resumo)
- `data_loader.py` lê e padroniza os CSVs.
- `kpi_calculator.py` gera KPIs e métricas.
- `insights_generator.py` contém funções que podem ser substituídas por chamadas a LangGraph/LLMs.
- `visualizer.py` monta componentes do Dash (gráficos, filtros).
- `app.py` junta tudo e expõe o dashboard.

---

## 🛣️ Roadmap (melhorias)
- Conectar a APIs de ERP/CRM.
- Implementar insights com LangGraph ou LangChain.
- Exportar relatórios PDF e integração com Power BI.
- Autenticação para múltiplos usuários.

---

## 🧾 Licença
MIT — use à vontade.

