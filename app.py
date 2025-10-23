from src.visualizer import create_dashboard

app = create_dashboard()

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
