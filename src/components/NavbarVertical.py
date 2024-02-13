from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/story_dx.png", style={"width": "3rem"}),
                html.H4("Money Cycle", className="m-0", style={"font-size": "1.0rem"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(    
                    [html.I(className="tf-icons bx bx-trophy fas fa-home"), html.Span("Main" , className="me-2")],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-group"),
                        html.Span("Players"),
                    ],
                    href="/team-analysis",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-info-circle"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                    className="pe-3",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)