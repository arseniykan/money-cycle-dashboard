from dash import html
import dash_bootstrap_components as dbc
from components.OverallActionsDist import ActionsDist
from components.WCComponents import *
from components.WCIntroCard import WCIntroCard
from components.TeamGoalsStats import TeamGoalsStats

worldcup_page_content = html.Div([
    dbc.Row([
            WCIntroCard,
            ]),

    dbc.Row([
        WCWinnersBar,
        # WCWinnerRegion,
        ActionsDist,
        AggressiveConservative,

    ]),


    # dbc.Row([
    #     MostAttendedMatchesBar,
    #     dbc.Col([GoalsCountPerTourLine,
    #              GoalsCountPerMinute, ], className="m-0 p-0")
    # ]),


    dbc.Row([
    ]),

    dbc.Row([

    ]),
], style={"padding-top": "40px"})
