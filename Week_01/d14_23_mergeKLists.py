#方法一：暴力求解，O(NlogN)和O(N)       先学会这种方法，再学优先队列和分治等方法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #声明用于排序的空数组
        self.nodes=[]
        #声明头节点和构成链表的结点
        head=point=ListNode(0)
        #将输入的节点值放入数组中
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l=l.next
        #将数组排序并建立新的链表
        for x in sorted(self.nodes):
            point.next=ListNode(x)
            point=point.next
        return head.next


#方法二：优先队列,O(Nlogk)和O(N)

from Queue import PriorityQueue
class Solution:
    def mergeLists(self,lists:List[ListNode])->ListNode:
        #声明头节点和构成链表的结点
        head=point=ListNode(0)
        #声明优先队列
        q=PriorityQueue()
        #将输入的节点放入优先队列中
        for l in lists:
            if l:
                q.put(l.val,l)
        #循环迭代队列
        while not q.empty():
            val,node=q.get()
            point.next=ListNode(val)
            point=point.next
            node=node.next
            if node:
                q.put(node.val,node)
        return head.next


#方法三：分治思想
