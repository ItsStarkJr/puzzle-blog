from flask import Flask, redirect, url_for, render_template, request
import webbrowser
import json

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        # Retrieve the form data
        data = {}
        data["difficulty"] = request.form.get("difficulty")
        data["variant"] = request.form.get("variant")
        data["genre"] = request.form.get("genre")
        data["title"] = request.form.get("title")
        data["intro"] = request.form.get("intro")
        data["rules"] = request.form.get("rules")

        # Retrieve checkbox values
        data["tags"] = []
        if request.form.get("drawing"):
            data["tags"].append("drawing")
        if request.form.get("hybrid"):
            data["tags"].append("hybrid")
        if request.form.get("loop"):
            data["tags"].append("loop")
        if request.form.get("number-placement"):
            data["tags"].append("number-placement")
        if request.form.get("object-placement"):
            data["tags"].append("object-placement")
        if request.form.get("pack"):
            data["tags"].append("pack")
        if request.form.get("path"):
            data["tags"].append("path")
        if request.form.get("region-division"):
            data["tags"].append("region-division")
        if request.form.get("shading"):
            data["tags"].append("shading")

        with open("data.json", "w") as file:
            json.dump(data, file)
            print(f"Saved to data.json")

        return "<p>success</p>"

    else:
        return render_template("index.html")


if __name__ == "__main__":
    webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=True)
