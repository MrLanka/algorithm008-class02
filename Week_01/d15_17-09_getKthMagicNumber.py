class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans=[1]*k
        ind3,ind5,ind7=0,0,0
        for i in range(1,k):
            ans[i]=min(ans[ind3]*3,ans[ind5]*5,ans[ind7]*7)
            if ans[i]==ans[ind3]*3:
                ind3 += 1
            if ans[i]==ans[ind5]*5:
                ind5 += 1
            if ans[i]==ans[ind7]*7:
                ind7 += 1
        return ans[k-1]