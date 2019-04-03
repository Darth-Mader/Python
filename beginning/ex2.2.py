#!/usr/bin/env python3.6
#########################
#
#	get user input for 2 strings and a number between 1 and 3. build manipulations with the input
#
#########################

str1 = input("Insert a string: ")
str2 = input("Insert another string: ")
num1 = input("Enter an integer between 1 and 3: ")
print("##############")
#checking which string is longer

len_str1 = len(str1)
len_str2 = len(str2)
if len_str1 == len_str2:
 print("The strings are equal in length")
 short = str1
 long = str2
elif len_str1 > len_str2:
 print("The string '"+str1+"' is longer than the string '"+str2+"'")
 long = str1
 short = str2
else:
 print("The string '"+str2+"' is longer than the string '"+str1+"'")
 long = str2
 short = str1

#check if the shorter string exists in the longer
if short in long:
 print("The string '"+short+"' exists in '"+long+"'")

#print first 1-3 chars of the longer string, decided by what the user inputed at the beginning 
print("The first "+num1+" character of '"+long+"' are '"+long[:int(num1)]+"'")

#replace all the occurences of the first char of the short string in the long string with your name
name = input("kimi no namae wa? ")
first_short = short[:1]
