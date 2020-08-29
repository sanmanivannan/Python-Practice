with open("D:\\Learning\\Python\\test.txt","r") as f:
 with open("D:\\Learning\\Python\\test1.txt", "w") as f_out:
  for line in f:
    token = line.split(" ")
    f_out.write("number of words:" + "  " +  str(len(token)) + "  " +  line)
