sum = 0
choice = 'yes'
while choice == 'yes':
    num = int(input('enter no:'))
    if num%4==0:
        sum += num

    choice = input('do you want to continue')
    
print(sum)