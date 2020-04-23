class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans=''
        count,i=1,1
        while i<len(S):
            count +=1 if S[i]=="(" else -1
            if count==0:
                count+=1
                i+=2
                continue
            ans+=S[i]
            i+=1
        return ans

#这里通过栈的状态来判定，左括号进栈右括号出栈。进栈时，栈长大于1说明不是最外层的括号，将中括号记录下来；
#出栈时，如果栈长不为零，说明不是最外层的左括号，记录下来。
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        ans=''
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(i)
                if len(stack)>1:
                    ans+=S[i]
            else:
                stack.pop()
                if len(stack)!=0:
                    ans+=S[i]
        return ans