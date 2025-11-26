# First 10 Fibonacci Numbers
# Fibonacci Series?

# Each number is the sum of the previous two numbers.

# Starts with 0 and 1.

# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...




# Initialize the first two numbers
a, b = 0, 1

print("First 10 Fibonacci numbers:")

for i in range(10):
    print(a, end=" ")  # print current number
    a, b = b, a + b    # update a and b for next number



a,b = 0,1

print("enter a fibonacci numbers from 1 to 10:")

for i in range(1,11):
    print(a, end= " ")
    a,b = b, a + b



    # Print Fibonacci series up to N terms
a,b = 0,1
num = int(input("enter a number:"))

for i in range(1,num+1):
    print(a, end="")
    a,b=b,a+b
