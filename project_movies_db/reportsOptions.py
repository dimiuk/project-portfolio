import reports_sep

# function to read the contents in the menu.txt file
def read_rep_menu():
  with open("reportsOptions.txt") as fileRead:
    userMenu = fileRead.read()
  return userMenu

# print(read_menu())

def reportsMenu():
  option = 0 #
  optionsList = ["1", "2", "3", "4", "5"]
  menuOptions = read_rep_menu()

  #while the variable options(0) is not in/present in the list execute coe below
  while option not in optionsList:
    print(menuOptions) #repeat menu

#re-assign option var with the input func
    option = input("Enter an option from the reports menu: ")
    if option not in optionsList:
      print(f"{option} is not a valid choice")
  return option

# print(songsMenu())

#create boolean
# reportProgram = True

# while reportProgram: #same as While True
#   menu = reportsMenu() 

#   if menu == "1": 
#     reports_sep.report_sel_all()

#   elif menu == "2":
#     reports_sep.report_genre()


#   elif menu == "3":
#     reports_sep.report_year()


#   elif menu == "4":
#     reports_sep.report_rating()


#   else:
#     reportProgram = False

#   input("Press Enter to quit the reports Menu")

  