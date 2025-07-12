Below is a Python code using Dash by Plotly to create a simple dashboard that displays system performance metrics and regrets over time. This example assumes you have some historical data on system performance and regrets, which are stored in CSV files.

First, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install dash pandas plotly
```

Here's the Python code for the dashboard:

```python
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Load your data
df_performance = pd.read_csv('performance_data.csv')  # Ensure this CSV has columns 'Date' and 'Performance'
df_regret = pd.read_csv('regret_data.csv')  # Ensure this CSV has columns 'Date' and 'Regret'

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("System Performance and Regret Dashboard"),
    html.Div([
        dcc.Graph(id='performance-graph'),
        dcc.Graph(id='regret-graph')
    ]),
    html.Div([
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=df_performance['Date'].min(),
            end_date=df_performance['Date'].max(),
            display_format='YYYY-MM-DD'
        )
    ])
])

@app.callback(
    Output('performance-graph', 'figure'),
    Output('regret-graph', 'figure'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_graph(start_date, end_date):
    # Filter data based on selected date range
    filtered_df_performance = df_performance[(df_performance['Date'] >= start_date) & (df_performance['Date'] <= end_date)]
    filtered_df_regret = df_regret[(df_regret['Date'] >= start_date) & (df_regret['Date'] <= end_date)]
    
    # Create performance graph
    fig_performance = px.line(
        filtered_df_performance, x='Date', y='Performance',
        title='System Performance Over Time',
        labels={'Performance': 'Performance Score'}
    )
    
    # Create regret graph
    fig_regret = px.line(
        filtered_df_regret, x='Date', y='Regret',
        title='System Regret Over Time',
        labels={'Regret': 'Regret Score'}
    )
    
    return fig_performance, fig_regret

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```

### Explanation:
1. **Data Loading**: The code assumes you have two CSV files, `performance_data.csv` and `regret_data.csv`, each containing a 'Date' column and a 'Performance' or 'Regret' column respectively.

2. **Dash App Layout**: The layout includes two graphs and a date picker to filter data based on the date range.

3. **Callbacks**: The `update_graph` function updates the graphs based on the selected date range from the date picker.

4. **Graphs**: Plotly Express is used to create line graphs for both performance and regret metrics.

Make sure to adjust the paths to the CSV files and ensure the date formats in your CSV files match those expected by the `DatePickerRange`. This example provides a basic structure, and you can expand upon it by adding more interactive components or detailed visualizations as needed.