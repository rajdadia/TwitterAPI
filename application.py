from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import sys
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    positive=0
    negative=0
    neutral=0

    # analyze word
    for i in tweets:
        med=analyzer.analyze(i)
        if med > 0.0:
            positive+=1
        elif med < 0.0:
            negative+=1
        else:
            neutral+=1

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
