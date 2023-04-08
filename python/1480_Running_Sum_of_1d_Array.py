class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums is None or not nums:
            return nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    # def runningSum(self, nums: List[int]) -> List[int]:
    #     # accumulate method
    #     return accumulate(nums)
