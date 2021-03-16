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
            print('Login Start', flush=True)
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM user WHERE email = %s""", (email))
            print('Login executed', flush=True)
            account = cursor.fetchone()
            cursor.close()
            print('Login cursor close', flush=True)
            if (account):
                print('Login checking password', flush=True)
                if verifyHash(password, account[2]):
                    print('password correct !', flush=True)
                    print(account, flush=True)
                    session['loggedin'] = True
                    print('DEBUGG 1', flush=True)
                    session['id'] = account[0]
                    print('DEBUGG 2', flush=True)
                    session['email'] = account[1]
                    print('DEBUGG 3', flush=True)
                    res['result'] = "login successful"
                    print('return Login', res, flush=True)
                    return res
                print('not good password', flush=True)
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
        print('TEST BEFORE REGISTER', flush=True)
        isExists = self.checkAccountExists(email)
        print('TEST REGISTER', flush=True)
        if isExists:
            res['error'] = "account already exists"
        else:
            res['result'] = "account created"
            self.createAccount(email, password, genre)
        return jsonify(res)

    def login(self, email, password):
        res = self.loginAccount(email, password)
        return jsonify(res)

