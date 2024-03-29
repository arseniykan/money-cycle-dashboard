import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback

RankOver20 = html.Div(className="card-chart-container col-lg-6 md-6 sm-12",
                       children=[

                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("Ranking over last 20 Games",
                                           className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                                   dls.Triangle(
                                       id="team-goals-count-per-tour",
                                       children=[


                                       ], debounce=theme.LOADING_DEBOUNCE
                                   )
                               ]
                           )

                       ],
                       style={"min-height" :"26.25rem"}
                       )


@callback(
    Output("team-goals-count-per-tour", "children"),
    Input("query-team-select", "value"),
    # State("goals-df", "data"),
    State("qualified-teams-df" , "data")
)
def update_figures(query_team, qualified_teams_df):
    # goals_df = pd.read_json(goals_df)
    qualified_teams_df = pd.read_json(qualified_teams_df)

    team_data = qualified_teams_df.loc[qualified_teams_df.team_name == query_team].groupby("year",as_index=False).sum(numeric_only=True)

    # goals_df = goals_df.loc[goals_df.team_name == query_team].groupby(
    #     "year", as_index=False).size().merge(qualified_teams_df[["year" , "rank"]] , on="year", how="left")
    # goals_df.rename(columns = {'size':'Goals Count' , "rank":"Rank"}, inplace = True)
    

    figure = px.line(team_data, x="year", y=["rank"] , labels={"rank":"Rank" , "year":"Game", "variable": ''}, color_discrete_sequence=theme.COLOR_PALLETE)
    
    figure.update_yaxes(autorange="reversed")
    

    return dcc.Graph(figure=figure.
        update_xaxes(type="category")
        .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                       plot_bgcolor="rgb(0,0,0,0)",
                       legend=dict(
                           bgcolor=theme.LEGEN_BG),
                       font_family=theme.FONT_FAMILY,
                       ),
        config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )
