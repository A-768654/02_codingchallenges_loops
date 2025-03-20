#-----------------------------------------------------------------------------
# Name:        Sum of Numbers
# Purpose:     Write a program that asks the user for a number `n` and calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      Aleeza Siddiqui
# Created:     5-Mar-2025
#-----------------------------------------------------------------------------

num = int(input("Enter a number: "))
sum = 0

#Use for loop to calculate sum
for i in range(0, num + 1):
    sum += i
#print answer
print("Sum =", sum)