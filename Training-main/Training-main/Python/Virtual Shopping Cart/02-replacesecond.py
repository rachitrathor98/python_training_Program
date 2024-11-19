num = int(input('Enter a number: '))  
s
digits = []  


while num > 0:
    rem = num % 10  
    digits.insert(0, rem)  #
    num = num // 10  


ans = 0


for next_digit in digits:
    ans = ans * 10 + next_digit  

print("Output the result:", ans) 