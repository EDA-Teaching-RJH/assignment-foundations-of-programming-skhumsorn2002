def init_database():
    names_list = ["Picard", "Riker", "Data", "Worf", "Ducane"]
    ranks_list = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divisions_list = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids_list = ["01", "02", "03", "04", "05"]
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




      
      
      



def main():
     names = init_database()[0]
     ranks = init_database()[1]
     divs = init_database()[2]
     ids = init_database()[3]




main()