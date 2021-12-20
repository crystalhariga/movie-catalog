import dash_bootstrap_components as dbc
from dash import dcc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

class topBar:
    # Building the search bar
    @staticmethod # to pass 0 arguments
    def Search():
        search_bar = dbc.Row(
                [
                    dbc.Col([
                         html.Div([
                             dcc.Input(id='filtering', value='', type = 'text', placeholder = "Titles, Genres, Tags"),
                         ],
                            )]),
                    dbc.Col(
                        dbc.Button(
                            "Search", id = 'search-val', color = "primary", className = "ms-2", n_clicks = 0
                        ),
                        width = "auto",
                    ),
                ],
                className = "g-0 ms-auto flex-nowrap mt-3 mt-md-0",
                align = "center",
            )
        return search_bar

    # Building a navigation bar
    @staticmethod
    def Navbar(search):
        movieLogo = "https://www.clipartmax.com/png/middle/1-18632_free-film-wallpaper-clip-art-movie-logo-without-background.png"    
        navbar = dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=movieLogo, height="30px")),
                                dbc.Col(dbc.NavbarBrand("Movie Bar", className="ms-2")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        #href="https://plotly.com",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        search,
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ]
            ),
            color = "dark",
            dark = True,
        )
        return navbar