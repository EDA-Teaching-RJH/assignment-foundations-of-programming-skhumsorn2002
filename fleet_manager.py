def init_database():
    names_list = ["Picard", "Riker", "Data", "Worf", "Ducane"]
    ranks_list = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divisions_list = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids_list = ["123", "329", "671", "621", "999"]
    return(names_list, ranks_list, divisions_list, ids_list)

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
          return(input("Select option: "))

def display_roster(names, ranks, divs, ids):
          for i in range(len(names)):
               print(F"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}")

def add_member(names, ranks, divs, ids):
     add_name = input("Enter new member name: ").title()   
     add_ranks = input("Enter new member rank: ").title()
     add_divs = input("Enter new member divisions: ").title()
     add_ids = input("Enter new member ID(000): ")

     return(names.append(add_name), ranks.append(add_ranks), divs.append(add_divs), ids.append(add_ids))

def main():
     names = init_database()[0]
     ranks = init_database()[1]
     divs = init_database()[2]
     ids = init_database()[3]
     
     while True:
          choices = display_menu()
          if choices == "1":
               print(display_roster(names, ranks, divs, ids))

          elif choices == "4":
               add_member(names, ranks, divs, ids)
          else:
               break



main()