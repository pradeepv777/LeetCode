class Solution(object):
    def moveZeroes(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0
        for i in range(len(a)):
            if a[i]!=0:
                a[write],a[i] = a[i],a[write]
                write+=1
