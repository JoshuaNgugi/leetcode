class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_s = [t.lower() for t in s if t.isalnum()]
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls / 2
        return all(alnum_s[i] == alnum_s[ls - 1 - i] for i in range(mid))