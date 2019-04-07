#!/usr/bin/env python3.6
##########################
#
# Write a function called add which recieves 2 numbers returns their sum
# Write a func called mul which recieves 2 numbers returns their multiplication using function add
#
##########################

#function add
def Add(x,y):
    sum1=sum([x,y])
    return sum1

#function mul
def Mul(x,y):
    mul1=0
    for i in range(y):
        mul1=Add(mul1,x)
    return mul1

#test
print(Mul(5,125))
