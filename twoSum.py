testList = [3,2,4]
target = 6
indices = []
def twoSum(testList, target):
    for i, num1 in enumerate(testList):
        for j, num2 in enumerate(testList):
            if j > i:
                if num1 + num2 == target:
                    return [i,j]
indices = twoSum(testList, target)
print(indices)