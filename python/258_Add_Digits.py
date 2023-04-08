class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https: // en.wikipedia.org / wiki / Digital_root
        return num if num < 10 else num - ((num - 1) / 9) * 9