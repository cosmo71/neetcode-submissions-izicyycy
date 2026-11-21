class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a list with 26 elements , use the ord function for getting the ASCII value, a has 97 z has 97 + 26 - 1

        # convert the list into a tuple 
        # add the tuple as a key with a list that contains the string


        h = {}

        for s in strs:

            key = [0] * 26

            for c in s:
                key[ord(c)-97] += 1

            key = tuple(key)
            # print(key)
            h[key] = h.get(key, []) + [s]
            # print(h)
            # print("--------")
        
        return list(h.values())
