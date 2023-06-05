# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        # 特殊情况，如果一个链表为空那么结果返回另一个链表
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        # 从头结点开始考虑，比较两表头结点的值，值较小的list的头结点后面接merge好的链表（进入递归了）；
        if pHead1.val <= pHead2.val:
            pMerge = pHead1
            pMerge.next = self.Merge(pHead1.next,pHead2)
        else:
            pMerge = pHead2
            pMerge.next = self.Merge(pHead1,pHead2.next)

        # 返回结果即可
        return pMerge