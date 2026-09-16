class Solution:
    def trap(self, height: List[int]) -> int:
        suffix = [0] * len(height)
        prefix = [0] * len(height)

        res = 0

        for i in range(1, len(height)-1):
            if i == 1:
                prefix[i] = height[0]
                continue
            
            prefix[i] = max(prefix[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            if i == len(height) - 2:
                suffix[i] = height[len(height) - 1]
                continue
            
            suffix[i] = max(suffix[i+1], height[i+1])

        for i in range(1, len(height)-1):
            diff = min(prefix[i], suffix[i]) - height[i]

            if diff > 0:
                res += diff
            
        return res