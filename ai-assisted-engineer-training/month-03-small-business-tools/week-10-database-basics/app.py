import sqlite3
from flask import Flask, g, request, jsonify

app = Flask(__name__)
DATABASE = "app.db"

def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, "_db", None)
    if db is not None:
        db.close()

@app.route("/initdb")
def initdb():
    db = get_db()
    db.executescript("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        title TEXT,
        notes TEXT
    );
    """ )
    db.commit()
    return {"ok": True}

@app.route("/candidates", methods=["GET", "POST"])
def candidates():
    db = get_db()
    if request.method == "POST":
        data = request.get_json() or {}
        db.execute("INSERT INTO candidates (name, title, notes) VALUES (?, ?, ?)",
                   (data.get("name"), data.get("title"), data.get("notes")))
        db.commit()
        return {"created": True}, 201
    rows = db.execute("SELECT id, name, title, notes FROM candidates").fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)