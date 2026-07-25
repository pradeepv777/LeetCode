class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        temps = [0]* len(t)
        for i in range(len(t)-1,-1,-1):
            while stack and t[stack[-1]]<=t[i]:
                stack.pop()
            if stack:
                temps[i] = stack[-1] - i
            else:
                temps[i] = 0
            stack.append(i)
        return temps
        
        