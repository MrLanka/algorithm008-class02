class Solution:
    def reverseOnlyLetters(self, S: str) ->str:
        stack_1=[c for c in S if c.isalpha()]
        S_rev=[]
        for c in S:
            if c.isalpha()==1:
                S_rev.append(stack_1.pop())
            else:
                S_rev.append(c)
        return "".join(S_rev)