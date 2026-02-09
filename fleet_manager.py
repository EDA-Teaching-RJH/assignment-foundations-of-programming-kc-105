n = ["Picard", "Riker", "Data", "Worf","Goofy"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Knight"]
d = ["Command", "Command", "Operations", "Security","Operations"]
id = ["001","002","003","004","005"]

characters = [{n:"picard",r:"Captain",d:"Command",id:"001"} 
              {n:"Riker",r:"Commander",d:"Command",id:"002"}
              {n:"Data",r:"Lt. Commander",d:"Operations",id:"003"}
              {n:"Worf",r:"Lieutenant",d:"Security",id:"004"}
              {n:"Goofy",r:"Knight",d:"Operations",id:"005"}
]
init_database() #Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.
    print ("Current List")
    for i in range(len(n))
        
display_menu()#Queries users full name, Prints the options and current student logged in and returns the user's choice.
    
add_member(names, ranks, divs, ids)
        #Validates ID is unique.
        #Validates Rank is a valid TNG rank.
        #Appends data to all 4 lists.
        
remove_member(names, ranks, divs, ids)
    
       #Asks for an ID.
       #Finds the index.
       #Removes the entry from _all 4 lists_ to keep them in sync.
        
update_rank(names, ranks, ids)
    #Finds a member by ID.
    #Updates their rank string.
        
display_roster(names, ranks, divs, ids)`:
    #Iterates through the lists using `range(len(names))`.
    #Prints a formatted table of all crew.
        
search_crew(names, ranks, divs, ids)
    #Asks for a search term.
    #Prints any crew member whose name contains that term.
        
filter_by_division(names, divs)
    #Asks user for "Command", "Operations", or "Sciences".
    #Prints only members in that division using `match` or `if` .
        
calculate_payroll(ranks)
    #Iterates through the ranks list.
    #Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
    #Returns the total cost of the crew.
        
count_officers(ranks) #Counts how many "Captain" and "Commander" ranks exist and returns the integer.