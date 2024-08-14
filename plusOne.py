digits = [1,2,3]
num = int("".join(map(str, digits)))
newList = list(str(num+1))
for index,i in enumerate(newList):
    newList[index] = int(i)
print(newList)