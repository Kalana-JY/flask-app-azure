import sqlite3
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
DB = 'todo.db'

def db():
    conn = sqlite3.connect(DB)
    conn.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT)')
    return conn

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/todos')
def list_todos():
    rows = db().execute('SELECT id, title FROM todos').fetchall()
    return jsonify([{'id': r[0], 'title': r[1]} for r in rows])

@app.post('/todos')
def add_todo():
    conn = db()
    conn.execute('INSERT INTO todos (title) VALUES (?)', 
(request.json['title'],))
    conn.commit()
    return {'status': 'created'}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
