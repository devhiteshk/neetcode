class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []

        for i in nums:
            if i in d:
                d[i] += 1
            
            else:
                d[i] = 1
        
        # sort by occurence Decending order
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
            
        for i in range(k):
            res.append(sorted_items[i][0])

        return res