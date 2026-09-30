class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # maintain left and right pointers on m
        # loop while left < right
        # middle = (right - left) // 2
        # at matrix[middle], do binary search --> if target lesser than middle_left, shift right pointer to middle. Else if target more than middle_right, shift left pointer to middle

        
        l, r = 0, len(matrix) - 1

        while l <= r:
            middle = l + (r - l) // 2
            middle_l = matrix[middle][0]
            middle_r = matrix[middle][len(matrix[0]) - 1]

            if target < middle_l:
                r = middle - 1
            elif target > middle_r:
                l = middle + 1
            else:
                
                inner_l, inner_r = 0, len(matrix[0]) - 1

                while inner_l <= inner_r:
                    middle_m = inner_l + (inner_r - inner_l) // 2
                    mid_val = matrix[middle][middle_m]

                    if target == mid_val:
                        return True
                    elif target > mid_val:
                        inner_l = middle_m + 1
                    else:
                        inner_r = middle_m - 1
                return False
            
        return False
        