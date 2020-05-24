from flask import Flask, render_template, request, url_for
import us

app = Flask(__name__)


def read_results(path):
    """
    reads file with results of calculations
    :param path: str
    :return: dict
    """
    with open(path, "r") as f:
        coefficient_dict = {}
        for row in f.readlines():
            string = row.strip().split(",")
            coefficient_dict[string[0]] = (string[1], string[2])
    return coefficient_dict


@app.route("/", methods=['POST', 'GET'])
def enter():
    """
    search form for app
    rendering templates
    """
    input_form = request.form.get("input")
    if input_form is None or input_form == "":
        input_form = "NY"
    state_name = us.states.lookup(input_form)
    if isinstance(state_name, us.states.State):
        state_name = state_name.abbr.upper()
        filename = "{}.png".format(state_name)
        string1 = res_dict[state_name][0]
        string2 = res_dict[state_name][1]
        return render_template("us_state.html",
                               path=f"static/images/{filename}",
                               postot=string1, negtot=string2,
                               usa_postot=res_dict["USA"][0],
                               usa_negtot=res_dict["USA"][1])


@app.route("/", methods=['POST'])
def state():
    """
    renders base template
    to avoid empty promt error on start
    """
    return render_template("base.html")


if __name__ == '__main__':
    file_path = "/app/calculations"
    res_dict = read_results(file_path)
    app.run(debug=True)
