class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) 
            second = heapq.heappop(stones) 

            if first != second:
                heapq.heappush(stones, first - second)


        return stones[0] * -1 if stones else 0

