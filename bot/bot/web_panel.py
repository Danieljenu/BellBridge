from flask import Flask, render_template, request, redirect, url_for
from bot.actions import (
    action_ring_assembly_bell,
    action_play_prayer,
    action_play_birthday,
    action_play_anthem
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bell", methods=["POST"])
def bell():
    action_ring_assembly_bell()
    return redirect(url_for("home"))

@app.route("/prayer", methods=["POST"])
def prayer():
    action_play_prayer()
    return redirect(url_for("home"))

@app.route("/birthday", methods=["POST"])
def birthday():
    action_play_birthday()
    return redirect(url_for("home"))

@app.route("/anthem", methods=["POST"])
def anthem():
    action_play_anthem()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
