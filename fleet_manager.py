def init_database():
    names_list = ["Picard", "Riker", "Data", "Worf", "Ducane"]
    ranks_list = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divisions_list = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids_list = ["123", "329", "671", "621", "999"]
    return(names_list, ranks_list, divisions_list, ids_list)
#####################################################################################################################
def display_menu():
          print("\n--- MENU ---")
          print("1. View All Crew")
          print("2. Search Crew by Name/ID")
          print("3. Search Crew by Diviation")
          print("4. Add Member")
          print("5. Remove Member")
          print("6. Update Crew's Rank")
          print("7. Calculate Payroll")
          print("8. Crew Analysis")
          print("0. Exit\n")
          return(input("Select option: "))
#####################################################################################################################
def display_roster(names, ranks, divs, ids):
          for i in range(len(names)):
               print(F"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}")
          print("\nReturning To Main Menu")
#####################################################################################################################
def add_member(current_names, current_ranks, current_divs, current_ids):
     option_ranks = ["Cadet", "Ensign", "Lieutenant junior grade", "Lieutenant", "Lt. Commander", "Captain"]
     option_divisions = ["Command", "Operations", "Security", "Sciences"]

     add_name = input("\nEnter new member name: ").title()

     while True:
          add_ranks = input(F"Enter new member rank {option_ranks}: ").title()

          if add_ranks not in option_ranks:
               print("Invalid Ranks")
          else:
               break
     
     while True:
          add_divs = input(F"Enter new member divisions {option_divisions}: ").title()

          if add_divs not in option_divisions:
               print("Invalid Divisions")
          else:
               break
     
     
     while True:
          add_ids = input("Enter new member ID(000): ")

          if add_ids in current_ids:
               print("Duplicate ID")
               print("Enter Different ID\n")
          else:
               break
     print(F"\nID: {add_ids} | Name: {add_name} | Rank: {add_ranks} | Division: {add_divs}")
     print(F"\nCrew Have Been Added")
     print("\nReturning To Main Menu")
     return(current_names.append(add_name), current_ranks.append(add_ranks), current_divs.append(add_divs), current_ids.append(add_ids))
#####################################################################################################################
def remove_member(current_names, current_ranks, current_divs, current_ids):
     while True:
          search_id = input("\nEnter Crew's ID that will be remove: ")

          if search_id in current_ids:
               print("Removing Crew Member")
               crew_index = current_ids.index(search_id)
               break
          else:
               print("Crew Not Found")
               print("Try Again\n")
     
     print(F"\nID: {current_ids[crew_index]} | Name: {current_names[crew_index]} | Rank: {current_ranks[crew_index]} | current_divs: {current_ids[crew_index]}")
     print("\nCrew Have Been Removed")
     print("\nReturning To Main Menu")
     return(current_names.pop(crew_index), current_ranks.pop(crew_index), current_divs.pop(crew_index), current_ids.pop(crew_index) )
#####################################################################################################################     
def update_rank(current_names, current_ranks, current_ids):
     option_ranks = ["Cadet", "Ensign", "Lieutenant junior grade", "Lieutenant", "Lt. Commander", "Captain"]

     while True:
          search_id = input("\nEnter Crew's ID that will be update: ")

          if search_id in current_ids:
               crew_index = current_ids.index(search_id)
               print(F"\nUpdating rank for {current_names[crew_index]}, Current Rank: {current_ranks[crew_index]}\n")
               break   
          else:
               print("Crew Not Found")
               print("Try Again")

     while True:
          new_rank = input(F"Enter new rank for {option_ranks}: ").title()
          if new_rank not in option_ranks:
               print("Invalid Ranks")
          else:
               current_ranks[crew_index] = new_rank
               print("Rank Updated")
               break

     print(F"\n{current_names[crew_index]}'s Rank Have Been Updated To {new_rank}")
     print("\nReturning To Main Menu")
     return(current_names, current_ranks, current_ids)
#####################################################################################################################
def search_crew(current_names, current_ranks, current_divs, current_ids):
     while True:
          print("\nSearching Crew")
          print("1. Search by Name")
          print("2. Search by ID")
          option = input("\nSelect Option: ")

          if option == "1":
               while True:
                    search_names = input("\nEnter Crew's Name: ").title()
                    if search_names in current_names:
                         print("\nCrew Found\n")
                         crew_index = current_names.index(search_names)
                         break
                    else:
                         print("\nNo Crew Found\n")
               break
          elif option == "2":
               while True:
                    search_id = input("\nEnter Crew's ID: ")
                    if search_id in current_ids:
                         print("\nCrew Found\n")
                         crew_index = current_ids.index(search_id)
                         break
                    else:
                         print("\nNo Crew Found\n")
               break
          else:
               print("Invalid Input")     
          
     print(F"ID: {current_ids[crew_index]} | Name: {current_names[crew_index]} | Rank: {current_ranks[crew_index]} | Division: {current_divs[crew_index]}")
     print("\nReturning To Main Menu")
#####################################################################################################################
def main():
     names = init_database()[0]
     ranks = init_database()[1]
     divs = init_database()[2]
     ids = init_database()[3]
     
     username = input("Enter Your Full Name: ").upper()

     while True:
          print(F"\nHello, {username}")
          choices = display_menu()

          if choices == "1":
               print(display_roster(names, ranks, divs, ids))

          elif choices == "2":
               search_crew(names, ranks, divs, ids)
          

          elif choices == "4":
               add_member(names, ranks, divs, ids)

          elif choices == "5":
               remove_member(names, ranks, divs, ids)
          
          elif choices == "6":
               update_rank(names, ranks, ids)

          elif choices == "0":
               print("Program Closing Down")
               break
          else:
               print("Invalid Input")

main()