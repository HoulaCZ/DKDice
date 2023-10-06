from flask import Flask, redirect, render_template, request
import re
import random

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/throw")
def throw():
    dice = request.args.get("q")
    th = 0
    sum = 0
    if(re.search(r"^([0-9]+)[d k]([0-9]+)$", dice) != False):
        if re.search(r"^([0-9]+)[d]([0-9]+)$", dice) != None:
            dices = re.split("d", dice)
        elif re.search(r"^([0-9]+)[k]([0-9]+)$", dice) != None:
            dices = re.split("k", dice)
        else:
            message = "Wrong dice!"
            return render_template("error.html", message = message)

        diceAmounts = int(dices[0])
        diceValue = int(dices[1])

        for i in range(1,(diceAmounts+1)):
            th = random.randint(1,(diceValue))
            sum = th + sum

        return render_template("throw.html", sum = sum)
    else:
        message = "Wrong dice!"
        return render_template("error.html", message = message)

