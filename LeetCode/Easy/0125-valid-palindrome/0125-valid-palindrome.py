import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        s = re.sub('[^a-z0-9]*', '', s)

        is_palindrome = True
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                is_palindrome = False
                break
        
        return is_palindrome