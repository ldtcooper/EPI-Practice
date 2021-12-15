# Chapter 4
## Problem 9: Decimal Palindrome
This problem asks us to find out if a given integer is a palindrome, i.e. if it is the same number forwards and backwards. For example:

- 1 is a palindrome
- -1 is not a palindrome
- 121 is a palindrome
- 123 is not

Right away, we can see that any negative number is not a palindrome, so if we see one of those, we can return `False` immediately. Similarly, if we see a positive single digit number, we know it is a palindrome, and can return true immediately.

Then things get harder. We can go the 'brute force' way of turning the number into a string, then iterating through it, but this takes `O(n)` time to convert, and either `O(n)` time or `O(n)` space to check, so lets do it another way.

We can use some properties of the number itself to get the first and last digits and compare them as we whittle the number away.

The last digit is easy: `n % 10` gives that to us. The first digit is harder since we need to use logarithms. By taking $log_{10}(n)$ we get the power we need to raise 10 to to get our integer. Unless n is an exact power of 10, this is going to be a float, so we round it with `int` and raise 10 to this power to give ourselves the largest place value in the number, e.g. 123's largest place value is the hundreds, so this method gives us 100.

We can then divide our number by this place value using integer division (`//`) which will give us the number of times our number goes evenly into its largest place value. For example, 999's largest place value is 100, so `999 // 100 = 9`. This is the first digit.

We can compare these values and if they are equal, we can move on to the next pair of numbers, but how do we get rid of the pair we just found?

To get rid of the first, we just multiply the first digit by its place value and subrtact that from our number, e.g. `999 - (9 * 100) = 999 - 900 = 99`

We can then take that result, subtract the last digit, and divide by 10: `99 - 9 = 90`, `90 // 10 = 9`.

Thus, we get 9 and can repeat this process until we whittle down our original number to something 0 or smaller.
