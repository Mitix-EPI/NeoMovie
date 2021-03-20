from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from passlib.hash import pbkdf2_sha256 as sha256

def generateHash(password):
    return sha256.hash(password)

def verifyHash(password, hash):
    return sha256.verify(password, hash)

class API(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn

    def isFirstTime(self, userId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM user WHERE id = '%s'" % (userId))
            account = cursor.fetchone()
            cursor.close()
            print("First Time Checking : ", str(account), flush=True)
            if (account):
                print(str(account[3]), flush=True)
                if account[3] != "NULL":
                    return False
                else:
                    return True
            else:
                return "error"
        except Exception as e :
            print("error : getIdFromEmail\n" + str(e), flush=True)
            return "error"

    def getIdFromEmail(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM user WHERE email = '%s'" % (email))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                return str(account[0])
            else:
                return "error"
        except Exception as e :
            print("error : getIdFromEmail\n" + str(e), flush=True)
            return "error"

    def checkAccountExists(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM user WHERE email = '%s'" % (str(email)))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                return True
            else:
                return False
        except Exception as e :
            print("error : check_account_exists\n" + e, flush=True)
            return "error"

    def createAccount(self, email, password):
        try:
            hashedPassword = generateHash(password)
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO %s (email, password) VALUES ('%s', '%s')" % ("user", email, hashedPassword))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e :
            print("error : Create Account\n" + e, flush=True)
            return False

    def loginAccount(self, email, password):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM user WHERE email = %s""", (email))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                if verifyHash(password, account[2]):
                    session['loggedin'] = True
                    session['id'] = account[0]
                    session['email'] = account[1]
                    res['result'] = "Login successful"
                    userId = self.getIdFromEmail(email)
                    res['id'] = userId
                    if self.isFirstTime(userId):
                        res['firstTime'] = True
                    else:
                        res['firstTime'] = False
                        res['type'] = account[3]
                    return res
                res['error'] = "Login or password does not match"
                return res
            else:
                res['error'] = "Account doesn't exist"
                return res
        except Exception as e:
            print("error : check_signin\n" + str(e), flush=True)
            res['error'] = "internal error"
            return res

    def signout(self):
        res = {}
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        res['result'] = "signout successful"
        return json.dumps(res)

    def register(self, email, password):
        res = {}
        isExists = self.checkAccountExists(email)
        if isExists:
            res['error'] = "Account already exists"
        else:
            res['result'] = "Account created"
            self.createAccount(email, password)
        return jsonify(res)

    def login(self, email, password):
        res = self.loginAccount(email, password)
        return jsonify(res)

    def updateGenre(self, userId, genre):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("""UPDATE user SET genre = %s WHERE id = %s""", (genre, userId))
            self.conn.commit()
            cursor.close()
            res['result'] = "genre updated"
            return res
        except Exception as e :
            print("error : Genre Updated\n" + str(e), flush=True)
            res['error'] = "Internal error"
            return res

    def userSeesMovieUpdate(self, userId, movieId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO %s (id_user, id_movie) VALUES ('%s', '%s')" % ("seen_movie", userId, movieId))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e :
            print("error : userSeesMovie\n" + e, flush=True)
            return False

    def userSeesMovie(self, userId, movieId):
        res = {}
        try:
            boolean = self.userSeesMovieUpdate(userId, movieId)
            if boolean:
                res['result'] = "Movie Seen"
            else:
                res['error'] = "Error"
            return res
        except Exception as e :
            print("error : userLikeMovie\n" + e, flush=True)
            return False

    def getMovieById(self, movieId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM movie WHERE id = %s""", (movieId))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                return account
            else:
                return False
        except Exception as e :
            print("error : userLikeMovie\n" + str(e), flush=True)
            return False

    def getMovieSeenByUser(self, userId):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM seen_movie WHERE id_user = %s""", (userId))
            account = cursor.fetchall()
            cursor.close()
            if (account):
                result = []
                for row in account:
                    result.append(self.getMovieById(row[1]))
                res['result'] = result
            else:
                res['error'] = "No watched movie"
            return res
        except Exception as e :
            print("error : userLikeMovie\n" + str(e), flush=True)
            return False

    def getMovieByGenre(self, genre):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM movie WHERE genre = %s""", (genre))
            account = cursor.fetchall()
            cursor.close()
            print("Genre debug", genre, account, flush=True)
            if (account):
                res['result'] = account
            else:
                res['error'] = "Not movie in this type"
            return res
        except Exception as e :
            print("error : Movie By Genre\n" + str(e), flush=True)
            return False

    def userLikesMovie(self, userId, movieId):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO %s (id_user, id_movie) VALUES ('%s', '%s')" % ("liked_movie", userId, movieId))
            self.conn.commit()
            cursor.close()
            res['result'] = "Movie liked"
            return res
        except Exception as e :
            print("error : userSeesMovie\n" + str(e), flush=True)
            res['error'] = 'Internal Error user likes movie'
            return res

    def getMovieLikedByUser(self, userId):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM liked_movie WHERE id_user = %s""", (userId))
            account = cursor.fetchall()
            cursor.close()
            if (account):
                result = []
                for row in account:
                    result.append(self.getMovieById(row[1]))
                res['result'] = result
            else:
                res['error'] = "No movie liked"
            return res
        except Exception as e :
            print("error : userLikeMovie\n" + str(e), flush=True)
            return False

    def isPlaylistTitleExists(self, title):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM playlist WHERE title = '%s'" % (title))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                return True
            else:
                return False
        except Exception as e :
            print("error : check playlist exists\n" + e, flush=True)
            return "error"

    def getPlaylistIdFromTitle(self, title):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM playlist WHERE title = '%s'" % (title))
            account = cursor.fetchone()
            cursor.close()
            if (account):
                return str(account[1])
            else:
                return "error"
        except Exception as e :
            print("error : getPlaylistIdFromTitle\n" + e, flush=True)
            return "error"

    def insertMovieIntoPlaylist(self, movieId, playlistId):
        res = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO %s (id_playlist, id_movie) VALUES ('%s', '%s')" % ("playlist_videos", playlistId, movieId))
            self.conn.commit()
            cursor.close()
            res['result'] = "Movie inserted into playlist"
            return res
        except Exception as e :
            print("error : userSeesMovie\n" + e, flush=True)
            res['error'] = 'Internal Error user likes movie'
            return res

    def createPlaylist(self, userId, title, movieId):
        res = {}
        try:
            if (self.isPlaylistTitleExists(title)):
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO %s (id_user, title) VALUES ('%s', '%s')" % ("playlist", userId, movieId))
                self.conn.commit()
                cursor.close()
                playlistId = self.getPlaylistIdFromTitle(title)
                self.insertMovieIntoPlaylist(movieId, playlistId)
                res['result'] = 'Playlist created and movie inserted'
            else:
                res['error'] = 'Playlist title already exist'
            return res
        except Exception as e :
            print("error : createPlaylist\n" + e, flush=True)
            return False

    def addToPlaylist(self, playlistId, movieId):
        res = {}
        try:
            self.insertMovieIntoPlaylist(movieId, playlistId)
            res['result'] = 'add Movie to Playlist successfull'
        except Exception as e :
            print("error : addToPlaylist\n" + e, flush=True)
            res['error'] = "Error addToPlaylist"
            return res

