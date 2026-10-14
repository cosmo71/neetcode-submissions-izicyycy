class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 Ways:
            # sorting: TC: O(n logn)
            # store in hashmap with counts: TC: O(n)
                # iterate through s and add all requencies to m
                    # m[c] += 1
                # subtract from m[c] every time c is in t
        
        if len(s) != len(t):
            return False

        m = {}

        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] +=1


        for c in t:
            if c not in m:
                return False
            
            m[c] -= 1

            if m[c] < 0:
                return False
        

        return True





