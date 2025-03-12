# Check if a number is prime.

def check_prime(num):
    if num <= 1:
        return f"{num} is not a Prime Number"

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return f"{num} is not a Prime Number"
    return f"{num} is a Prime Number"
    
num = int(input("Enter a number:"))
print(check_prime(num))

        