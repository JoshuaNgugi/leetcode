class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        return len(temp[-1]) if temp else 0