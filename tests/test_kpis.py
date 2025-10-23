from src.data_loader import load_sales_csv
from src.kpi_calculator import calculate_kpis

def test_kpis():
    df = load_sales_csv()
    kpis = calculate_kpis(df)
    assert 'total_revenue' in kpis
    assert kpis['total_revenue'] >= 0
