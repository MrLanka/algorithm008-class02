class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        if n<k:return[]
        if n==k:
            nums=list(range(1,n+1))
            ans.append(nums)
            return ans
        def backtrack(level=1,curr=[]):
            #terminator
            if len(curr) == k:  
                ans.append(curr[:])
            for i in range(level, n + 1):
                #prpare data
                curr.append(i)
                #drill down
                backtrack(i + 1, curr)
                #reverse
                curr.pop()
        backtrack()
        return ans