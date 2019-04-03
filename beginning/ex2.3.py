#!/usr/bin/env python3.6
#########################
#
#	create array of 3 strings which are user's input. play with the array
#
#########################

#creating the array
arr = []
arr.append(input("Enter 3 strings: "))
arr.append(input())
arr.append(input())
print(arr)

#replacing 1st and 3rd items in array
tmp = arr[0]
arr[0] = arr[2]
arr[2] = tmp
print(arr)
#replacing 2nd item with other array of 3 numbers
arr[1] = []
arr[1].append(input("Enter 3 numbers: "))
arr[1].append(input())
arr[1].append(input())
print(arr)
#print the 2nd number in the inner array
print(arr[1][1])
