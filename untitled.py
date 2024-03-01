import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load East End Prints sales data
sales_data = pd.read_csv("east_end_prints_sales.csv")

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("East End Prints Sales Dashboard"),
    
    # Dropdown for selecting product
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': prod, 'value': prod} for prod in sales_data['Product'].unique()],
        value=sales_data['Product'].unique()[0],
        multi=True,
        placeholder="Select Product(s)"
    ),
    
    # Line chart to visualize sales trends
    dcc.Graph(id='sales-trend-chart'),
    
    # Indicator for total revenue
    html.Div(id='total-revenue-indicator', className='indicator'),
    
    # Indicator for total quantity sold
    html.Div(id='total-quantity-indicator', className='indicator')
])

# Callback to update sales trend chart
@app.callback(
    Output('sales-trend-chart', 'figure'),
    [Input('product-dropdown', 'value')]
)
def update_sales_trend_chart(selected_products):
    filtered_data = sales_data[sales_data['Product'].isin(selected_products)]
    sales_trend_fig = {
        'data': [
            {'x': filtered_data[filtered_data['Product'] == product]['Date'],
             'y': filtered_data[filtered_data['Product'] == product]['Revenue'],
             'type': 'line', 'name': product} 
            for product in selected_products
        ],
        'layout': {
            'title': 'Sales Trends',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Revenue'}
        }
    }
    return sales_trend_fig

# Callback to update total revenue and total quantity indicators
@app.callback(
    [Output('total-revenue-indicator', 'children'),
     Output('total-quantity-indicator', 'children')],
    [Input('product-dropdown', 'value')]
)
def update_indicators(selected_products):
    filtered_data = sales_data[sales_data['Product'].isin(selected_products)]
    total_revenue = filtered_data['Revenue'].sum()
    total_quantity = filtered_data['Quantity'].sum()
    return f"Total Revenue: £{total_revenue}", f"Total Quantity Sold: {total_quantity}"

if __name__ == '__main__':
    app.run_server(debug=True)
