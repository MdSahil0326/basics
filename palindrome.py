Given an integer x, return true if x is a 
palindrome
, and false otherwise.
class Solution:
    def isPalindrome(self, x):
        # Convert the integer to a string
        x_str = str(x)
        # Check if the string is the same forwards and backwards
        return x_str == x_str[::-1]
