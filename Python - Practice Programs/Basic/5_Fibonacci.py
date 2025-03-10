# Print the Fibonacci sequence up to n terms.

num = int(input("Enter the number of terms:"))
first_no = 0
second_no = 1

print(f"The Fibonacci Sequence up to {num} terms : ")

for i in range(num) :
    print(first_no, end=" ")
    next_no = first_no + second_no
    first_no = second_no
    second_no = next_no