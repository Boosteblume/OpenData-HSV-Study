import psycopg2
import pandas as pd
from psycopg2 import OperationalError
from configs import passwords

class Connection:

     def __init__(self):
          self.connection = None

          try:
              self.connection = psycopg2.connect(
                   __host = "studyserverhh.postgres.database.azure.com",
                   __dbname = "postgres",
                   __user = "Footballstudy",
                   __password = passwords.postgres_password,
                   __sslmode = "require"
              )
              self.cursor = self.connection.cursor()
              print("Connection to Server successfull")

          except OperationalError as e:
              print(f"The error '{e}' occurred")

          return self.connection

     def get_cursor(self):
          return self.cursor()
     
     def execute_query(self, query):
          try:
               self.cursor.execute(query)
               self.cursor.close()
               self.connection.commit()
               return True

          except OperationalError as e:
               print(f"The error {e} occured")

     def read_query(self, query):
          try:
               self.cursor.execute(query)
               r = self.cursor.fetchall()
               self.cursor.close()
               return r
          except OperationalError as e:
               print(f"The error {e} occured")
     
     def read_query_df(self, select_query, column_names):
          try:
               self.cursor.execute(select_query)
          except (Exception, psycopg2.DatabaseError) as error:
               print("Error: %s" % error)
               self.cursor.close()
               return 1
          df = pd.DataFrame(self.cursor.fetchall(), columns = column_names)
          self.cursor.close()
          return df

