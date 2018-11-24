# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:57:35 2018

@author: Elev
"""

sum_of_numbers = 0 
print("Now, sum of all numbers is " + str(sum_of_numbers))
for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
    print("Now, i is " + str(i))
    print("Now, sum of all numbers is " + str(sum_of_numbers))
    sum_of_numbers = sum_of_numbers + i

print("The sum of all numbers 1,2,3,4,5,6,7,8,9,10,11,12 is: ")
print(sum_of_numbers)