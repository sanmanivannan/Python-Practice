'''even or odd
to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
'''

num = int(input('enter a number:'))
if num%2==0:
    print("entered number:",num,"is a even number")
else:
    print("entered number:",num,"is a odd number")