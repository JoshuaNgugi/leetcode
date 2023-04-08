class Solution:
    def reverse(self, x):
        # https://leetcode.com/problems/reverse-integer/
        flag = x < 0
        if flag:
            x = -x
        x = str(x)[::-1]

        if flag:
            x = f"-{x}"

        value = 2 ** 31
        x = int(x)
        return x if -value <= x < value else 0
    
