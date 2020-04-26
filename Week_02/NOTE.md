第二周 学习笔记

第五课   |哈希表、映射、集合

Hash table

哈希表（Hash table），也叫散列表，是根据关键码值（Key value）而直接进行访问的数据结构。 
它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。 
这个映射函数叫作散列函数（Hash Function），存放记录的数组叫作哈希表（或散列表）。

工程实践
• 电话号码簿

• 用户信息表

• 缓存（LRU Cache）

• 键值对存储（Redis）


Python code
list_x = [1, 2, 3, 4] 
map_x = { 
 ‘jack’: 100, 
 ‘张三’: 80, 
 ‘selina’: 90, 
 … 
} 
set_x = {‘jack’, ‘selina’, ‘Andy’} 
set_y = set([‘jack’, ‘selina’, ‘jack’])





第六课 |树、二叉树、二叉搜索树

单链表 Linked List       树 Tree        二叉树 Binary Tree         图 Graph
                         （Linked List 是特殊化的 Tree        Tree 是特殊化的 Graph）

示例代码
Python
class TreeNode: 
def __init__(self, val): 
 self.val = val 
 self.left, self.right = None, None

 
 二叉树遍历 Pre-order/In-order/Post-order
1.前序（Pre-order）：根-左-右
def preorder(self, root): 
    if root: 
        self.traverse_path.append(root.val) 
        self.preorder(root.left) 
        self.preorder(root.right)

2.中序（In-order）：左-根-右
def inorder(self, root): 
    if root: 
        self.inorder(root.left) 
        self.traverse_path.append(root.val) 
        self.inorder(root.right) 

3.后序（Post-order）：左-右-根
def postorder(self, root): 
    if root: 
        self.postorder(root.left) 
        self.postorder(root.right) 
        self.traverse_path.append(root.val)

 
二叉搜索树 Binary Search Tree

二叉搜索树，也称二叉搜索树、有序二叉树（Ordered Binary Tree）、排序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉树： 
1. 左子树上所有结点的值均小于它的根结点的值； 
2. 右子树上所有结点的值均大于它的根结点的值； 
3. 以此类推：左、右子树也分别为二叉查找树。 （这就是 重复性！）

中序遍历：升序排列


二叉搜索树常见操作——时间复杂度都是:O(logN)
1. 查询
2. 插入新结点（创建）
3. 删除
Demo: https://visualgo.net/zh/bst

树的面试题解法一般都是递归，为什么？
答：从树的本身结构考虑，代码对根的左右节点使用相同的遍历方法。






第六课 |堆 Heap 和二叉堆 Binary Heap

堆 Heap
Heap：可以迅速找到一堆数中的最大值或者最小值的数据结构》

常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，则常见操作（API）：

find-max:         0(1)
delete-max:       O(LogN)
insert(create):    O(LogN) or O(1)

不同实现的比较:htps://en, Wikipedia.org/wiki/Heap_(data_ structure)


二叉堆性质

通过完全二叉树来实现(注意:不是二叉搜索树)；

二叉堆(大顶)它满足下列性质：
【性质一】是一棵完全树；
【性质二】树中任意节点的值总是>=其子节点的值；


二叉堆实现细节
1、二叉堆一般通过“数组”来实现
2、假设“第一个元素”在数组中的索引为0的话，
   则父节点和子节点的位置关系如下：
   （01）索引为i的左孩子的索引是（2*i+1）；
   （02）索引为i的右孩子的索引是（2*i+2）；
   （03）索引为i的父节点的索引是floor（（i-）/2）.

二叉堆
0.根节点（顶堆元素）是：a[0]

1.索引为i的左孩子的索引是（2*i+1）；
2.索引为i的右孩子的索引是（2*i+2）；
3.索引为i的父节点的索引是floor（（i-）/2）.


Insert 插入操作  ———— O（logN）
1.新元素一律先插入到堆的尾部
2.依次向上调整堆的结构（一直到根即可）
HeapifyUp


Delete Max 删除顶堆操作  ———— O（logN）
1.将堆尾元素替换到顶部（即对顶被替代删除掉）
2.依次从根部向下调整堆的结构（一直到堆尾即可）
HeapifyDown


注意：二叉堆是堆（优先队列priority_queue）的一种常见且简单的实现；但是并不是最优的实现。




第六课 |图 Graph

目录：1、图的属性和分类      2、基于图相关的算法

图的属性
数学上：Graph（V，E）

V-vertex：点
    1.度=入度和出度
    2.点与点之间：连通与否

E-edge：边
    1.有向和无向（单行线）
    2.权重（边长）

图的表示和分类
1、无向无权图
2、有向无权图
3、无向有权图
4、有向有权图

DFS代码-递归写法
                            注意：visited=set()   #和树中的DFS/BFS的最大区别
BFS代码