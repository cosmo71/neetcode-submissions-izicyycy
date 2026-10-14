class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap
        # iterate through list
        # check if current num is in list
            #   if yes -> return false
            #   if no -> add to hashmap
        # return true



        m = {}

        for n in nums:
            if n in m:
                return True
            else:
                m[n] = 1
        
        return False