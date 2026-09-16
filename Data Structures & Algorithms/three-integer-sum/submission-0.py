class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = 0
        res = []

        while k < len(nums):

            if k > 0 and nums[k] == nums[k - 1]:
                k += 1
                continue

            i = k + 1
            j = len(nums) - 1

            while i < j:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[k], nums[i], nums[j]])

                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif total > 0:
                    j -= 1

                else:
                    i += 1

            k += 1

        return res