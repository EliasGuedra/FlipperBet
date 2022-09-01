from flask import Flask, render_template, request, url_for, flash, redirect
import requests
import random
from datetime import datetime

app = Flask(__name__, static_folder='static')


Games = {
    "players": ["Alex vs Benji"]*10,
    "times": [datetime.utcnow()]*10,
    "results": [(102390, 203300)]*10,
    "comments": ["Semifinal mellan åttan och sextionian"]*10,
    "ids": range(10),
}


bets = {
    "players": [('Anders', 'Jonas')]*10,
    "insättning": ['🍻x1']*10,
    "odds": ['2:1']*10,
    "played": [True, False, False, True, False, False, True, True, True, True],
    "positions": [(random.randint(1, 5), random.randint(1, 8)) for i in range(10)],
    "ids": range(10)
}





@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html', players=Games['players'], times=Games['times'], results=Games['results'], comments=Games["comments"], ids=Games["ids"], nr_of_games=len(Games['players']))



@app.route('/<match_id>', methods=('GET', 'POST'))
def match(match_id):

    classes = ["mlb" if x else 'pga' for x in bets['played']]

    return render_template('bets.html', ids=["ids"], insättning=bets["insättning"], classes=classes, players=bets['players'], odds=bets['odds'], played=bets['played'], nr_of_bets=len(bets['players']), positions=bets['positions'])






if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')


