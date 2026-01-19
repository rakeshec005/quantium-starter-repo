from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px


def load_data(csv_path='output.csv'):
	df = pd.read_csv(csv_path)
	df['Date'] = pd.to_datetime(df['Date'])
	df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0.0)
	return df


app = Dash(__name__, title='Sales Visualiser')

raw_df = load_data('output.csv')

app.layout = html.Div([
	html.Div([
		html.H1(
			'Pink Morsel Sales Visualiser',
			style={
				'textAlign': 'center',
				'color': '#fff',
				'marginBottom': '30px',
				'fontSize': '42px',
				'fontWeight': '700',
				'textShadow': '0 2px 4px rgba(0,0,0,0.3)',
				'letterSpacing': '1px',
			}
		),
		html.Div(
			[
				html.Div(
					[
						html.Label(
							'Filter by Region:',
							style={
								'fontSize': '16px',
								'fontWeight': '600',
								'color': '#333',
								'marginBottom': '12px',
								'display': 'block',
							}
						),
						dcc.RadioItems(
							id='region-radio',
							options=[
								{'label': ' All', 'value': 'all'},
								{'label': ' North', 'value': 'north'},
								{'label': ' East', 'value': 'east'},
								{'label': ' South', 'value': 'south'},
								{'label': ' West', 'value': 'west'},
							],
							value='all',
							inline=True,
							style={
								'display': 'flex',
								'gap': '20px',
								'flexWrap': 'wrap',
							},
							labelStyle={
								'marginRight': '10px',
								'cursor': 'pointer',
								'fontSize': '14px',
								'fontWeight': '500',
								'padding': '8px 12px',
								'borderRadius': '6px',
								'transition': 'all 0.3s ease',
							},
						),
					],
					style={
						'backgroundColor': '#fff',
						'padding': '20px',
						'borderRadius': '12px',
						'marginBottom': '30px',
						'boxShadow': '0 4px 15px rgba(0,0,0,0.1)',
						'animation': 'slideDown 0.5s ease-out',
					}
				),
			],
			style={'maxWidth': '1200px', 'margin': '0 auto'}
		),
		html.Div(
			dcc.Graph(id='sales-line-chart'),
			style={
				'backgroundColor': '#fff',
				'borderRadius': '12px',
				'padding': '25px',
				'boxShadow': '0 8px 25px rgba(0,0,0,0.15)',
				'maxWidth': '1200px',
				'margin': '0 auto',
				'animation': 'slideUp 0.6s ease-out',
			}
		),
	],
	style={
		'minHeight': '100vh',
		'paddingBottom': '50px',
	}),
], style={'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'})


@callback(
	Output('sales-line-chart', 'figure'),
	Input('region-radio', 'value'),
)
def update_chart(selected_region):
	if selected_region == 'all':
		filtered_df = raw_df
	else:
		filtered_df = raw_df[raw_df['Region'].str.lower() == selected_region]
	
	agg = filtered_df.groupby('Date', as_index=False)['Sales'].sum().sort_values('Date')
	
	fig = px.line(agg, x='Date', y='Sales', title=f'Total Sales by Date ({selected_region.upper()})')
	fig.update_traces(line=dict(color='#667eea', width=3), hovertemplate='<b>%{x|%b %d, %Y}</b><br>Sales: $%{y:,.2f}<extra></extra>')
	fig.update_layout(
		xaxis_title='Date',
		yaxis_title='Sales ($)',
		title_font=dict(size=24, color='#333', family='Segoe UI'),
		hovermode='x unified',
		plot_bgcolor='#f8f9fa',
		paper_bgcolor='#fff',
		xaxis=dict(
			showgrid=True,
			gridwidth=1,
			gridcolor='#e0e0e0',
			showline=True,
			linewidth=1,
			linecolor='#999',
		),
		yaxis=dict(
			showgrid=True,
			gridwidth=1,
			gridcolor='#e0e0e0',
			showline=True,
			linewidth=1,
			linecolor='#999',
		),
		margin=dict(l=60, r=40, t=80, b=60),
		height=500,
	)
	return fig


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8050)
