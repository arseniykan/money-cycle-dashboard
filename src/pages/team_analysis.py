from dash import html
import dash_bootstrap_components as dbc
from components.TeamRankingTable import TeamRankingTable
from components.RankOver20 import RankOver20
from components.TeamTopScorers import TeamTopScorers
from components.TeamMatchesResults import TeamMatchesResults
from components.TeamGoalsStats import TeamGoalsStats
from components.TeamStatsOverall import TeamStatsOverall
from components.TeamCards import TeamBookings
from components.TeamGoalsCountPerMin import TeamGoalsCountPerMin
from components.TeamGoalsCountPerShirt import TeamGoalsCountPerShirt
from components.TeamVsRivalMainCard import TeamVsRivalMainCard
from components.TeamGamesWithRivalTable import TeamGamesWithRivalTable
from components.TeamResultsWithRival import TeamResultsWithRival
from components.TeamVsRivalMainCard import RivalSectionTitle
# from components.LastGameRank import LastGameRank
# from components.LastGameDistribution import LastGameDistribution
# from components.LastGameStats import LastGameStats

team_analysis_page_content = html.Div(children=[
    TeamStatsOverall,
    dbc.Row(children=[
        TeamRankingTable,
        RankOver20,
        TeamBookings


    ]),
    dbc.Row(children=[
        TeamTopScorers,
        TeamMatchesResults,
        TeamGoalsStats

    ]),
    # dbc.Row(children=[
    #     TeamGoalsCountPerMin,
    #     TeamGoalsCountPerShirt

    # ]),
    # dbc.Row(children=[
    #     RivalSectionTitle
    # ]),
    # dbc.Row(children=[
    #     TeamVsRivalMainCard,
    #     TeamGamesWithRivalTable,
    #     TeamResultsWithRival,

    # ]),
    # dbc.Row(children=[
    #     LastGameRank,
    #     LastGameDistribution,
    #     LastGameStats
    # ]),
], style={"padding-top": "3rem"})
