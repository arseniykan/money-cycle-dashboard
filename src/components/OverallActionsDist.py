import plotly.express as px
from utils.consts import tours, teams, actions
from dash import html, dcc
import utils.theme as theme
import pandas as pd



totals = {
    'Total Cash': actions['Total Cash'].sum(),
    'Total Saving': actions['Total Saving'].sum(),
    'Total Investment': actions['Total Investment'].sum(),
    'Total Expenditure': actions['Total Expenditure'].sum(),
}

# Convert the totals dictionary to a DataFrame for plotting
totals_df = pd.DataFrame(list(totals.items()), columns=['Category', 'Amount'])

# Create the pie chart figure using Plotly Express
pie_fig = px.pie(
    totals_df,
    names='Category',
    values='Amount',
    height=theme.MAX_CHART_HEIGHT,
    color_discrete_sequence=theme.COLOR_PALLETE,
).update_layout(
    font_family=theme.FONT_FAMILY,
    margin={"t": 5, "l": 0, "r": 0, "b": 30},
)

# Update the ActionsDist div to include the new pie chart
ActionsDist = html.Div(className="card-chart-container col-lg-4 col-md-12 col-sm-12", children=[
    html.Div(
        className="card-chart",
        children=[
            html.H4("Overall Financial Distribution",
                    className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
            dcc.Graph(
                figure=pie_fig,
                config={"displayModeBar": False},
            )
        ],
    ),
])