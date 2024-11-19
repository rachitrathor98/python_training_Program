RR = int(input("enter a number: "))
digits = []
while RR > 0:
    meme = RR % 10
    digits.insert(0, meme)
    RR = RR // 10

divideby3 = 0
divideby5 = 0

for i in digits:
    if i % 3 == 0: 
        divideby3 += 1
    elif i % 5 == 0:  
        divideby5 += 1

print(abs(divideby3))  