s = "[{()()}]"
paren = ["()", "{}", "[]"]
def removePairs(s):
    for i in paren:
        s = s.replace(i,"")
    return s
while "()" in s or "{}" in s or "[]" in s:
    s = removePairs(s)
if s == "":
    print(True)
else:
    print(False)