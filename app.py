from flask import Flask, render_template, request, flash
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sucka-my-dicka-you-dummy-stinky-ugly-dumbshmucka'


@app.route('/set', methods=['GET', 'POST'])
def sett():
    return render_template("set.html")


@app.route('/start', methods=['GET', 'POST'])
def start():
    y = request.form.get("date")
    ajs = json.dumps(y)
    print(ajs)
    return render_template("start.html")


if __name__ == '__main__':
    app.run("0.0.0.0")
