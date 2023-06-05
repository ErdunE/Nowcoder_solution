from importlib.abc import TraversableResources
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head: ListNode) -> bool:
        # 如果链表为空或者节点数量只有1个 那么不满足成环的标准，即返回False
        if head == None or head.next == None:
            return False

        # 设置快慢两指针
        fast = slow = head

        # 设置循环
        while fast and fast.next:
            
            # 慢指针只走一步，快指针走两步，只要快指针和快指针下一个还有那就一直循环，直到和慢指针碰到
            fast = fast.next.next
            slow = slow.next

            # 碰到的话返回Ture
            if fast == slow:
                return True
        
        # 其他情况返回False
        return False

        