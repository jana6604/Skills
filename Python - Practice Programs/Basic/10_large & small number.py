# Find the largest and smallest numbers in a list.

n = int(input("Enter a number:"))

list = []

for i in range(n) :
    element = input(f"The Element {i+1} :")
    list.append(element)

largest = max(list)
smallest = min(list)

print(f"The largest number is {largest} and smallest number is {smallest} ")