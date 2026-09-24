class Solution(object):
    def topKFrequent(self, nums, k):
        Sortt = {}
        for i in nums:
            if i in Sortt:
                Sortt[i]+=1
            else:
                Sortt[i]= 1
        
        sorte = sorted(Sortt.items(), key = lambda item: item[1],reverse = True)
        result = []
        for i in sorte[:k]:
            result.append(i[0])


        return result