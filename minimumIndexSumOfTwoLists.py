list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
comStrInOfL1 = []
comStrInOfL2 = []
for index, i in enumerate(list1):
    if i in list2:
        comStrInOfL1.append(index)
        comStrInOfL2.append(list2.index(i))
sumOfComStrInOfL = []
i = 0
while i < len(comStrInOfL1):
    sumOfComStrInOfL.append(comStrInOfL1[i]+comStrInOfL2[i])
    i += 1
inOfComStr = [comStrInOfL1[0]]
smallest = sumOfComStrInOfL[0]
for index, i in enumerate(sumOfComStrInOfL):
    if i < smallest:
        smallest = i
        inOfComStr.pop()
        inOfComStr.append(comStrInOfL1[index])
    elif i == smallest:
        if index == 0:
            inOfComStr.pop()
        smallest = i
        inOfComStr.append(comStrInOfL1[index])
comStr = []
for i in inOfComStr:
    comStr.append(list1[i])
print(comStr)