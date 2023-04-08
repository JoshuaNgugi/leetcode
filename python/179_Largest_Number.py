class LargerNumKey(str):
    def __lt__(self, y):
        return self + y > y + self


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
