class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[]
        M=len(matrix)
        N=len(matrix[0])
        for i in range(0,M):
            for j in range(0,N):
                if matrix[i][j]==0:
                    res.append([i,j]
        for c in res:
            for j in range(0,N):
                matrix[c[0]][j]=0
            for i in range[0,M]:
                matrix[i][c[1]]=0