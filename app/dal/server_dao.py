
class ServerDAO:
    def __init__(self, db):
        self.__db = db

    def insertNewserver(self, serverid, servername, serverpassword, serverip, serverport):
        try:
            with self.__db.cursor() as cur:
                cur.execute('INSERT INTO server_data (serverid, servername, serverpassword, serverip, serverport) VALUES (%s, %s, %s, %s, %s);',
                            (serverid, servername, serverpassword, serverip, serverport))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            self.__db.rollback()
            return False
        
        
    def checkServerPublic(self, serverid):
        try:
            with self.__db.cursor() as cur:
                cur.execute('SELECT serverpassword FROM server_data WHERE serverid=%s;', (serverid,))
                data = cur.fetchone()
                if data and (data[0] is None or data[0] == ""):
                    return True
        except Exception as e:
            print(f"An error occurred: {e}")
        return False

  
    def checkPassword(self, serverid, serverpassword):
        try:
            with self.__db.cursor() as cur:
                cur.execute('SELECT * FROM server_data WHERE serverid=%s AND serverpassword=%s;',
                            (serverid, serverpassword))
                if cur.fetchone():
                    return True
        except Exception as e:
            print(f"An error occurred: {e}")
        return False

    def addUsertoserver(self, userid, serverid):
        try:
            with self.__db.cursor() as cur:
                cur.execute('INSERT INTO user_server (userid, serverid) VALUES (%s, %s);', (userid, serverid))
                return True
        except Exception as e:
            print(f"An error occurred: {e}")
            self.__db.rollback()
            return False

