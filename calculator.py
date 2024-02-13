import math

print("Operations:")
print("1. Square Root")
print("2. Factorial")
print("3. Natural Logarithm")
print("4. Power of")
operation = int(input())

if operation == 1:
    x = int(input("Enter the number: "))
    print(math.sqrt(x))
elif operation == 2:
    x = int(input("Enter the number: "))
    print(math.factorial(x))
elif operation == 3:
    x = int(input("Enter the number: "))
    print(math.log(x))
elif operation == 4:
    x = int(input("Enter the number: "))
    b = int(input("Enter the power: "))
    print(x**b)

