class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:return []
        self.result=[]
        #之前的皇后所攻击的位置（cols，pie，na）
        self.cols=set()
        self.pie=set()
        self.na=set()
        self.DFS(n,0,[])
        return self._generate_result(n)
    def DFS(self,n,row,cur_state):
        #recursion terminateor
        if row>=n:
            self.result.append(cur_state)
            return 
        #current level! Do it!
        for col in range(n):    #遍历列column
            if col in self.cols or row+col in self.pie or row-col in self.na:
                #go die!
                continue   
            #update the flags
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.DFS(n,row+1,cur_state+[col])
            #reverse states
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)
    def _generate_result(self,n):
        board=[]
        for res in self.result:
            for i in res:
                board.append("."*i+"Q"+"."*(n-i-1))
        return [board[i:i+n]for i in range(0,len(board),n)]