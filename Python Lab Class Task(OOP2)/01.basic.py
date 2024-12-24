#TITAS SARKER
#a_Math_Formula
"""
Create a function that will take 2 inputs from keyboard and perform the following formula:
    (a+b)^2 = a^2 + b^2 + 2ab
take input (a,b)
return a^2 + b^2 + 2ab
"""

def formula(a,b):
    return a**2 + b**2 + 2*a*b

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print (f"(a+b)^2 = a^2 + b^2 + 2ab = {formula(a,b)}")


#b_ Math_Formula_With_Lambda
"""
(a+b)^2 = a^2 + b^2 + 2ab
Use lambda function to perform above formula
"""

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
square_formula = lambda a, b: a**2 + b**2 + 2*a*b
print(f"Result: {(a + b)**2} = {square_formula(a, b)}")

#c _Recursion_Tragedy

"""
Define a recursion function that return the factorial of a number
Example: n -> Take input
perform n!
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")

#d_Prime_Or_Not
"""
Create a function that will find the number is prime or not
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")