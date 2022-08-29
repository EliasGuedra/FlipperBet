from flask import Flask, render_template, request, url_for, flash, redirect
import requests



app = Flask(__name__, static_folder='static')


Games = {
    "players": ["Alex vs Benji"]*10,
    "times": ["18:00:00"]*10,
    "results": [(102390, 203300)]*10,
    "comments": ["Semifinal mellan åttan och sextionian"]*10
}


@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html', players=Games['players'], times=Games['times'], results=Games['results'], comments=Games["comments"], nr_of_games=len(Games['players']))



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')


