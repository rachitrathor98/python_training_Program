def getvalidNum(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print(getvalidNum('Enter a number: '))
