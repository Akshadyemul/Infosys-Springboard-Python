#lex_auth_01269363490743091290

def display(num):
    message=""
    #write your logic here
    if num % 3 ==0 and num % 5==0:
        print('Zoom')
    elif num % 5 ==0:
        print('Zap')
    elif num % 3==0:
        print('Zip')
    else:
        print('Invalid')
    return message

#Provide different values for num and test your program
message=display(9)
print(message)