'''function that takes a positive integer and returns the sum of the cube of all the positive integers
smaller than the specified number.
Ex.: 8 = 73+63+53+43+33+23+13 = 784'''

def sum_of_cube(num):
     total=0
     num = num - 1
     while num>0:
         total = total+(num*num*num)
         num = num - 1
     return total

num=21
print('sum of cube of all the numbers is:',sum_of_cube(num))