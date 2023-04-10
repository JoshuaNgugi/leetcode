# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome(1001))
