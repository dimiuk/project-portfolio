from connect import *

# create a subroutine 
def insert_song():
    #SongID field is auto increment (no data input is required)
    
    # ask for user input for Title, Artist and Genre
    filmTitle = input("Enter film Title: ")
    filmYearReleased = input("Enter film Year Release: ")
    filmRating = input("Enter film Rating: ")
    filmDuration = input("Enter film Duration: ")
    filmGenre = input("Enter film Genre: ")

  

    #data from Title, Artist and Genre variables and save it into the database.
    dbCursor.execute("INSERT INTO tblFilms(Title, YearReleased, Rating, Duration, Genre) VALUES(?,?,?,?,?)", (filmTitle, filmYearReleased, filmRating, filmDuration, filmGenre))
    # Permanently save the record in the songstable in the database
    dbCon.commit()

    print(f"{filmTitle} inserted in the songs table. ")

if __name__ == "__main__":
    insert_song()

