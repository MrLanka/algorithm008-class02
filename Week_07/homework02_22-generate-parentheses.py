class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def _generate(left:int,right:int,n:int,s:str):
            #terminator
            if left==n and right==n:
                result.append(s)
                return
            #process
            #drill down
            if left<n:
                _generate(left+1,right,n,s+"(")
            if right<left:
                _generate(left,right+1,n,s+")")

        _generate(0,0,n,"")
        return result