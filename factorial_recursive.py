#Creating a code to compute a Factorial (Recursive).
def factorial_recursive(n):

    #If n is 0 or 1, return 1; otherwise multiply n by the factorial of (n-1).
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

#Testing the factorial_recursive(n) with example cases.
case1 = 2
print(f"Factorial of the number {case1} is {factorial_recursive(case1)} ")

case2 = 4
print(f"Factorial of the number {case2} is {factorial_recursive(case2)} ")