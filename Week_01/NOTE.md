学习笔记
第3课 数组、链表、跳表
    对于这一块知识，可能是相对简单而且接触的多，也可能是只做的这一部分题目都是简单题，才觉得这一部分的练习题，认真思考都能找到解题思路。所以觉得这一部分学的还可以。

    但是对于后面一课，基本的概念也好理解，就是做题的时候很难把握好，甚至会碰到一些需要思考很久的题解。



第4课 栈、队列、优先队列、双端队列
    栈和队列是两种基本的数据结构，同为容器类型。两者根本的区别在于：stack:后进先出，queue:先进先出。PS:stack和queue是不能通过查询具体某一个位置的元素而进行操作的，需要遍历，时间复杂度O(n)。但是他们的排列是按顺序的。
    
    这是两个最基本的常识，在做题的过程中，利用栈的后进先出往往能有出其不意的效果。比如Leetcode中第917题仅仅反转字母https://leetcode-cn.com/problems/reverse-only-letters/。
    这道题我的第一个想法就是利用栈后进先出的特点，将字符串中所有字母压入栈中，然后遍历原字符串，遇到字母就从栈里pop出一个元素进行替换，遇到非字母就跳过，从而实现一个反转。当然最后学习别人的题解过程中也看到不少其它的思路，比如双指针等。
    
    但是真正在做关于栈和队列的题目时，有时候还是一头雾水，即使看了别人的题解，也一时半会不能明了。


    后面自己又查了一些相关的资料。
    
    对于stack我们可以使用python内置的list实现，因为list是属于线性数组，在末尾插入和删除一个元素所使用的时间都是O(1),这非常符合stack的要求。当然，我们也可以使用链表来实现。

    stack的实现代码（使用python内置的list），实现起来是非常的简单，就是list的一些常用操作:
        class Stack(object):
        def __init__(self):
            self.stack = []

        def push(self, value):    # 进栈
            self.stack.append(value)

        def pop(self):  #出栈
            if self.stack:
                self.stack.pop()
            else:
                raise LookupError('stack is empty!')

        def is_empty(self): # 如果栈为空
            return bool(self.stack)

        def top(self): 
            #取出目前stack中最新的元素
            return self.stack[-1]


    使用链表来实现队列数据结构：
    定义一个头结点，左边指向队列的开头，右边指向队列的末尾，这样就可以保证我们插入一个元素和取出一个元素都是O(1)的操作，使用这种链表实现stack也是非常的方便。实现代码如下：
        class Head(object):
        def __init__(self):
            self.left = None
            self.right = None

        class Node(object):
            def __init__(self, value):
                self.value = value
                self.next = None

        class Queue(object):
            def __init__(self):
            #初始化节点
            self.head = Head()

        def enqueue(self, value):
            #插入一个元素
            newnode = Node(value)
            p = self.head
            if p.right:
                #如果head节点的右边不为None
                #说明队列中已经有元素了
                #就执行下列的操作
                temp = p.right
                p.right = newnode
                temp.next = newnode
            else:
                #这说明队列为空，插入第一个元素
                p.right = newnode
                p.left = newnode

        def dequeue(self):
            #取出一个元素
            p = self.head
            if p.left and (p.left == p.right):
                #说明队列中已经有元素
                #但是这是最后一个元素
                temp = p.left
                p.left = p.right = None
                return temp.value
            elif p.left and (p.left != p.right):
                #说明队列中有元素，而且不止一个
                temp = p.left
                p.left = temp.next
                return temp.value

            else:
                #说明队列为空
                #抛出查询错误
                raise LookupError('queue is empty!')

        def is_empty(self):
            if self.head.left:
                return False
            else:
                return True

        def top(self):
            #查询目前队列中最早入队的元素
            if self.head.left:
                return self.head.left.value
            else:
                raise LookupError('queue is empty!')




