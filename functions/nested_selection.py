'''
Problem Statement
Try out the below code and make the necessary corrections to get the output as follows:
Airport security cleared
Extra luggage charge is Rs. 600
Please make the payment to clear check-in
'''


passport_status="valid"
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(passport_status=="valid"):
    print("Airport security cleared")
    
    if(ticket_status=="Confirmed"):
        
        if(luggage_weight>0 and luggage_weight<=weight_limit):
            print("Check-in cleared")
            
        elif(luggage_weight<=(weight_limit+10)):
            extra_luggage_charge=300*(luggage_weight-weight_limit)
            
            print("Extra luggage charge is Rs.", extra_luggage_charge)
            print("Please make the payment to clear check-in")
            
        else:
            print("Sorry, ticket is not confirmed")
else:
    print("Invalid passport")