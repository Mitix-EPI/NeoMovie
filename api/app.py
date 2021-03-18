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
        return api.register(email, password)
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
        email = request.args['email']
        password = request.args['password']
        return api.login(email, password)
    except Exception as e:
        print(e)
        error = {
            'status': 'Error',
            'message': 'Error login'
        }
        return jsonify(error)

@app.route('/api/updateGenre', methods=['POST'])
def updateGenre():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        genre = request.args['genre']
        return api.updateGenre(userId, genre)
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

@app.route('/api/movieSeen', methods=['POST'])
def movieSeen():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        movieId = request.args['movieId']
        print(userId, flush=True)
        print(movieId, flush=True)
        return api.userSeesMovie(userId, movieId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/getMovieSeen', methods=['GET'])
def getMovieSeenByUser():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        return api.getMovieSeenByUser(userId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/getMoviesByGenre', methods=['GET'])
def getMovieByGenre():
    api = API(app, get_connection())
    try:
        genre = request.args['genre']
        return api.getMovieByGenre(genre)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/likedMovie', methods=['POST'])
def movieLiked():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        movieId = request.args['movieId']
        return api.userLikesMovie(userId, movieId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/getMovieLiked', methods=['GET'])
def getMovieLikedByUser():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        return api.getMovieLikedByUser(userId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/createPlaylist', methods=['GET'])
def createPlaylist():
    api = API(app, get_connection())
    try:
        userId = request.args['userId']
        title = request.args['title']
        movieId = request.args['movieId']
        return api.createPlaylist(userId, title, movieId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

@app.route('/api/addToPlaylist', methods=['GET'])
def addToPlaylist():
    api = API(app, get_connection())
    try:
        playlistId = request.args['playlistId']
        movieId = request.args['movieId']
        return api.addToPlaylist(playlistId, movieId)
    except Exception as e:
        print(str(e), flush=True)
        error = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(error)

if __name__ == '__main__':
    app.secret_key = 'taker'
    app.permanent_session_lifetime = timedelta(minutes=5)
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
