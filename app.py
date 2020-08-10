from flask import Flask, render_template, request, flash
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sucka-my-dicka-you-dummy-stinky-ugly-dumbshmucka'


@app.route('/', methods=['GET', 'POST'])
def sett():
    return render_template("set.html")


if __name__ == '__main__':
    app.run("0.0.0.0")
