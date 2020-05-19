from flask import Flask, render_template, request, url_for
import us

app = Flask(__name__)

with open("/home/acid/PycharmProjects/Course_Project/app/calculations", "r") as f:
    coeff_dict = {}
    for row in f.readlines():
        string = row.strip().split(",")
        coeff_dict[string[0]] = (string[1], string[2])


@app.route("/", methods=['POST', 'GET'])
def enter():
    input_form = request.form.get("input")
    if input_form is None or input_form == "":
        input_form = "NY"
    state_name = us.states.lookup(input_form)
    if isinstance(state_name, us.states.State):
        state_name = state_name.abbr.upper()
        filename = "{}.png".format(state_name)
        string1 = coeff_dict[state_name][0]
        string2 = coeff_dict[state_name][1]
        return render_template("us_state.html",
                               path=f"static/images/{filename}",
                               postot=string1, negtot=string2,
                               usa_postot=coeff_dict["USA"][0],
                               usa_negtot=coeff_dict["USA"][1])


@app.route("/", methods=['POST'])
def state():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
