class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # nums[i] + nums[j] = target
    # return [i , j]
    # i != j


        h = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            
            if diff in h:
                return [h[diff], i]
            else:
                h[n] = i

        
        return []