#还是递归，O(N)和O(logN)

#define N-Tree Node
class Node:
    def __init__(self,val=None,children=None):
        self.val=val
        self.childeren=children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None: 
            return 0 
        elif root.children == []:
            return 1
        else: 
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1 

