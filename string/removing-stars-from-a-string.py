class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if not i == "*":
               stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
  