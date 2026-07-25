class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
        }
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1]!= map[i]:
                    return False
                stack.pop()
        return len(stack)== 0 

       