from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="3df5b6dd5b83f2d7a47968d025c27d53"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def input():
    print("Got Post Info")
    print(request.form)
    session["result-name"] = request.form["fname"]
    session["result-location"] = request.form["location"]
    session["result-language"] = request.form["language"]
    session["result-comment"] = request.form["comment"]
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)