class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # 30 38 30 36 35 40 28
        # 1  4  1   2 1  0  0

        # [30] push i = 0
        # 38 , 30 pop compare is greater, push 38, i = 1
        
        # [38], 30 pop compare is lower, push 30 i = 2
        # [38, 30], 36 pop compare is greter, pop compare is lower, push 38, 36 i = 3
        

        stack = []
        upto = [0] * len(temperatures)

        for i in range(len(temperatures)):
            current = temperatures[i]
            if i == 0:
                stack.append((i, current))
            else:

                while(len(stack) != 0):
                    j, last = stack.pop()
                    print(j , last)

                    if current > last:
                        upto[j] = i - j
                    else:
                        stack.append((j, last))
                        break

                stack.append((i, current))

            
        return upto

