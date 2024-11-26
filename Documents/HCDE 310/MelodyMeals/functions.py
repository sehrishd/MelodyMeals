# MelodyMeals Project Outline

# Import necessary libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import requests

# Skeleton of functions

# Authenticate with Spotify API using Spotipy.
# Returns an authenticated Spotify client.
def authenticate_spotify():
    # 1. Set up Spotify credentials (client ID, secret, and redirect URI).
    # 2. Use SpotifyOAuth to authenticate and return the Spotipy client.
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="MY_CLIENT_ID",
            client_secret="MY_CLIENT_SECRET",
            redirect_uri="MY_REDIRECT_URI",
            scope="user-library-read playlist-read-private"
        ))
        return sp
    except Exception as e:
        print(f"Error authenticating Spotify: {e}")
        return None

# Retrieve metadata (tempo, energy, mood, etc.) for a playlist.
# Parameters:
#   sp: Authenticated Spotify client.
#   playlist_link: User-provided Spotify playlist URL.
# Returns:
#   A DataFrame containing song metadata.
def get_playlist_metadata(sp, playlist_link):
    # 1. Extract playlist ID from the URL.
    # 2. Get tracks and relevant metadata using the Spotify API.
    # 3. Organize metadata into a DataFrame (tempo, energy, mood, genre).
    # 4. Return the DataFrame.
    pass 

# Analyze the mood of the playlist based on metadata.
# Parameters:
#   metadata_df: DataFrame containing playlist metadata.
# Returns:
#   A dictionary summarizing the playlist's mood (e.g., energy level, tempo range).
def analyze_mood(metadata_df):
    # 1. Calculate averages or dominant attributes from the metadata.
    # 2. Return the mood summary.
    pass


# Fetch recipe suggestions from a recipe API based on playlist mood.
# Parameters:
#   playlist_mood: Dictionary summarizing playlist mood.
# Returns:
#   A list of recipes matching the playlist mood.

SPOONACULAR_API_KEY = "my_api_key_here"
BASE_URL = "https://api.spoonacular.com"

def get_recipe_suggestions(playlist_mood):
    # 1. Map mood attributes (e.g., "energetic") to recipe categories (e.g., spicy dishes)
    # 2. Use the recipe API to fetch matching recipes.
    # 3. Return the list of recipes.
    endpoint = f"{BASE_URL}/recipes/complexSearch"
    params = {
        "query": playlist_mood,
        "number": 5,  # Number of results to return, can change this later
        "apiKey": SPOONACULAR_API_KEY
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        return response.json()["results"]  # Returns a list of recipes
    
    else:
        return {"error": response.text}
    

# Generate Custom HTML output based on the playlist the user entered
# Parameters:
#   playlist_metadata: DataFrame with song metadata.
#   recipe_suggestions: List of recipes.
# Returns:
#   HTML content to render on the web app.
def generate_web_output(playlist_metadata, recipe_suggestions):
    # 1. Use Flask's render_template function to generate dynamic HTML.
    # 2. Pass playlist metadata and recipe suggestions to the template.
    html_output = f"<h2>Playlist: {playlist_metadata['name']}</h2>"
    html_output += "<h3>Recipes:</h3><ul>"
    for recipe in recipe_suggestions:
        html_output += f"<li><a href='{recipe['url']}'>{recipe['name']}</a></li>"
    html_output += "</ul>"

    return html_output

