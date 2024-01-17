from connect import *




def reports():

 
  dbCursor.execute("SELECT * FROM tblFilms")

#   # dbCursor.execute("SELECT * FROM tblFilms WHERE Genre IN('Action')")

#   # dbCursor.execute("SELECT * FROM tblFilms WHERE YearReleased IN('2016')")

#   dbCursor.execute("SELECT * FROM tblFilms WHERE rating IN('PG')")

  reportQuery = dbCursor.fetchall()

  for aRecord in reportQuery:
    print(aRecord)


if __name__ == "__main__":
  reports()
