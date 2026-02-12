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
          print("2. View Crew by Diviation")
          print("3. Search for Crew")
          print("4. Add Member")
          print("5. Remove Member")
          print("6. Update Crew's Rank")
          print("7. Calculate Payroll")
          print("8. Crew Analysis")
          print("0. Exit")
          return(input("\nSelect option: "))
#####################################################################################################################
def display_roster(names, ranks, divs, ids):
          for i in range(len(names)):
               print(F"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}")
#####################################################################################################################
def add_member(current_names, current_ranks, current_divs, current_ids):
     ranks = ["Cadet", "Ensign", "Lieutenant junior grade", "Lieutenant", "Lt. Commander", "Captain"]
     divisions = ["Command", "Operations", "Security", "Sciences"]

     add_name = input("Enter new member name: ").title()

     while True:
          add_ranks = input("Enter new member rank (Cadet, Ensign, Lieutenant, Lt. Commander, Captain): ").title()
          if add_ranks not in ranks:
               print("Invalid Ranks")
          else:
               break
     
     while True:
          add_divs = input("Enter new member divisions (Command, Operations, Security, Sciences): ").title()
          if add_divs not in divisions:
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

     return(current_names.append(add_name), current_ranks.append(add_ranks), current_divs.append(add_divs), current_ids.append(add_ids))
#####################################################################################################################
def remove_member(current_names, current_ranks, current_divs, current_ids):
     while True:
          search_id = input("Enter Crew's ID that will be remove: ")
          if search_id in current_ids:
               print("Removing Crew Member")
               id_index = current_ids.index(search_id)
               break
          else:
               print("Crew Not Found")
               print("Try Again\n")

     return(current_names.pop(id_index), current_ranks.pop(id_index), current_divs.pop(id_index), current_ids.pop(id_index) )
#####################################################################################################################     
def update_rank(current_names, current_ranks, current_ids):
     return()
#####################################################################################################################
def main():
     names = init_database()[0]
     ranks = init_database()[1]
     divs = init_database()[2]
     ids = init_database()[3]
     
     username = input("Enter Your Full Name: ")

     while True:
          print(F"\nHello, {username}")
          choices = display_menu()

          if choices == "1":
               print(display_roster(names, ranks, divs, ids))

          elif choices == "4":
               add_member(names, ranks, divs, ids)

          elif choices == "5":
               remove_member(names, ranks, divs, ids)
          
          elif choices == "6":
               update_rank(names, ranks, ids)

          elif choices == "0":
               break
          else:
               print("Invalid Input")

main()