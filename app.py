from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form['name_input']
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run()
