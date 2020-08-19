"""import sys
print(sys.version)
print(sys.version_info)

import datetime
now = datetime.datetime.now
print(now.strftime("%Y:%m:%d %H:%M:%S"))"""

"""'''Write a Python program which accepts the radius of a circle from the user and compute the area.'''
import math '''Or can be written as from math import pi'''
r = float(input("enter the radius of the circle:"))
area = math.pi*r*r
print(area)"""

"""accepts a sequence of comma-separated numbers from user and generate a list and a tuple 
nums = input("enter the list of number seperated by comma:")
list=nums.split(",")
tuple=tuple(list)
print("List:",list)
print("Tuple:",tuple)
"""

"""program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
"""

""" that accepts an integer (n) and computes the value of n+nn+nnn"""
"""n = 5
res, tot = 0, 0
# if n==0:
#    print(0)
for i in range(n):
    res = int(str(res) + str(n))
    print(res)
    tot = tot + res
print(tot)"""

