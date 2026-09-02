class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        post = 1

        for i in range(1, length):
            res[i] = (res[i-1] * nums[i-1])

        for i in range(length-2, -1, -1):
            post *= nums[i+1]
            res[i] = post * res[i]

        return res 
