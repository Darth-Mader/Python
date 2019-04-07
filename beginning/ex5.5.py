#!/usr/bin/env python3.6
#########################
#
# Write a function that recieves a power of 2 and print all the halves in recursion
#
#########################

#function definition:
def recurs(x):
    int(x)
    print(x)
    if x != 1:
        recurs(x//2)

#test 
recurs(32)
