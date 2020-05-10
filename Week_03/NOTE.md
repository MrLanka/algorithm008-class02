第3周  学习笔记

第七课

泛型递归、树的递归


递归 Recursion
递归 - 循环
通过函数体来进行的循环


特点：
• 向下进入到不同梦境中；向上又回到原来一层：梦境代表不同函数层

• 通过声音同步回到上一层：声音代表不同层之间传递的参数

• 每一层的环境和周围的人都是一份拷贝、 主角等几个人穿越不同层级的梦境（发生和携带变化）：函数里的参数（全局变量）可以实现不同层之间的传递



Python 代码模版
def recursion(level, param1, param2, ...): 
    # recursion terminator         ————>递归终止条件
    if level > MAX_LEVEL: 
        process_result 
        return 

    # process logic in current level ————>处理当前层逻辑
    process(level, data...) 
    
    # drill down                ————>下探到下一层
    self.recursion(level + 1, p1, ...) 
    
    # reverse the current level status if needed  ————>必要时，清理当前层




思维要点
1. 不要人肉进行递归（最大误区）

2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）

3. 数学归纳法思维







第八课

分治、回溯


分治代码模板
def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator 
    if problem is None: 
        print_result 
        return 

    # prepare data 
    data = prepare_data(problem) 
    subproblems = split_problem(problem, data) 

    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
    ...

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …) 
 
    # revert the current level states


 回溯

Backtracking


回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程
中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将
取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问
题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种
情况：

• 找到一个可能存在的正确的答案；

• 在尝试了所有可能的分步方法后宣告该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。