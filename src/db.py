import mysql.connector





class Database():
  def __init__(self):  
    self.db = mysql.connector.connect(host="localhost",
                                      database="FRIDGE",
                                      user= "knight",
                                      password="knight23",
                                      )
    self.cursor = self.db.cursor()

  def dbVersion(self):
    data = self.cursor.fetchone()
    return ("Database version : %s " % data)


  def cleanup(self):
    self.db.close()