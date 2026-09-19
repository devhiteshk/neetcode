class Solution:
    def maxArea(self, x: List[int]) -> int:
        i = 0
        j = len(x)-1
        res = -float('inf')

        while i < j:
            res = max( (j-i)*min(x[i],x[j]), res )

            if x[j] < x[i]:
                j -= 1
            
            else:
                i += 1

        return res

