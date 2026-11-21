class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Bucket sort 

        m = {}
        
        for n in nums:
            m[n] = m.get(n, 0) + 1

        # print(m)
        
        counts = [0] * (len(nums) + 1)

        
        for key,v in m.items():
            # print(counts)
            if counts[v] == 0:
                counts[v] = [key]
            else:
                counts[v] = counts[v] + [key]

        counts = counts[::-1]
        final = []

        # print(counts)

        for i, l in enumerate(counts):  
            # print(final  )
            if l != 0 and k!= 0:
                final = final + l
                k-= len(l)

            
        return final

