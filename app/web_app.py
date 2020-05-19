from flask import Flask, render_template, flash, request, url_for
import us

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/state", methods=['POST', 'GET'])
def enter():
    input_form = request.form.get("input")
    state_name = us.states.lookup(input_form)
    if isinstance(state_name, us.states.State):
        filename = "{}.png".format(state_name.abbr.upper())
        return render_template("state.html", path="static/images/{}".format(filename))


@app.route("/", methods=['POST'])
def state():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
