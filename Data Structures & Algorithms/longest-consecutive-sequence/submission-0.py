class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        s = set(nums)
        res = 0

        for i in s:
            if i - 1 not in s:
                l = 1

                x = i
                while x + 1 in s:
                    l += 1
                    x += 1
                
                res = max(res, l)

        return res

            
            


            
        