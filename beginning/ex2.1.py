#!/usr/bin/env python3.6
#########################
#
#	play with 2 integers you get from user input
#
#########################

num1 = input("Enter an integer: ")
num2 = input("Enter another integer: ")
print ("You entered the integers "+num1+" and "+num2)
#summing the two numbers:
sum = int(num1) + int(num2)
print ("their sum is "+str(sum))
#multiplying the two numbers:
mul = int(num1) * int(num2)
print ("their multiplication is "+str(mul))
#dividing the two numbers:
div = int(num1) / int(num2)
print ("dividing them equal "+str(div))
#checking is equal and printing the bigger one if not
if num1 == num2:
 print("The numbers are equal")
elif num1 > num2:
 print(num1+" is bigger than "+num2)
else:
 print(num2+" is bigger than "+num1)
