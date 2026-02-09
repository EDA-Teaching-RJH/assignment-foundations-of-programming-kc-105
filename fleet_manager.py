def init_database() #Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.
    n = ["Picard", "Riker", "Data", "Worf","Goofy"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Knight"]
    d = ["Command", "Command", "Operations", "Security","Operations"]
    id = ["001","002","003","004","005"]

    characters = [{n:"picard",r:"Captain",d:"Command",id:"001"} 
                {n:"Riker",r:"Commander",d:"Command",id:"002"}
                {n:"Data",r:"Lt. Commander",d:"Operations",id:"003"}
                {n:"Worf",r:"Lieutenant",d:"Security",id:"004"}
                {n:"Goofy",r:"Knight",d:"Operations",id:"005"}]


def display_menu()#Queries users full name, Prints the options and current student logged in and returns the user's choice.
    if currentuser == "":
        currentuser = input("Please Enter Full Name")
    
    print("\n--- MENU ---")
    print("Welcome ", currentuser)
    print("1. View Database")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Display Roster")
    print("6. Search Crew")
    print ("7.Search Division")
    print("8. Payroll")
    print("9. Count Officers")
    print("0. Exit")

def add_member()
        print ("please enter the information of the new character")
        new_name = input("Name: ")
        n.append(new_name)
        new_rank = input("Rank: ")
        r.append(new_rank)
        new_div = input("Division: ")
        d.append(new_div)
        while true:
            new_id = input("ID:")
            for _ in id:
                 if new_id not in id:
                      id.append(newid)
                      break
            return
        print("Crew member added.")
        #Validates ID is unique.
        #Validates Rank is a valid TNG rank.
        #Appends data to all 4 lists.
        
def remove_member()
    removalid = input("Please enter ID of Character to be removed :")#Asks for an ID.
    xid = n.index(removalid)#Finds the index.
    n.pop(xid)
    r.pop(xid)
    d.pop(xid)
    id.pop(xid)#Removes the entry from _all 4 lists_ to keep them in sync.
    print("Removed.")
        
def update_rank()
    update = input("Please enter ID of Character to be Updated :")
    newrank = input("PLease enter a new Rank ")
    updid = id.index(update)#Finds a member by ID.
    r(updid)= newrank #Updates their rank string.
    
   
        
def display_roster()
    #Iterates through the lists using `range(len(names))`.
    #Prints a formatted table of all crew.
        
def search_crew()
    #Asks for a search term.
    #Prints any crew member whose name contains that term.
        
def filter_by_division()
    #Asks user for "Command", "Operations", or "Sciences".
    #Prints only members in that division using `match` or `if` .
        
def calculate_payroll()
    #Iterates through the ranks list.
    #Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
    #Returns the total cost of the crew.
        
def count_officers() #Counts how many "Captain" and "Commander" ranks exist and returns the integer.