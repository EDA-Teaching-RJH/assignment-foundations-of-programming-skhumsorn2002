def init_database():
    names_list = ["Picard", "Riker", "Data", "Worf", "Ducane"]
    ranks_list = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divisions_list = ["Command", "Command", "Operations", "Security", "sciences"]
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
          print("\n--- Crew List ---")
          for i in range(len(names)):
               print(F"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}")
          print("\nReturning To Main Menu")
#####################################################################################################################
def add_member(current_names, current_ranks, current_divs, current_ids):
     option_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Cadet"]
     option_divisions = ["Command", "Operations", "Security", "Sciences"]
     print("\n--- ")

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
     print("\n--- Removing Crew ---")
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
     option_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Cadet"]
     print("\n--- Updating Crew's Rank ---")
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
          print("\n--- Searching Crew ---")
          print("1. Search by Name")
          print("2. Search by ID")
          option = input("\nSelect Option: ")

          if option == "1":
               search_names = input("\nEnter Crew's Name: ").title()
               if search_names in current_names:
                    print("\nCrew Found\n")
                    crew_index = current_names.index(search_names)
                    print(F"ID: {current_ids[crew_index]} | Name: {current_names[crew_index]} | Rank: {current_ranks[crew_index]} | Division: {current_divs[crew_index]}")
               else:
                    print("\nNo Crew Found")
               break
          elif option == "2":
               search_id = input("\nEnter Crew's ID: ")
               if search_id in current_ids:
                    print("\nCrew Found\n")
                    crew_index = current_ids.index(search_id)
                    print(F"ID: {current_ids[crew_index]} | Name: {current_names[crew_index]} | Rank: {current_ranks[crew_index]} | Division: {current_divs[crew_index]}")
               else:
                    print("\nNo Crew Found")
               break
          else:
               print("Invalid Input")     
     
     print("\nReturning To Main Menu")
#####################################################################################################################
def filter_by_division(current_names, current_divs):
     name_found = []
     print("\n--- Filter Crew By Division ---\n")

     while True:
          search_div = input(f"Enter Division ['Command', 'Operations', 'Security', 'Sciences']: ").title()

          if search_div == "Command":
               for i in range(len(current_divs)):
                    if search_div == current_divs[i]:
                         name_found.append(current_names[i])
                    else:
                         continue
               break     
          elif search_div == "Operations":
               for i in range(len(current_divs)):
                    if search_div == current_divs[i]:
                         name_found.append(current_names[i])
                    else:
                         continue
               break     
          elif search_div == "Security":
               for i in range(len(current_divs)):
                    if search_div == current_divs[i]:
                         name_found.append(current_names[i])
                    else:
                         continue
               break     
          elif search_div == "Sciences":
               for i in range(len(current_divs)):
                    if search_div == current_divs[i]:
                         name_found.append(current_names[i])
                    else:
                         continue
               break     
          else:
               print("\nInvalid Division\n")

     print(f"\nCrew In {search_div} Division")

     if len(name_found) == 0:
          print("None")
     else:
          for i in range(len(name_found)):
               print(f"{i+1}. {name_found[i]}")

     print("\nReturning To Main Menu")
#####################################################################################################################
def calculate_payroll(current_ranks):
     option_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Cadet"]
     payroll = [1000, 800, 600, 400, 300, 200, 100]
     pay_per_rank = 0
     rank_found = []
     rank_count = []
     total_pay_by_rank = []
     count = 0
     total_pay = 0

     for i in range(len(option_ranks)):
          count = 0
          if option_ranks[i] in current_ranks:
               count = current_ranks.count(option_ranks[i])
               pay_per_rank = payroll[i] * count

               rank_found.append(option_ranks[i])
               rank_count.append(count)
               total_pay_by_rank.append(pay_per_rank)

     for i in current_ranks:
          rank_index = option_ranks.index(i)
          total_pay = total_pay + payroll[rank_index]

     print ("\n--- Total Crew Count ---")
     for i in range(len(rank_found)):
          print(F"{rank_found[i]} - {rank_count[i]} - ${total_pay_by_rank[i]}")

     print(F"\nTotal Payroll = {total_pay}")
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
          
          elif choices == "3":
               filter_by_division(names, divs)

          elif choices == "4":
               add_member(names, ranks, divs, ids)

          elif choices == "5":
               remove_member(names, ranks, divs, ids)
          
          elif choices == "6":
               update_rank(names, ranks, ids)
          
          elif choices == "7":
               calculate_payroll(ranks)

          elif choices == "8":
               count_officers(ranks)
               
          elif choices == "0":
               print("Program Closing Down")
               break
          
          else:
               print("Invalid Input")

main()