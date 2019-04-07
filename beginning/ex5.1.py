#!/usr/bin/env python3.6
#######################
#
# write a program that defines a function which receives two parameters:
# an array and a number
#
#######################

def funk(x,y):
    #print array sum
    sum1=str(sum(x))
    print("Array's sum is "+sum1)
    #return true if number is greater than array length, false if not
    if y > len(x):
        return True
    else:
        return False

#check the script
print(funk([1,2,3],1))
print(funk([1,2,3123213123],5))
