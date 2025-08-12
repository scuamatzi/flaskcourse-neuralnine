from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")


@app.template_filter("reverse_string")
def reverse_string(data):
    return data[::-1]


@app.template_filter("repeat")
def repeat(data, times=2):
    return data * times


@app.template_filter("alternate_case")
def alternate_case(data):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(data)])


@app.route("/")
def index():
    title = "Flask course"
    description = "NeuralNine course from Novice to Advanced"
    ages_list = [25, 8, 35, 9, 11, 27, 42, 6, 59, 24]
    return render_template(
        "index.html", title=title, description=description, ages_list=ages_list
    )


@app.route("/filters")
def filters():
    data = "Lorem ipsum"
    return render_template("filters.html", data=data)


@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("filters"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
