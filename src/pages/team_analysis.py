from dash import html
import dash_bootstrap_components as dbc
from components.PlayerRankingTable import LatestResults
from components.RankOver20 import RankOver20
from components.HighestEarning import TeamTopScorers
from components.TeamMatchesResults import TeamMatchesResults
from components.TeamGoalsStats import TeamGoalsStats
from components.PlayerStatsOverall import TeamStatsOverall
from components.LuckyLoans import TeamBookings
#from components.TeamGoalsCountPerMin import TeamGoalsCountPerMin
#from components.TeamGoalsCountPerShirt import TeamGoalsCountPerShirt
#from components.TeamVsRivalMainCard import TeamVsRivalMainCard
# from components.TeamGamesWithRivalTable import TeamGamesWithRivalTable
# from components.TeamResultsWithRival import TeamResultsWithRival
#from components.TeamVsRivalMainCard import RivalSectionTitle
# from components.LastGameRank import LastGameRank
# from components.LastGameDistribution import LastGameDistribution
# from components.LastGameStats import LastGameStats

team_analysis_page_content = html.Div(children=[
    TeamStatsOverall,
    dbc.Row(children=[
        LatestResults,
        RankOver20,
        TeamBookings


    ]),
    dbc.Row(children=[
        TeamTopScorers,
        TeamMatchesResults,
        TeamGoalsStats

    ]),

], style={"padding-top": "3rem"})
