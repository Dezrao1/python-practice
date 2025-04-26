#Creating a code to compute the factorial of different numbers using a loop sequence.
def factorial_loop(num):

    #Calculating the factorial by successively multiplying each number from 1 to num.
    #Initial answer for the factorial of number one is one.
    answer = 1
    for i in range(1,num+1):
        answer *= i

    return answer
#This returns the answer of the factorial of any number.

#Testing the factorial_loop(num) with example cases.
case1 = 2
print(f"Factorial of the number {case1} is {factorial_loop(case1)} ")

case2 = 4
print(f"Factorial of the number {case2} is {factorial_loop(case2)} ")