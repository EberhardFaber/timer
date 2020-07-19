from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    y = request.form.get("date")
    # m = request.form.get("month")
    # a = request.form.get("day")
    # b = request.form.get("hour")
    # c = request.form.get("minute")
    # d = request.form.get("second")
    return render_template("set.html")


@app.route('/start', methods=['GET', 'POST'])
def start():
    y = request.form.get("date")
    print(y)
    return render_template("start.html")


if __name__ == '__main__':
    app.run("0.0.0.0")
