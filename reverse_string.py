#Creating a code to compute the reverse of a string (without using [::-1] or built-in methods).
def reverse_string(s):
    #There is no string yet hence there is no reverse_string.
    reversed_str = ''

    #Reverse the string by building it character by character starting from the last character.
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
#Testing the reverse_string(s) with example cases.
case1 = "Elon"
print(f"Reversed string is {reverse_string(case1)}")

case2 = "Musk"
print(f"Reversed string is {reverse_string(case2)}")