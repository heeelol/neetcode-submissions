class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        best = 1
        cur = 1

        for i in range(1, len(nums)):
           if nums[i] != nums[i-1]:
            if nums[i] - nums[i-1] == 1:
                cur += 1
            else:
                best = max(best, cur)
                cur =1

        return max(best, cur)