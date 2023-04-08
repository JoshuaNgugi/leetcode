class Solution:
    # https://leetcode.com/problems/longest-palindrome/solution/
    # def longestPalindrome(self, s):
    #     ans = 0
    #     for v in collections.Counter(s).itervalues():
    #         ans += v / 2 * 2
    #         if ans % 2 == 0 and v % 2 == 1:
    #             ans += 1
    #     return ans
    def longestPalindrome(self, s):
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        ans = sum(
            char_map.pop(c) if value % 2 == 0 else char_map[c] / 2 * 2
            for c, value in char_map.items()
        )
        if char_map:
            ans += 1
        return ans