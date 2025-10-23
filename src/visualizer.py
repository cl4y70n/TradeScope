import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from src.data_loader import load_sales_csv
from src.kpi_calculator import calculate_kpis

def create_dashboard(server=None):
    app = dash.Dash(__name__, server=server, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    df = load_sales_csv()

    # KPIs
    kpis = calculate_kpis(df)
    revenue_fig = px.line(df.groupby('date')['total_price'].sum().reset_index(), x='date', y='total_price', title='Receita ao longo do tempo')
    category_fig = px.bar(x=list(kpis['revenue_by_category'].keys()), y=list(kpis['revenue_by_category'].values()), title='Receita por Categoria')
    top_prod = pd.DataFrame(list(kpis['top_products'].items()), columns=['product','quantity'])

    app.layout = html.Div([
        html.H1('VendasInteligentes — Painel de Vendas'),
        html.Div([
            html.Div([
                html.H3('KPIs'),
                html.P(f"Receita Total: R$ {kpis['total_revenue']:.2f}"),
                html.P(f"Pedidos: {kpis['total_orders']}"),
                html.P(f"Ticket Médio: R$ {kpis['avg_ticket']:.2f}"),
            ], className='three columns'),
            html.Div([
                dcc.Graph(figure=revenue_fig)
            ], className='nine columns')
        ], className='row'),
        html.Div([
            dcc.Graph(figure=category_fig)
        ]),
        html.Div([
            html.H3('Top Produtos'),
            dcc.Graph(figure=px.bar(top_prod, x='product', y='quantity', title='Top Produtos (Unidades)'))
        ]),
        html.Div([
            html.H3('Filtros'),
            dcc.DatePickerRange(
                id='date-range',
                start_date=df['date'].min(),
                end_date=df['date'].max()
            ),
        ]),
    ], style={'margin':'2%'})


    @app.callback(
        Output(component_id='date-range', component_property='start_date'),
        Input(component_id='date-range', component_property='end_date')
    )
    def _noop(start_date):
        # callback placeholder (Dash requires at least one)
        return start_date

    return app
