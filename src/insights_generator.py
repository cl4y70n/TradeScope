# Placeholder insights generator.
# Designed to be swapped for a LangGraph or LLM based implementation.
import pandas as pd

def generate_insights(df: pd.DataFrame) -> list:
    insights = []
    # Example rule-based insights
    revenue_by_region = df.groupby('region')['total_price'].sum()
    top_region = revenue_by_region.idxmax()
    insights.append(f"Região com maior faturamento: {top_region} ({revenue_by_region.max():.2f})")
    # detect product growth/decline
    prod_sales = df.groupby('product').agg({'quantity':'sum'}).sort_values('quantity', ascending=False)
    if not prod_sales.empty:
        top_prod = prod_sales.index[0]
        insights.append(f"Produto mais vendido: {top_prod} (unidades: {int(prod_sales.iloc[0].quantity)})")
    # custom: low diversity alert
    if len(prod_sales) < 3:
        insights.append('Alerta: poucos produtos com vendas — considerar diversificar catálogo.')
    return insights
