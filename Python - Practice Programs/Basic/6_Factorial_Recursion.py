# Find the factorial of a number using recursion.

def factorial(num) :
    if num < 0 :
        print("Factorial is undefined for negative numbers.")
    elif num == 0 or num == 1 :
        return 1
    else :
        return num*factorial(num-1)
    
num = int(input("Enter a non-negative number :"))
print(f"The factorial of a number {num} is {factorial(num)}")