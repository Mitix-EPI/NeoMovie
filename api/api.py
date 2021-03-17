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
            print("error : getIdFromEmail\n" + e, flush=True)
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

    def createAccount(self, email, password, genre):
        try:
            hashedPassword = generateHash(password)
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO %s (email, password, genre) VALUES ('%s', '%s', '%s')" % ("user", email, hashedPassword, genre))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e :
            print("error : check_account_exists\n" + e, flush=True)
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
                    res['result'] = "login successful"
                    res['id'] = self.getIdFromEmail(email)
                    return res
                res['error'] = "login or password does not match"
                return res
            else:
                res['error'] = "Account doesn't exist"
                return res
        except Exception as e:
            print("error : check_signin\n" + e, flush=True)
            res['error'] = "internal error"
            return res

    def signout(self):
        res = {}
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        res['result'] = "signout successful"
        return json.dumps(res)

    def register(self, email, password, genre):
        res = {}
        isExists = self.checkAccountExists(email)
        if isExists:
            res['error'] = "account already exists"
        else:
            res['result'] = "account created"
            self.createAccount(email, password, genre)
        return jsonify(res)

    def login(self, email, password):
        res = self.loginAccount(email, password)
        return jsonify(res)

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
                res['error'] = "Not movie already seen"
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
            print(account, flush=True)
            if (account):
                res['result'] = account
            else:
                res['error'] = "Not movie already seen"
            return res
        except Exception as e :
            print("error : userLikeMovie\n" + e, flush=True)
            return False

