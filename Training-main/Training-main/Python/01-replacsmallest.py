
input_number = input("Enter a number: ")


number_str = input_number
binary_representation = ''
for digit in number_str:
    # Check if the digit is even or odd
    if int(digit) % 2 == 0:
    else:
        binary_representation += '1'  


print(f"The binary representation of {input_number} is: {binary_representation}")