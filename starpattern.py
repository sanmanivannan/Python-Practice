num=4
for i in range(num):
 for j in range(num):
  print('#',end='')
 print('')

num = 4
for i in range(num):
  for j in range(i+1):
   print('#', end='')
  print('')

num=4
for i in range(num):
 for j in range(num-i):
  print('#',end='')
 print('')