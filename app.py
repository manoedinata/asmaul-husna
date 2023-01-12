from flask import Flask, render_template, request
import requests

app = Flask(__name__)
session = requests.Session()
URL = "https://data.asmaulhusna.manoe.my.id"
defaultRandomResult = 5

@app.route("/")
def home():
    req = session.get(URL)
    data = req.json()

    return render_template("home.html", data=data)

@app.route("/random")
def show_random():
    resultNum = request.args.get("result_num")
    if resultNum:
        req = session.get(URL + "/random", params={"result_num": int(resultNum)})
    else:
        req = session.get(URL + "/random", params={"result_num": defaultRandomResult})
    data = req.json()

    return render_template("random.html", data=data)

if __name__ == "__main__":
    app.run()
