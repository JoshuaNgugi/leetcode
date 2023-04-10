class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        for value in dic.values():
            if value % 2 == 0:
                even += 1
            else:
                odd += 1
        return odd <= 1
