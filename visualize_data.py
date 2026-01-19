from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


def load_and_prepare(csv_path='output.csv'):
	df = pd.read_csv(csv_path)
	df['Date'] = pd.to_datetime(df['Date'])
	df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0.0)
	agg = df.groupby('Date', as_index=False)['Sales'].sum().sort_values('Date')
	return agg


app = Dash(__name__, title='Sales Visualiser')

df = load_and_prepare('output.csv')

fig = px.line(df, x='Date', y='Sales', title='Total Sales by Date')
fig.update_layout(xaxis_title='Date', yaxis_title='Sales')

app.layout = html.Div([
	html.H1('Sales Visualiser'),
	dcc.Graph(id='sales-line-chart', figure=fig),
])


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8050)
