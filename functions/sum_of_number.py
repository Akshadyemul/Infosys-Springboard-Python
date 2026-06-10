'''
Problem Statement
Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6
Note: Initialize the number with various values and test your program.
'''

#lex_auth_012693749623193600122

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    l = tuple(number)

    sum_of_digits += l

    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          