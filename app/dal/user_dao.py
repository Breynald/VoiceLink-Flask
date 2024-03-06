
class UserDAO:
    def __init__(self, db):
        self.__db = db
    
    def checkRepeatemail(self, email):
        cur = self.__db.cursor()
        cur.execute('SELECT * FROM user_data WHERE email = %s;', (email, ))
        data = cur.fetchone()
        cur.close()
        return data
    
    def insertNewaccount(self, uuid, username, email, password):
        cur = self.__db.cursor()
        cur.execute('INSERT INTO user_data (uuid, username, email, password) VALUES (%s, %s, %s, %s);',
                    (uuid, username, email, password))
        cur.close()

    def checkEmailandPassword(self, email, password):
        cur = self.__db.cursor()
        cur.execute('SELECT uuid FROM user_data WHERE email = %s AND password = %s;', 
                    (email, password))
        data = cur.fetchone()
        cur.close()
        return data

        