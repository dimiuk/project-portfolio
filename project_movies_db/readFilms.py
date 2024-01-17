from connect import * 

# create a subroutine
def read_films():
    # select all records from the table 
    dbCursor.execute("SELECT * FROM tblFilms")

    # fetch all records that have been selected using the fetchall method
    allRecords = dbCursor.fetchall()

    # loop through all records in the database
    for eachrecord in allRecords:
        # display every record you find 
        print(eachrecord)

if __name__ == "__main__":
    read_films()