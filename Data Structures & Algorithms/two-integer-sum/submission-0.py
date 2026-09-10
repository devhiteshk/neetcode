class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):

            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]

            if target - nums[i] in d:
                for z in d[target - nums[i]]:
                    if z != i:
                        return [z,i]
                