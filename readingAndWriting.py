'''Reading/Writing Files
1. File input.txt contains numbers separated by comma as shown below,
6,8
7,6
2,8
9,5
9,6
a. Write a function countNum(file_name,num) such that it returns number of
occurrences of a number in that file. for example,
countNum(“input.txt”,9) should return 2
countNum(“input.txt”,100) should return 0
Answer:'''
def countNum(file_path, num):
 count = 0
 with open(file_path,"r") as f:
 for line in f.readlines():
 tokens = line.split(",")
 count += count_num_in_tokens(tokens, num)
 return count
def count_num_in_tokens(tokens, num):
 count = 0
 for token in tokens:
 if num == int(token):
 count+=1
 return count
c = countNum("C:\\Code\\Py\\Basics\\input.txt",9)
print("count: ",c)


'''b. Change input.txt so that when program ends it contains sum of all numbers in a line
as shown below,
6,8,sum: 14
7,6,sum: 13
2,8,sum: 10
9,5,sum: 14
9,6,sum: 15
Answer:'''
def sum_numbers(file_path):
 output_lines = []
 with open(file_path,"r") as f:
 for line in f.readlines():
 tokens = line.split(",")
 total = sum_tokens(tokens)
 output_lines.append("sum: " + str(total) + " | " + line)
 with open(file_path,"w") as f:
 f.writelines(output_lines)
def sum_tokens(tokens):
 sum = 0
 for token in tokens:
 sum += int(token)
 return sum
sum_numbers("C:\\Code\\Py\\Basics\\input.txt")