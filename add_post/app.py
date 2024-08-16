from flask import Flask, redirect, url_for, render_template, request, session
import webbrowser
import json

app = Flask(__name__)
app.secret_key = "bobbelientjuh69420"


@app.route("/", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        # Retrieve the form data
        data = {
            "difficulty": request.form.get("difficulty"),
            "variant": request.form.get("variant"),
            "genre": request.form.get("genre"),
            "title": request.form.get("title"),
            "intro": request.form.get("intro"),
            "rules": request.form.get("rules"),
            "tags": [
                tag
                for tag in [
                    "drawing",
                    "hybrid",
                    "loop",
                    "number-placement",
                    "object-placement",
                    "pack",
                    "path",
                    "region-division",
                    "shading",
                ]
                if request.form.get(tag)
            ],
            "links": {
                link: request.form.get(link)
                for link in ["puzz.link", "sudokupad", "penpa"]
                if request.form.get(link)
            },
        }

        # Store the data dictionary in the session
        session["data"] = data

        # with open("data.json", "w") as file:
        #     json.dump(data, file)
        #     print(f"Saved to data.json")
        print(data)

        # return "<p>success</p>"
        return render_template("index.html", data=data)

    else:
        data = session.get("data", {})
        return render_template("index.html", data=data)


@app.route("/preview")
def preview():
    data = session.get("data", {})
    return render_template("preview.html", data=data)


if __name__ == "__main__":
    # webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=True)
