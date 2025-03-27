from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connexion à la base de données
def connect_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Création de la table (exécutée une seule fois)
with connect_db() as db:
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db.commit()

# Route : récupérer tous les utilisateurs
@app.route("/users", methods=["GET"])
def get_users():
    with connect_db() as db:
        users = db.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(row) for row in users])

# Route : ajouter un utilisateur
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Missing 'name'"}), 400
    
    with connect_db() as db:
        db.execute("INSERT INTO users (name) VALUES (?)", (data["name"],))
        db.commit()
    return jsonify({"message": "User added"}), 201

# Route : récupérer un utilisateur par ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    with connect_db() as db:
        user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return jsonify(dict(user)) if user else jsonify({"error": "User not found"}), 404

# Route : supprimer un utilisateur
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    with connect_db() as db:
        result = db.execute("DELETE FROM users WHERE id = ?", (user_id,))
        db.commit()
    return jsonify({"message": "User deleted"}) if result.rowcount else jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
