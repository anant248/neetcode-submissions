class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using monotonic stack
        # time: O(n)
        # space: O(n)
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            # while stack isnt empty and we have a warmer temp, keep updating
            while stack and temp > stack[-1][1]:
                previ, prevTemp = stack.pop()
                res[previ] = i - previ
            
            stack.append((i, temp))
        
        return res


            


