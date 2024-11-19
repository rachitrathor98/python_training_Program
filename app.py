def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)



The while True loop ensures the function keeps asking for valid input until the user provides it.
The try block attempts to convert the user input to an integer.
If the input is not a valid integer, a ValueError is raised, and the except block prints an error message and asks again.





