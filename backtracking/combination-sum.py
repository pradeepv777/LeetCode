class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i,current_sum,path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum> target:
                return
            if i ==len(candidates):
                return 
            path.append(candidates[i])
            dfs(i , current_sum+candidates[i],path)
            path.pop()

            dfs(i+1,current_sum ,path)
        dfs(0,0,[])
        return res



        