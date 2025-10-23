import pandas as pd

def calculate_kpis(df: pd.DataFrame) -> dict:
    total_revenue = df['total_price'].sum()
    total_orders = df['order_id'].nunique()
    total_items = df['quantity'].sum()
    avg_ticket = total_revenue / total_orders if total_orders else 0
    revenue_by_category = df.groupby('category')['total_price'].sum().sort_values(ascending=False).to_dict()
    top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(10).to_dict()
    return {
        'total_revenue': float(total_revenue),
        'total_orders': int(total_orders),
        'total_items': int(total_items),
        'avg_ticket': float(avg_ticket),
        'revenue_by_category': revenue_by_category,
        'top_products': top_products
    }

def suggest_restock(df: pd.DataFrame, threshold_multiplier: float = 0.2) -> dict:
    # Simple heuristic: compare last 30 days average sales per product to a placeholder 'stock' (mock)
    # For MVP we generate suggestions based on quantity sold
    avg_sold = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
    suggestions = {}
    for product, qty in avg_sold.items():
        # placeholder stock level heuristic
        stock_estimate = max(1, int(qty * 0.5))
        if stock_estimate < qty * threshold_multiplier:
            suggestions[product] = {
                'estimated_stock': stock_estimate,
                'recent_sales': int(qty)
            }
    return suggestions
