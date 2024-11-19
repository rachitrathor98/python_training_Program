RR=int(input("enter a number "))
digits=[]
while RR > 0:
    rem= RR % 10  
    digits.insert(0,rem) 
    RR=RR//10 
sum=0
for i in range (len(digits)-1):
    sum=sum+(abs(digits[i]-digits[i+1]))
    
    
print(sum)


    



