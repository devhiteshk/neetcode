class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        res = []

        for i in range(1,len(nums)):
            prefix.append(prefix[-1]*nums[i])

        for j in range(len(nums)-2,-1,-1):
            suffix.append(suffix[-1]*nums[j])
        
        suffix.reverse()

        for k in range(len(nums)):
            if k == 0:
                res.append(suffix[1])

            elif k == len(nums) - 1:
                res.append(prefix[-2])

            else:
                res.append(prefix[k-1]*suffix[k+1])

        return res

        

