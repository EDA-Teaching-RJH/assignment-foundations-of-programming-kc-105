def init_database():
    n = ["Picard", "Riker", "Data", "Worf","Goofy"]#Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    d = ["Command", "Command", "Operations", "Security","Operations"]
    idn = ["001","002","003","004","005"]

    characters = dict(zip(n,r,d,idn))
               # [{n:"picard",r:"Captain",d:"Command",id:"001"} 
               # {n:"Riker",r:"Commander",d:"Command",id:"002"}
                #{n:"Data",r:"Lt. Commander",d:"Operations",id:"003"}
                #{n:"Worf",r:"Lieutenant",d:"Security",id:"004"}
               # {n:"Goofy",r:"Ensign",d:"Operations",id:"005"}]


def display_menu():#Queries users full name, Prints the options and current student logged in and returns the user's choice.
    while true:
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
            
        opt = input("Select option: ")
        match opt:
            case 1:
                display_roster
            case 2:
                add_member
            case 3:
                remove_member
            case 4:
                update_rank
            case 5:
                display_roster
            case 6:
                search_crew
            case 7:
                filter_by_division
            case 8:
                calculate_payroll
            case 9:
                count_officers
            case 0:
                print("Shutting down.")
                break
            case _:
                print ("please enter a valid option")   

def add_member():
        print ("please enter the information of the new character")
        new_name = input("Name: ")
        n.append(new_name)#Appends data to all 4 lists.
        new_rank = input("Rank: ")
        r.append(new_rank)#Validates Rank is a valid TNG rank.
        new_div = input("Division: ")
        d.append(new_div)
        while true:
            new_id = input("ID:")#Validates ID is unique.
            for _ in idn:
                 if new_id not in idn:
                      idn.append(new_id)
                      break
            return
        print("Crew member added.")   
        
def remove_member():
    removalid = input("Please enter ID of Character to be removed :")#Asks for an ID.
    xid = n.index(removalid)#Finds the index.

    n.pop(xid)
    r.pop(xid)
    d.pop(xid)
    idn.pop(xid)#Removes the entry from _all 4 lists_ to keep them in sync.
    print("Removed.")
        
def update_rank():
    update = input("Please enter ID of Character to be Updated :")
    newrank = str(input("PLease enter a new Rank "))
    #Finds a member by ID.
    for i in range(idn):
        if idn(i) == update:
            r[i] = newrank #Updates their rank string.
    
   
        
def display_roster():
    print ("Current Roster")
    for i in range(len(n)):#Iterates through the lists using `range(len(names))
        print("Name: ",n(i)," Rank: ",r(i)," Division: ",d(i)," ID: ", idn(i))#Prints a formatted table of all crew.
    
    
        
def search_crew():
    count = 0
    while count > 0:
        searchterm = input("Please enter a search term :")#Asks for a search term.
        for i in range(len(n)):
            if searchterm in n(i):
                print("Name: ",n(i)," Rank: ",r(i)," Division: ",d(i)," ID: ", idn(i))#Prints any crew member whose name contains that term
                count = count + 1
        if count == 0:
            print("No names with term: ", searchterm)

def filter_by_division():
    divisionname = input("Please enter the Division (Command, Operations, Sciences):")#Asks user for "Command", "Operations", or "Sciences"
    print("Current members in ", divisionname)
    for i in d:
        if d(i) == divisionname:#Prints only members in that division using `match` or `if` .
            print(n(i))
    
        
def calculate_payroll():
    print ("current payroll: ")
    payroll = 0
    for i in r:#Iterates through the ranks list.
        match r: #Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
            case "Captain":
                payroll = payroll+ 1000
            case "Commander":
                payroll = payroll+ 750
            case "Lt. Comancer":
                payroll = payroll+ 500
            case "Lietenant":
                payroll = payroll+ 400
            case "Ensign":
                payroll = payroll+ 200
    print (payroll)#Returns the total cost of the crew.
        
def count_officers():
    count = 0
    for rank in r: 
        if rank == "Captain" or rank =="Commander": 
            count = count + 1
            print(f"There are {count} High ranking officers") #Counts how many "Captain" and "Commander" ranks exist and returns the inte

init_database()
display_menu()