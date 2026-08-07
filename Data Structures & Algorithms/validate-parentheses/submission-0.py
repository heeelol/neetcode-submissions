class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(' : ')', '[' : ']', '{' : '}'}

        for i in s:
            if i in pair:
                stack.append(i)
            else: 
                if stack:
                    popped = stack.pop()
                else:
                    return False
                
                if pair[popped] != i:
                    return False

        if stack:
            return False
        else:
            return True
                
            
