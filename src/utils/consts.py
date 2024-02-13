import os
import pandas as pd

SRC_FOLDER = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
DATA_FOLDER = os.path.join(os.path.dirname(
    os.path.abspath(SRC_FOLDER)), "data/")
ASSETS_FOLDER = os.path.join(os.path.dirname(
    os.path.abspath(SRC_FOLDER)), "src/assets/")

teams = pd.read_csv(os.path.join(DATA_FOLDER, "processed/teams.csv"))
u_teams = pd.read_csv(os.path.join(DATA_FOLDER, "processed/updated_teams.csv"))
bookings = pd.read_csv(os.path.join(DATA_FOLDER, "processed/bookings.csv"))
award_winners = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/award_winners.csv"))
data = pd.read_csv(os.path.join(DATA_FOLDER, "processed/qualified_teams.csv"))
goals = pd.read_csv(os.path.join(DATA_FOLDER, "processed/goals.csv"))
tours = pd.read_csv(os.path.join(DATA_FOLDER, "processed/tournaments.csv"))
u_tours = pd.read_csv(os.path.join(DATA_FOLDER, "processed/updated_tournaments.csv"))
matches = pd.read_csv(os.path.join(DATA_FOLDER, "processed/matches.csv"))
team_stats = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/teams_overall_stats.csv"))
u_team_stats = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/updated_teams_overall_stats.csv"))
actions = pd.read_csv(os.path.join(DATA_FOLDER, "processed/game_user_actions_expanded_final.csv"))

GITHUB_PROFILE = "https://github.com/arseniykan"
FACEBOOK_PROFILE = "https://www.facebook.com/arseniykan3"
LINKEDIN_PROFILE = "https://github.com/arseniykan"
