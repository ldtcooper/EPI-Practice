# Check if a decimal integer is a palindrome
import math

# def decimal_paliondrome(num: int) -> bool:
#     string_rep = str(num)
#     return string_rep == string_rep[::-1]

def decimal_paliondrome(num: int) -> bool:
    if num < 0:
        return False
    if num < 10:
        return True
    while num > 0:
        # get last digit
        last = num % 10
        # get first digit
        first_mag = 10**int(math.log(num, 10))
        first = num // first_mag
        print(first, last)
        if first != last:
            return False
        # remove first and last digits
        num -= first_mag * first
        num = (num - last) // 10
    return True
        
        
        

cases = [0, 1, 7, 11, 121, 333, 2147447412, -1, 12, 100, 1234567]
answers = [True, True, True, True, True, True, True, False, False, False, False]
for i in range(len(cases)):
    print(cases[i], decimal_paliondrome(cases[i]) == answers[i])
