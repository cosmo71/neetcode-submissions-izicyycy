class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hmap = {}

        for n in nums:
            # print(hmap)
            if n not in hmap:
                hmap[n] = 1
            else:
                return True


        return False