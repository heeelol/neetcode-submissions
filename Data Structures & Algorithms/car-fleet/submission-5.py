class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for i in range(len(position)):
            stack.append([position[i], speed[i]])

        stack.sort(key = lambda x : x[0], reverse = False)

        res = 1

        startP, startS = stack.pop()
        timeCurr = (target - startP) / startS
        
        while len(stack) > 0:
            nextP, nextS = stack.pop()

            timeNext = (target - nextP) / nextS

            if timeCurr >= timeNext:
                continue
            else: 
                timeCurr = timeNext
                res += 1
        
        return res
