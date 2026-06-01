num = int(input('enter:'))
reverse = 0
temp = num
while num != 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10

if temp == reverse:
    print('palindrome')
else:
    print('not palindrome')