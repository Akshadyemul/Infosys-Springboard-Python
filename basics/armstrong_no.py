num = int(input('enter num:'))
sum = 0
temp = num
while temp != 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10

if sum == num:
    print('it is armstrong num')
else:
    print('it is not armstrong num')