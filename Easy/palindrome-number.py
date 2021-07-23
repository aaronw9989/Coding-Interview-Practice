# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# One line answer def
# isPalindrome(self, x):
# return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        num = str(x)
        end = len(num) - 1
        print(num[0])

        for start in range(len(num)):
            if start >= end:
                return True
            elif num[start] == num[end]:
                end -= 1
            elif num[start] != num[end]:
                return False