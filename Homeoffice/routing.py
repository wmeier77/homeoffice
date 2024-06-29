from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

import dbService


app = Flask(__name__)

authorized = False
start_day = None
start_time = None
logged_in = False


@app.route('/')
def index():
    """Führt einen Redirect zur Login-Seite durch
    """
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Rendert die Login-Seite
    """
    global logged_in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dbService.get_user(username, password)
        if user:
            logged_in = True
            return redirect(url_for("startstop"))
        else:
            return redirect(url_for("index"))

    return render_template("login.html")


@app.route('/startstop', methods=['GET', 'POST'])
def startstop():
    """Rendert die StartStop-Seite
    """
    global logged_in

    if not logged_in:
        return redirect(url_for("login"))

    return render_template("startstop.html")


@app.route('/overview')
def overview():
    """Rendert die Uebersicht-Seite
    """
    global logged_in

    if not logged_in:
        return redirect(url_for("login"))

    return render_template("overview.html")


@app.route('/start', methods=['PUT'])
def start():
    """REST-Endpoint für die Start-Uhrzeit
    :return: 200, 500
    """
    global start_day, start_time

    today = datetime.today()
    start_day = today.strftime("%d.%m.%Y")
    start_time = today.strftime("%H:%M")

    if dbService.start(start_day, start_time):
        return "", 200
    else:
        return "Fehler während der Zeiterfassung", 500


@app.route('/stop', methods=['PUT'])
def stop():
    """REST-Endpoint für die Stop-Uhrzeit
    :return: 200, 500
    """
    global start_day, start_time

    today = datetime.today()
    stop_time = today.strftime("%H:%M")

    if dbService.stop(start_day, start_time, stop_time):
        start_day = None
        start_time = None
        return "", 200
    else:
        return "Fehler beim Aktualisieren der Zeiterfassung", 500


@app.route('/recdata/<date>', methods=['GET'])
def recdata(date):
    """REST-Endpoint für die Abfrage der Uhrzeiten
    :param date: Tag, für den die Uhrzeiten zuruckgegeben werden sollen
    :return: Die Uhrzeiten
    """
    selectedDateData = []
    if date:
        result = dbService.get_rec_data(date)
        for item in result:
            if item:
                selectedDateData.append(f"{item['start']} - {item['stop']} Uhr")

    return selectedDateData


def create_app():
    """Gibt das Flask Objekt zurueck
    """
    return app
