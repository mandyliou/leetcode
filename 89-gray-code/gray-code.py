class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        visited = set([0])
        
        def backtrack(current: int) -> bool:
            if len(result) == 2**n:
                return True
            
            for i in range(n):
                next_num = current ^ (1 << i)
                if next_num not in visited:
                    visited.add(next_num)
                    result.append(next_num)
                    
                    if backtrack(next_num):
                        return True
                    
                    visited.remove(next_num)
                    result.pop()
                    
            return False
        
        backtrack(0)
        return result