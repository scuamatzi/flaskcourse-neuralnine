from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!"


@app.route("/hello")
def hello():
    return "Hello Friend!!"


@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2} "


@app.route("/handle_params")
def handle_params():
    # return str(request.args)
    if "name" in request.args.keys() and "surname" in request.args.keys():
        name = request.args["name"]
        surname = request.args["surname"]
        return f"Hello {name} {surname}"
    else:
        return "Some arguments are missing!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
    # app.run(debug=True)
