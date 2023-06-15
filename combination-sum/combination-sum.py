class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(curr, curr_sum, idx):
            if curr_sum > target: #no way to reach target by adding num, sum too big
                return #ends current recurrsive call and goes back to the point where fxn was called & moves back to previous call in the call stack
            if curr_sum == target:#valid combo, add to list
                result.append(curr)
                return
            for i in range(idx, len(cand)): #curr_sum < target
                dfs((curr + [cand[i]]), (curr_sum + cand[i]), i)
        dfs([], 0, 0) #starts off as empty combo, sum's 0, & index's 0
        return result #returns list of all valid combo
        

                

