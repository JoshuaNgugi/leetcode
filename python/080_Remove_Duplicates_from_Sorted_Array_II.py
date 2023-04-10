class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        length = len(nums)
        result = 0
        i = j = 0
        while i < length:
            j = i
            while j < length and nums[j] == nums[i]:
                j += 1
            if j-i > 2:
                length -= j-i-2
                for _ in range(j-i-2):
                    del nums[i]
                result += 2
                j = i+2
            else:
                result += (j-i)
            i = j
        return result


