from connect import * 

# create a subroutine
def delete_film():
    idfield = input("Enter filmID for the record to be deleted:")


    #    delete the record with the film id entered 
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idfield}")

    dbCon.commit()

    print(f"Record {idfield} deleted from the songs table")

if __name__ == "__main__":
    delete_film()