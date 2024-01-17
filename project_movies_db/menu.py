import readFilms, addFilms, updateFilms, deleteFilms, reportsOptions, reports_sep

# function to read the contents in the menu.txt file
def read_menu():
  with open("menuOptions.txt") as fileRead:
    userMenu = fileRead.read()
  return userMenu

# print(read_menu())

def filmsMenu():
  option = 0 #
  optionsList = ["1", "2", "3", "4", "5", "6"]
  menuOptions = read_menu()

  #while the variable options(0) is not in/present in the list execute coe below
  while option not in optionsList:
    print(menuOptions) #repeat menu

#re-assign option var with the input func
    option = input("Enter an option from the films menu: ")
    if option not in optionsList:
      print(f"{option} is not a valid choice")
  return option

# print(songsMenu())

#create boolean
mainProgram = True

while mainProgram: #same as While True
  menu = filmsMenu() 

  if menu == "1": #if the input from key board mathes value 1 from list then call rea_song () in readSongs file
    readFilms.read_films()

  elif menu == "2":
    addFilms.insert_song()

  elif menu == "3":
    updateFilms.update_film()

  elif menu == "4":
    deleteFilms.delete_film()

  elif menu == "5":
    reportProgram = True

    while reportProgram: #same as While True
      menu = reportsOptions.reportsMenu() 

      if menu == "1": 
        reports_sep.report_sel_all()

      elif menu == "2":
        reports_sep.report_genre()

      elif menu == "3":
        reports_sep.report_year()

      elif menu == "4":
        reports_sep.report_rating()
      else:
        reportProgram = False
        input("Press Enter to quit the reports Menu")
        mainProgram = True
  else:
    mainProgram = False

    input("Press Enter to quit the films App")