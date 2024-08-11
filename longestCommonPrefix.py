strs = ["flower", "flow", "floor"]
count = 0
subString = ""
for index, i in enumerate(strs):
    if index == 0:
        string = i
    if len(i) < len(string):
        string = i
for index, i in enumerate(string):
    for j in strs:
        if i == j[index]:
            count += 1
    if count == len(strs):
        subString = subString+i
    else:
        break
    count = 0
print(subString)

# Another Method:
# strs = ["flower", "flow", "floor"]
# subString = ""
# prefix = ""
# count = 0
# string = strs[0]
# for i in string:
#     prefix = prefix + i
#     for j in strs:
#         if j.startswith(prefix):
#             count += 1
#     if count == len(strs):
#         subString = prefix
#         count = 0
#     else:
#         break
# print(subString)