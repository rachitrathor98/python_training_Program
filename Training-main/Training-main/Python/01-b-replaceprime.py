def separate_digits(num):
    digits=[]
    while num>0:
        rem=num%10
        digits.insert(0,rem)
        num=num//10
    return digits

n=int(input('enter a num'))
digits=separate_digits(n)
prime_digits=[2,3,5,7]
ans=0
comman=list(set(digits).intersection(set(prime_digits)))
comman.sort(reverse=True)
for digit in digits:
    if digit in comman:
        ans=ans*10+comman.index(digit)
    else:
        ans=ans*10+digit

print(ans)