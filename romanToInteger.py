s = "MMMCCCXXXIII"
num = 0
excep = ""
prev = 0

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

for i in s:
    excep = excep + i
    if len(excep) > 2:
        excep = list(excep)
        excep.pop(0)
        excep = "".join(map(lambda x:x, excep))
    
    if excep == "IV":
        num -= prev
        num += V - I
    elif excep == "IX":
        num -= prev
        num += X - I
    elif excep == "XL":
        num -= prev
        num += L - X
    elif excep == "XC":
        num -= prev
        num += C - X
    elif excep == "CD":
        num -= prev
        num += D - C
    elif excep == "CM":
        num -= prev
        num += M - C
    else:
        if i == "I":
            num += I
            prev = I
        elif i == "V":
            num += V
            prev = V
        elif i == "X":
            num += X
            prev = X
        elif i == "L":
            num += L
            prev = L
        elif i == "C":
            num += C
            prev = C
        elif i == "D":
            num += D
            prev = D
        elif i == "M":
            num += M
            prev = M
print(num)