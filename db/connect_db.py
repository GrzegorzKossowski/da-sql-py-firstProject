import psycopg2
import colors

class DatabaseConnection:
  def __init__(self, hostname, port, database, username, password) -> None:
    self.hostname = hostname
    self.port = port
    self.database = database
    self.username = username
    self.password = password
    self.connection = None
    
  def connect(self):
    try:
      self.connection = psycopg2.connect(
        host = self.hostname,
        port=self.port,
        database=self.database,
        user=self.username,
        password=self.password,
      )
      colors.prGreen('DB connection established.')
      # print('DB connection established.')
    except psycopg2.Error as e:
      colors.prRed('DB connection error: ', e)

  def close(self):      
      if self.connection:
        self.connection.close()
        colors.prYellow('DB connection closed')