class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans=[1]*k 
        index3,index5,index7=0,0,0
        for i in range(1,k):
            ans[i]=min(ans[index3]*3,ans[index5]*5,ans[index7]*7)
            if ans[i]==ans[index3]*3:
                index3+=1
            if ans[i]==ans[index5]*5:
                index5+=1
            if ans[i]==ans[index7]*7:
                index7+=1
        return ans[k-1]