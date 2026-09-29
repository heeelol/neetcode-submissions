class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for i in range(len(position)):
            stack.append([position[i], speed[i]])

        stack.sort(key = lambda x : x[0], reverse = False)

        res = 1

        timeCurr = (target - stack[-1][0]) / stack[-1][1]
        
        while len(stack) > 1:
            stackP, stackS = stack.pop()

            timeNext = (target - stack[-1][0]) / stack[-1][1]

            if timeCurr >= timeNext:
                continue
            else: 
                timeCurr = timeNext
                res += 1
        
        return res
