from dash import html
from utils.consts import LINKEDIN_PROFILE


Footer = html.Div(html.H6(["©2024, Developed By ", html.A("Arseniy Kan" , href=LINKEDIN_PROFILE, target="_blank",style={"color": "#0084d6"})]), className="mt-9")