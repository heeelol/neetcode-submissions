class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevIndex = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevIndex:
                return [prevIndex[diff], i]

            prevIndex[val] = i

        return