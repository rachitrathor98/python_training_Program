num = input("Enter a number: ")

# Convert the number to a string to iterate through each digit
num_str = num
binary_representation = ''

# Iterate through each digit in the number
for digit in num:
  
    if int(digit) % 2 == 0:
        binary_representation += '0' 
    else:
        binary_representation += '1'  


print(f"The binary representation of {num} is: {binary_representation}")