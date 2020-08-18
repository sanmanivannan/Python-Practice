def findodd(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if i!=j:
                product = num[i]*num[j]
                if product & 1:
                    return True
                    return False



num=[2,3,4,5,6]
print(findodd(num))