class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a_count,b_count=0,0
        s,g=[],[]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a_count +=1
            else:
                s.append(secret[i])
                g.append(guess[i])       
        counter1,counter2 = collections.Counter(s), collections.Counter(g)
        for k in counter1.keys():
            if k in counter2:
                b_count += min(counter1[k], counter2[k])
        return str(a_count)+"A"+str(b_count)+"B"