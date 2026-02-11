def init_database():
    global n,r,d,idn

    n = ["Picard", "Riker", "Data", "Worf","Goofy"]#Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]#rank
    d = ["Command", "Command", "Operations", "Security","Operations"]#division
    idn = ["001","002","003","004","005"]#idnumber
    return [n,r,d,idn]
    #characters = dict(zip(n,r,d,idn))
               # [character(n="picard",r="Captain",d="Command",id="001")
               # character(n="Riker",r="Commander",d="Command",id="002")
                #character(n="Data",r="Lt. Commander",d="Operations",id="003")
                #character(n="Worf",r="Lieutenant",d="Security",id="004")
               # character(n="Goofy",r="Ensign",d="Operations",id="005")]

def display_menu():#Queries users full name, Prints the options and current student logged in and returns the user's choice.
    init_database()
    count = 0
    while True:
        if count == 0: 
            currentuser = input("Please Enter Full Name")
        count = count + 1
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
            case "1":
                display_roster()
            case "2":
                add_member()
            case "3":
                remove_member()
            case "4":
                update_rank()
            case "5":
                display_roster()
            case "6":
                search_crew()
            case "7":
                filter_by_division()
            case "8":
                calculate_payroll()
            case "9":
                count_officers()
            case "0":
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
    for _ in idn:#for loop for validation
        new_id = input("ID:")#Validates ID is unique.
        if new_id not in idn:
            idn.append(new_id)
            print("Crew member added.")
            break
        else:  
            print("Please enter valid id")
               
def remove_member():
    for _ in idn:#for loop for validation
        removal_id = input("Please enter ID of Character to be removed :")#Asks for an ID.
        if removal_id in idn:
            xid = idn.index(removal_id)#Finds the index.
            n.pop(xid)
            r.pop(xid)
            d.pop(xid)
            idn.pop(xid)#Removes the entry from _all 4 lists_ to keep them in sync.
            print("Removed.")
            break
        else:  
            print("Please enter valid id")
     
def update_rank():
    while True:
        update = input("Please enter ID of Character to be Updated :")
        if update in idn:
            newrank = str(input("PLease enter a new Rank "))
            for i in range(len(idn)):#Finds a member by ID.
                if idn[i] == update:
                    r[i] = newrank #Updates their rank string.
                    print ("rank updated")
            break
        else:
            print("Please enter valid id")
        
def display_roster():
    print ("Current Roster")
    for i in range(len(n)):#Iterates through the lists using `range(len(names))
        print("Name: ",n[i]," Rank: ",r[i]," Division: ",d[i]," ID: ", idn[i])#Prints a formatted table of all crew.
            
def search_crew():
    count = 0
    while True:
        searchterm = input("Please enter a search term :")#Asks for a search term.
        for i in range(len(n)):
            if searchterm in n[i]:
                print("Name: ",n[i]," Rank: ",r[i]," Division: ",d[i]," ID: ", idn[i])#Prints any crew member whose name contains that term
                count = count + 1
        if count == 0:
            print("No names with term: ", searchterm)
            break
        else:
            break

def filter_by_division():
    count = 0
    while True:
        division_name = input("Please enter the Division (Command, Operations, Sciences):")#Asks user for "Command", "Operations", or "Sciences"
        if division_name == "Command" or division_name == "Operations" or division_name == "Sciences":
            print("Current members in ", division_name)
            for i in range(len(d)):
                if d[i] == division_name:#Prints only members in that division using `match` or `if` .
                    print(n[i])
                    count += 1 
            if count == 0:
                print("no members in ", division_name)
                break
            break
        else:
            print("Division name not valid")   
            break
        
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


display_menu()