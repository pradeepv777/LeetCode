class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]

        def dfs(i, cur_sum, path):
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target:
                return
            if i == len(candidates):
                return
            path.append(candidates[i])
            dfs(i, cur_sum + candidates[i], path)
            path.pop()

            dfs(i+1, cur_sum, path)
        dfs(0,0 , [])
        return res





       