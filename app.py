from flask import Flask, render_template, request

app = Flask(__name__)

thoughts = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        thought = request.form.get("thought", "").strip()

        if thought:
            thoughts.append(thought)

    return render_template("index.html", thoughts=thoughts)

if __name__ == "__main__":
    app.run(debug=True)