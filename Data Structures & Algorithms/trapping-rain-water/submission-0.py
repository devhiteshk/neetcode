class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        l = 0
        r = len(h) - 1
        res = 0
        l_max, r_max = h[l], h[r]

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, h[l])
                res += l_max - h[l]

            else:
                r -= 1
                r_max = max(r_max, h[r])
                res += r_max - h[r]

        return res

            
