import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
from utils.consts import u_tours, tours, goals, award_winners, actions
import numpy as np


def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                dcc.Graph(
                    figure=fig.update_layout(
                        paper_bgcolor="rgb(0,0,0,0)",
                        plot_bgcolor="rgb(0,0,0,0)",
                        legend=dict(bgcolor=theme.LEGEN_BG),
                        font_family=theme.FONT_FAMILY,
                    ),
                    config={"displayModeBar": False},
                )
            ],
        ), className=class_name
    )


WCWinnersBar = create_card(class_name="card-chart-container col-lg-3 col-md-12 col-sm-12",
                           title="Overall Ranking",
                           fig=px.bar(
                               u_tours.groupby("winner", as_index=False).size(),
                               x="winner",
                               y="size",
                               height=theme.MAX_CHART_HEIGHT,
                               text="size",
                               color_discrete_sequence=theme.COLOR_PALLETE,
                               labels={"value": "Country",
                                       "size": "", "winner": "Winner"},
                           ).update_xaxes(categoryorder="total descending",
                                          ).update_layout(margin={"r": 20, "l": 30}))


tmp_tours = u_tours
tmp_tours["year"] = u_tours["year"].astype("str")

actions_df = actions
# Define your classification logic
risky_actions = ['Investment', 'Lottery']
safe_actions = ['Deposit (Saving)', 'Loan']
actions_df['Decision Type'] = actions_df['Action Detail'].apply(lambda x: 'Risky' if x in risky_actions else ('Safe' if x in safe_actions else 'Other'))

# Calculate counts
decision_counts = actions_df['Decision Type'].value_counts()
decision_counts = decision_counts[decision_counts.index.isin(['Risky', 'Safe'])]

AggressiveConservative = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                title="Risk Assessment",
                                fig = px.bar(
                                x=decision_counts.index,
                                y=decision_counts.values,
                                labels={'x': 'Decision Type', 'y': 'Count'},
                                color=decision_counts.index,
                                #color_discrete_map={'Risky': 'red', 'Safe': 'green'},
                                color_discrete_sequence=theme.COLOR_PALLETE,
                                height=350
                            ).update_layout(showlegend=False)
                                                          )








top_players_df = goals.groupby(["family_name", "given_name"], as_index=False).size(
).sort_values(by="size", ascending=False)
top_players_df.loc[top_players_df["given_name"]
                   == "not applicable", "given_name"] = ""
top_players_df["player_full_name"] = top_players_df["given_name"] + \
    " " + top_players_df["family_name"]

# TopWcScorersBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
#                               title="Top Scorers in World Cups",
#                               fig=px.bar(top_players_df.loc[top_players_df["size"] > 6],
#                                          y="player_full_name", x="size",
#                                          labels={"player_full_name": "",
#                                                  "size": "Goals Count"},
#                                          color_discrete_sequence=theme.COLOR_PALLETE,
#                                          height=795,
#                                          orientation="h").update_yaxes(categoryorder="total ascending"))

PenaltiesCountPerTour = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                    title="Penalties Count Per Tour",
                                    fig=px.line(goals[goals.penalty == 1].groupby("year", as_index=False).size(),
                                                x="year", y="size", color_discrete_sequence=theme.COLOR_PALLETE,
                                                height=theme.MAX_CHART_HEIGHT,))


GoalsCountPerTourLine = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                    title="Goals Count in Each Tour",
                                    fig=px.line(goals.groupby(
                                        "year", as_index=False).size(), x="year", y="size",
                                        labels={"year": "Year",
                                                "size": "Count"},
                                        height=theme.MAX_CHART_HEIGHT,
                                        color_discrete_sequence=theme.COLOR_PALLETE,))


MostAttendedMatchesBar = create_card(class_name="card-chart-container col-lg-5 col-md-12 col-sm-12",
                                     title="Most Attended Match In Each Tour",
                                     fig=px.bar(tours, x="number", y="year",
                                                text="game(s)",
                                                hover_data=["venue", "hosts"],
                                                labels={
                                                    "number": "Attendance", "year": "Year"},
                                                orientation="h",
                                                height=795,
                                                color_discrete_sequence=theme.COLOR_PALLETE
                                                ).update_yaxes(type='category'))


tmp_df = pd.DataFrame({"minute": range(121), "count": np.zeros((121))})
grouped_df = goals.groupby("minute_regulation", as_index=False).size()
tmp_df = tmp_df.merge(grouped_df, how="left",
                      left_on="minute", right_on="minute_regulation")
tmp_df["goals_count"] = tmp_df["count"] + tmp_df["size"]
tmp_df.fillna(0, inplace=True)
GoalsCountPerMinute = create_card(class_name="card-chart-container col-lg-12 col-md-12 col-sm-12",
                                  title="Goals Count per Minute",
                                  fig=px.line(tmp_df,
                                              x="minute", y="goals_count", labels={"goals_count": "Goals Count", "minute": "Minute"},
                                              color_discrete_sequence=theme.COLOR_PALLETE,
                                              height=theme.MAX_CHART_HEIGHT)
                                  )

