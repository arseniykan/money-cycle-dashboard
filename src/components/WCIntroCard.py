from dash import html
import dash_bootstrap_components as dbc
from utils.consts import LINKEDIN_PROFILE

WCIntroCard = html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container", children=[

    html.Div(className="card", children=[
        dbc.Row([
            dbc.Col(className="col-lg-6", children=[html.Div(className="card-header card-m-0 me-2 pb-3", children=[
                html.H2(["Money Cycle Dashboard"],
                    className="card-title m-0 me-2 mb-2", style={"font-size": "2vw"}),
                html.Span(
                    "Developed by StoryDX", style={"color": "#0084d6", "font-size": "1.5vw"})
            ]),
                html.P(["This dashboard presents all you need to know about Money Cycle app: games played, wins, progress, investment breakdown, and more. You can check each player's detailed statistics and compare them with each other in the",
                        html.A(" Players tab.", href="/team-analysis",
                               style={"color": "#0084d6"}),
                        # html.P(
                        #     "*Note: dashboard doesn't include Qatar 2022 WorldCup data.", className="mt-1")
                        ], className="card-title me-4"),
            

                html.P(["Please feel free to report any problems or reach me directly,",
                        html.A(" Arseniy Kan.", href=LINKEDIN_PROFILE, target="_blank", style={"color": "#0084d6"})], className="card-title me-4 mb-0 mt-4"),

            ]),

            dbc.Col(className="col-lg-6", children=[html.Img(
                src="./assets/images/money_cycle_background.jpg", className="img-fluid")], style={"align-self": "self-end"})
        ]),

    ])
])
