import json
from flask import Flask, jsonify, request, session
from connection import ConnectionDatabase
from api import API
import sys
from datetime import timedelta

app = Flask(__name__)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

conn = ConnectionDatabase(app)

def get_connection():
    return conn.get_connection()

@app.route('/')
def hello_world():
    return 'Flask API'

@app.route('/api/register', methods=['POST'])
def register():
    api = API(app, get_connection())
    try:
        email = request.args['email']
        password = request.args['password']
        genre = request.args['genre']
        return api.register(email, password, genre)
    except Exception as e:
        print(e)
        error = {
            'status': 'Error',
            'message': 'Error register'
        }
        return jsonify(error)

@app.route('/api/login', methods=['POST'])
def login():
    api = API(app, get_connection())
    try:
        print("Login before get requests", flush=True)
        email = request.args['email']
        password = request.args['password']
        print(email, flush=True)
        print(password, flush=True)
        return api.login(email, password)
    except Exception as e:
        print(e)
        error = {
            'status': 'Error',
            'message': 'Error login'
        }
        return jsonify(error)

@app.route('/api/logout', methods=['POST'])
def logout():
    api = API(app, get_connection())
    try:
        return api.logout()
    except Exception as e:
        print(e)
        error = {
            'status': 'Error',
            'message': 'Error logout'
        }
        return jsonify(error)

if __name__ == '__main__':
    app.secret_key = 'taker'
    app.permanent_session_lifetime = timedelta(minutes=5)
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
