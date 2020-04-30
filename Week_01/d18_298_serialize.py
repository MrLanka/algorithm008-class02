# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"   #基线条件
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(alist):
            if alist[0] == "None":
                alist.pop(0)
                return None
            root = TreeNode(alist[0])
            alist.pop(0)
            root.left = dfs(alist)
            root.right = dfs(alist)    #注意：此处的两个alist,实际大小并不相同
            return root
        if not data:
            return None
        return dfs(data.split(","))
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

作者：blackgeeker
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/pythondi-gui-jian-ji-qing-xi-by-blackgeeker/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。