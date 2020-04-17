class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B=[]
        for i in range(len(A)):
            B.append(A[i]*A[i])
        B=sorted(B)
        return B