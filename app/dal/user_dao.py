
class UserDAO:
    def __init__(self, pool):
        self.__pool = pool
    
    def checkRepeatemail(self, email):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM user_data WHERE email = %s;', (email, ))
                return cur.fetchone()
        except Exception as e:
                print(f"An error occurred: {e}")
                return None
        finally:
            conn.close() 
    
    def insertNewaccount(self, userid, username, email, password):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO user_data (userid, username, email, password) VALUES (%s, %s, %s, %s);',
                            (userid, username, email, password))
                return True
        except Exception as e:
                print(f"An error occurred: {e}")
                conn.rollback()
                return False
        finally:
            conn.close() 



    def checkEmailandPassword(self, email, password):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT userid FROM user_data WHERE email = %s AND password = %s;', 
                            (email, password))
                return cur.fetchone()
        except Exception as e:
                print(f"An error occurred: {e}")
                return None
        finally:
            conn.close() 


    def getUser(self, userid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM user_data WHERE userid = %s;', 
                            (userid,))
                return cur.fetchone()
        except Exception as e:
                print(f"An error occurred: {e}")
                return None
        finally:
            conn.close()

    def setUsername(self, userid, username):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('UPDATE user_data SET username=%s WHERE userid=%s;',
                            (username, userid))
                return True
        except Exception as e:
                print(f"An error occurred: {e}")
                conn.rollback()
                return False
        finally:
            conn.close() 











    


        