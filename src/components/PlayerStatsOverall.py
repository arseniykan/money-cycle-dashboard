from dash.dependencies import Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
import dash_loading_spinners as dls
import utils.theme as theme
from dash import callback
from utils.consts import *


wc_winning_times_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="winning-times-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Times Winner"], style={"font-size": "1vw"}
                         ),
                         html.Small(
                             className="card-text", id="winning-years-text",
                             style={"font-size": "0.6rem"}

                         )
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/money_cycle.png", style={"width": "8rem"})
            ]
            )
        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)

participations_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="participation-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Games Played"], style={"font-size": "1vw"}
                         ),
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/money.png", style={"width": "8rem"})
            ]
            )
        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)


matches_count_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="matches-count-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Rounds"], style={"font-size": "1vw"}
                         ),
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/dice.png", style={"width": "9rem"})
            ]
            )
        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)


TeamStatsOverall = dbc.Row(children=[
    html.Div(className="col-lg-3 col-md-6 col-sm-12 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info",
                         children=[
                             dbc.Select(
                                 id="query-team-select",
                                 value="Richard Martinez",
                                 options=[
                                     {"label": l, "value": l} for l in u_teams.team_name.values
                                 ],
                                 style={"width": "10rem"}
                             ),
                             html.P(className="card-text mb-1 mt-1 fs-sm",
                                    id="team-code-text",
                                    children=[f"Player ID: "]),
                             html.P(className="card-text mb-1 fs-sm",
                                    id="team-region-text",
                                    children=[f"City:"]),
                             html.P(className="card-text mb-1 fs-sm",
                                    id="team-confederation-text",
                                    children=[f"School: "]),
                             html.A(id="query-team-wiki-link",
                                    target="_blank",
                                    style={"font-size": "0.7rem"})
                         ]),
                html.Div(className="card-icon d-flex align-items-center w-40 justify-content-center p-1", children=[
                    # dls.Triangle(
                    #     html.Img(className="img-fluid bx-lg",
                    #              id="team-flag-main",
                    #              style={
                    #                  "width": "2em", "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}
                    #              ),
                    #     debounce=theme.LOADING_DEBOUNCE
                    # )
                    html.Img(className="img-fluid bx-lg",
                    src="./assets/images/user.png",
                    style={"width": "2em", "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"})
                ]
                )

            ])

        ])
    ], style={"min-height": "11rem"})]
    ),
    wc_winning_times_card,

    participations_card,

    matches_count_card,
])


@callback(
    Output("team-code-text", "children"),
    Output("team-region-text", "children"),
    Output("team-confederation-text", "children"),
    # Output("team-flag-main", "src"),
    Output("query-team-wiki-link", "href"),
    Output("query-team-wiki-link", "children"),
    Output("winning-times-text", "children"),
    Output("winning-years-text", "children"),
    Output("participation-text", "children"),
    Output("matches-count-text", "children"),
    Input("query-team-select", "value"),
    State("teams-df", "data"),
)
def update_team_select(query_team, teams_df):
    teams_df = pd.read_json(teams_df)
    team_code = f"Player ID: {teams_df.loc[teams_df.team_name==query_team , 'team_code'].values[0]}"
    team_region = f"City: {teams_df.loc[teams_df.team_name==query_team , 'region_name'].values[0]}"
    team_confederation = f"School: {teams_df.loc[teams_df.team_name==query_team , 'confederation_code'].values[0]}"
    team_flag = f"./assets/flags/4x3/{query_team}.svg"
    wiki_link = teams_df.loc[teams_df.team_name ==
                             query_team, 'team_wikipedia_link'].values[0]

    matches_count = u_team_stats.loc[u_team_stats.team_name ==
                                   query_team]["count_matches"].values[0]
    winning_times = u_team_stats.loc[u_team_stats.team_name ==
                                   query_team]["winning_times"].values[0]
    participation_count = u_team_stats.loc[u_team_stats.team_name ==
                                         query_team]["participations"].values[0]

    winning_years = "- ".join(tours.loc[tours.winner ==
                                        query_team, "year"].values.astype("str"))

    return team_code, team_region, team_confederation, wiki_link, f"{query_team}'s profile", winning_times, winning_years, participation_count, matches_count
