import pymysql as sql

class ConnectionDatabase(object):

    def __init__(self, app):
        self.conn = None
        self.set_connection()

    def set_connection(self):
        try:
            self.conn = sql.connect(host= "db",
                                    user = "taker",
                                    password = "taker",
                                    db = "neomovie")
            if self.conn == None:
                raise Exception
        except (Exception) as error:
            print(error)
            exit(84)

    def get_connection(self):
        return (self.conn)