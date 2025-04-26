#Creating a code of the sum of all elements in a list.
def sum_list(elements):
    #Initial sum is zero.
    sum = 0

    # Add each item (num) in 'elements' to 'sum'.
    for num in elements:
        sum += num

#This returns the sum.
    return sum

#Testing the sum_list with example cases.
case1 = [2, 4, 6, 8, 10]
print("sum: ", sum_list(case1))

case2= [3, 5, 7,11]
print("sum: ", sum_list(case2))