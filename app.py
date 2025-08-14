from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form.get("password")
        if username == "yo" and password == "tu":
            return "Success"
        else:
            return "Failure"


@app.route("/file_upload", methods=["POST"])
def file_upload():
    file = request.files["file"]

    if file.content_type == "text/plain":
        return file.read().decode()
    else:
        return "Not text plain"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

