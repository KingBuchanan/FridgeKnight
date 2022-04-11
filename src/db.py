import MySQLdb





class Database():
  def __init__(self):  
    self.db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    self.cursor = self.db.cursor()

  def dbVersion(self):
    data = self.cursor.fetchone()
    print "Database version : %s " % data

  def cleanup(self):
    self.db.close()