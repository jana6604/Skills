# Find the largest and smallest numbers in a list.

n = int(input("Enter a number:"))

numbers = []

for i in range(n) :
    element = input(f"The Element {i+1} :")
    numbers.append(element)

largest = max(numbers)
smallest = min(numbers)

print(f"The largest number is {largest} and smallest number is {smallest} ")
