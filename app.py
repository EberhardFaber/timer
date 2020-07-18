from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_time():
    return render_template("timer.html")


if __name__ == '__main__':
    app.run("0.0.0.0")
