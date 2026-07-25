class Solution(object):
    def calPoints(self,a):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in a:
            if i not in {'C','D','+'}:
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i =="D":
                stack.append(stack[-1]*2)
            elif i == "+":
                stack.append(stack[-1]+stack[-2])
        return sum(stack)
       
        