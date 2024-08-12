s = "   fly me   to   the moon  "
s = s.strip()
length = 0
for index,i in enumerate(s):
    if i != " ":
        length += 1
    else:
        length = 0
print(length)