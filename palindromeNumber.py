def listReverser(_list):
    reversedList = []
    for i in range(len(_list)-1, -1, -1):
        reversedList.append(_list[i])
    return reversedList
x = 121
x = str(x)
listOfX = list(x)
y = "".join(map(lambda x:x,listReverser(listOfX)))
if x == y:
    print(True)
else:
    print(False)