class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # https://en.wikipedia.org/wiki/Happy_number
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x)**2, list(str(n))))
        return n == 1