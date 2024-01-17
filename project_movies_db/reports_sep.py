from connect import *




def report_sel_all():

  dbCursor.execute("SELECT * FROM tblFilms")
#   # dbCursor.execute("SELECT * FROM tblFilms WHERE Genre IN('Action')")

#   # dbCursor.execute("SELECT * FROM tblFilms WHERE YearReleased IN('2016')")

#   dbCursor.execute("SELECT * FROM tblFilms WHERE rating IN('PG')")
  reportQuery = dbCursor.fetchall()
  for aRecord in reportQuery:
    print(aRecord)


def report_genre():

  dbCursor.execute("SELECT * FROM tblFilms WHERE Genre IN('Action')")
  reportQuery = dbCursor.fetchall()

  for aRecord in reportQuery:
    print(aRecord)



def report_year():

  dbCursor.execute("SELECT * FROM tblFilms WHERE YearReleased IN('2016')")
  reportQuery = dbCursor.fetchall()
  for aRecord in reportQuery:
    print(aRecord)



def report_rating():

  dbCursor.execute("SELECT * FROM tblFilms WHERE rating IN('PG')")
  reportQuery = dbCursor.fetchall()
  for aRecord in reportQuery:
    print(aRecord)

if __name__ == "__main__":
  report_sel_all()
  report_genre()
  report_year()
  report_rating()