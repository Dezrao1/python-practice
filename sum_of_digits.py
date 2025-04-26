#Creating a code to compute the sum of digits of any number.
def sum_of_digits(n):

    #Shows the sum of digits of n.
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

#Testing the sum_of_digits(n) with example cases.
case1 = 190
print(f"Sum of digits of {case1} is {sum_of_digits(case1)}")

case2 = 74
print(f"Sum of digits of {case2} is {sum_of_digits(case2)}")