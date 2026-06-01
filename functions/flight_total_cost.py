'''
Problem Statement
The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: 
Rate per Adult: Rs. 37550.0 
Rate per Child: 1/3rd of the rate per adult 
Service Tax: 7% of the ticket amount (including all passengers) 
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.
'''

#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    ticket_per_adult = 37550
    ticket_per_child = ticket_per_adult / 3
    
    ticket_cost = (no_of_adults * ticket_per_adult) + (no_of_children * ticket_per_child)
    
    service_tax = ticket_cost * (7/100)
    total_cost = ticket_cost + service_tax
    
    discount = total_cost * (10/100)
    total_ticket_cost = total_cost - discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)