#Creating a code to differentiate between odd and even numbers.
def check_even_or_odd(num):
    #This is a loop sequence used to determine even or odd numbers using divisibility by 2.
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    #This returns the solution as either even or odd.

 #Testing the check_even_or_odd(num) with example cases.
case1 = 19
print(f"The number {case1} is {check_even_or_odd(case1)}")

case2 = 74
print(f"The number {case2} is {check_even_or_odd(case2)}")