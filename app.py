from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("thoughts.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS thoughts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        thought = request.form.get("thought")

        if thought and thought.strip():
            conn = sqlite3.connect("thoughts.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO thoughts (content) VALUES (?)",
                (thought.strip(),)
            )

            conn.commit()
            conn.close()

    conn = sqlite3.connect("thoughts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM thoughts ORDER BY id DESC")

    thoughts = [row[0] for row in cursor.fetchall()]

    conn.close()

    return render_template("index.html", thoughts=thoughts)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)