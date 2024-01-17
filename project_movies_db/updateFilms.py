from connect import * 

# create subroutine
def update_film():
    # ask for the SongID
    idfield = input("Enter filmID for the record to be updated:")

    # ask for the field/columns value(new value)
    # songTitle = input("Enter song Title value : ").title()
    # songArtist = input("Enter song Artist value: ").title()
    # songGenre = input("Enter Song Genre value: ").title()

    filmTitle = input("Enter film Title value: ").title()
    filmYearReleased = input("Enter film Year Release value: ").title()
    filmRating = input("Enter film Rating value: ").title()
    filmDuration = input("Enter film Duration value: ").title()
    filmGenre = input("Enter film Genre value: ").title()
    
    # add single quotes to the new value 
    filmTitle = "'"+filmTitle +"'"
    filmYearReleased ="'"+filmYearReleased+"'"
    filmRating = "'"+filmRating +"'"
    filmDuration = "'"+filmDuration +"'"
    filmGenre = "'"+filmGenre +"'"

    # update a specific field for a particula record
    dbCursor.execute(f"UPDATE tblFilms SET title = {filmTitle}, yearReleased = {filmYearReleased}, rating = {filmRating}, duration = {filmDuration}, genre = {filmGenre}  WHERE filmID = {idfield}")

    dbCon.commit()

    print(f"Record {idfield} update in the songs table")

if __name__ == "__main__":
    update_film()
        



