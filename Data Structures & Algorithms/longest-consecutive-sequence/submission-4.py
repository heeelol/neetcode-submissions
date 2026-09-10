class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new = set(nums)
        curr, best = 1, 1

        for num in new:
            prev = num - 1
            next = num + 1

            if prev in new:
                continue
            
            while next in new:
                curr += 1
                next += 1
                best = max(curr, best)

            curr = 1

        return best





