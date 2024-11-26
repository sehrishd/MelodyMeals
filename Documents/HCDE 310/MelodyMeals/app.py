from flask import Flask, render_template, request

# import necessary functions from functions.py so that Flask has access!
from functions import authenticate_spotify, get_playlist_metadata, analyze_mood, get_recipe_suggestions, generate_web_output


# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

# Handle user input (Spotify playlist link) and generate recipe suggestions
@app.route('/submit', methods=['POST'])
def submit_playlist():
    playlist_link = request.form['playlist_link']
    sp = authenticate_spotify()
    if not sp:
        return "Error authenticating with Spotify."

    playlist_metadata = get_playlist_metadata(sp, playlist_link)
    if playlist_metadata is None:
        return "Error fetching playlist metadata."

    playlist_mood = analyze_mood(playlist_metadata)
    recipe_suggestions = get_recipe_suggestions(playlist_mood)
    return generate_web_output(playlist_metadata, recipe_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
