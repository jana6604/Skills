# Write a Python program to check if a number is even or odd.

try :
    number = int(input("Enter a number : "))

    if (number % 2 == 0) :
       print(f" The number {number} is even ")
    else :
       print(f" The number {number} is odd ")

except ValueError :
   print(" Invalid Input! please enter a integer..")
