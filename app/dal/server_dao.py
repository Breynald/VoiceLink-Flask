
class ServerDAO:
    def __init__(self, pool):
        self.__pool = pool

    def insertNewserver(self, serverid, servername, serverpassword, serverip, serverport, avatarutl):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO server_data (serverid, servername, serverpassword, serverip, serverport, avatarurl) VALUES (%s, %s, %s, %s, %s, %s);',
                            (serverid, servername, serverpassword, serverip, serverport, avatarutl))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()
            return False
        finally:
            conn.close() 
        
        
    def checkServerPublic(self, serverid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT serverpassword FROM server_data WHERE serverid=%s;', (serverid,))
                data = cur.fetchone()
                if data[0] is None:
                    return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close() 

  
    def checkPassword(self, serverid, serverpassword):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM server_data WHERE serverid=%s AND serverpassword=%s;',
                            (serverid, serverpassword))
                if cur.fetchone():
                    return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close() 

    def addUsertoserver(self, userid, serverid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO user_server (userid, serverid) VALUES (%s, %s);', (userid, serverid))
                return True
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()


    def getServeridlist(self, userid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT serverid FROM user_server WHERE userid=%s;', (userid, ))
                return cur.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close() 


    def getServer(self, serverid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM server_data WHERE serverid=%s;', (serverid, ))
                return cur.fetchone()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close()             

    def getChannellist(self, serverid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM channel_data WHERE serverid=%s ORDER BY channelid ASC;', (serverid, ))
                return cur.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close() 

    def getChanneluserscount(self, serverid, channelid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('SELECT currentplayer FROM channel_data WHERE serverid=%s AND channelid=%s;', (serverid, channelid))
                return cur.fetchone()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close() 

    def setChanneluserscount(self, serverid, channelid, count):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('UPDATE channel_data SET currentplayer=%s WHERE serverid=%s AND channelid=%s;', (count, serverid, channelid))
                return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close() 


    def insertNewchannel(self, serverid, channelname, channelpassword, maxplayer):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO channel_data (serverid, channelname, channelpassword, maxplayer, currentplayer) VALUES (%s, %s, %s, %s, %s);',
                            (serverid, channelname, channelpassword, maxplayer, 0))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            conn.rollback()
            return False
        finally:
            conn.close() 

    def delChannel(self, serverid, channelid):
        try:
            conn = self.__pool.connection()
            with conn.cursor() as cur:
                cur.execute('DELETE FROM channel_data WHERE serverid=%s AND channelid=%s;', (serverid, channelid))
                return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            conn.close() 
        