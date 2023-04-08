class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = upper + 1 if i == len(nums) else nums[i]
            if curr - prev > 2:
                ranges.append("%d->%d" % (prev + 1, curr - 1))
            elif curr - prev == 2:
                ranges.append("%d" % (prev + 1))
            prev = curr
        return ranges