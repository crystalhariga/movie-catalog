import dash
import dash_bootstrap_components as dbc
import pandas as pd
import requests
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from dash_bootstrap_components._components.Container import Container

# Imported functions from various class files
from topBar import topBar # class that returns the navigation bar on top
from readData import readData # class to read/prep data
from movie_content import MovieContent # class to return movie details
print("Loading...")
search = topBar.Search()
nav = topBar.Navbar(search)
rat = readData.rating()
rat5 = rat.loc[rat["rating"] == 5.0]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])



app.layout = html.Div([
    html.Div([
        html.H3(children='Movies Database App',
                style={'textAlign': 'center'}),
        nav, # navbar taken from separate file
        html.Br(),
        dbc.Carousel(id='movie_carousel',
                    items=[],
                    controls=True,
                    indicators=True,
                    style={'width': 220, 'align': 'center'})
    ]), ])

## callback for collapsing searchbar
@app.callback(
            Output("navbar-collapse", "is_open"), # collapsing/opening the navbar
            [Input("navbar-toggler", "n_clicks")], # navbar toggling
            [State("navbar-collapse", "is_open")] # checking state of navbar
            )

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


## callback to generate results based on tag search (need to sort by tag count desc)
@app.callback(
            Output('movie_carousel', 'items'),            
            [Input('search-val', 'n_clicks')],
            [State('filtering', 'value')],
            )

def searching(n_clicks, value):
    ratsmp = rat5.sample(10) # randomly sample movies
    general = ratsmp["movieId"].values.tolist()
    movies = []
    if n_clicks == 0: # before any user input
        #### randomly show 10 movies with 5.0 ratings
        for movieId in general:
            movieinfo = MovieContent.get_movie_info(movieId)
            carousel = { # carousel content
                'key': general.index(movieId), # movie index as the key
                'src': movieinfo.get("image"), # image to be displayed
                'header': movieinfo.get("title"), # movie title
                'caption': movieinfo.get("rating"), # movie rating
            }
            movies.append(carousel)
        return movies
    elif n_clicks > 0: # when user has clicked the button
        category = MovieContent.checkCategory(value) # get category
        searchid = MovieContent.matchRows(category, value) # get movie ids that match
        search10 = MovieContent.checkRating(searchid) # filter top 10 results based on rating
        for movieId in search10:
            movieinfo = MovieContent.get_movie_info(movieId)
            carousel = { # carousel content
                'key': search10.index(movieId), # movie index as the key
                'src': movieinfo.get("image"), # image to be displayed
                'header': movieinfo.get("title"), # movie title
                'caption': movieinfo.get("rating"), # movie rating
            }
            movies.append(carousel)
        return movies
            




if __name__ == '__main__':
    app.run_server(debug=True)
    