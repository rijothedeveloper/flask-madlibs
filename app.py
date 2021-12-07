from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/story")
def story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    answers = {}
    answers["place"] = request.args.get("place")
    answers["noun"] = request.args.get("noun")
    answers["verb"] = request.args.get("verb")
    answers["adjective"] = request.args.get("adjective")
    answers["plural_noun"] = request.args.get("plural_noun")

    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
    storyStr = story.generate(answers)
    return render_template("story.html", storyString=storyStr)