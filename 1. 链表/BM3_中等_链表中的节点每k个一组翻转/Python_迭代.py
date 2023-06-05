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
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        # 特殊情况 k=1的话 不用反转 没有head的话返回None
        if k == 1:
            return head
        if not head:
            return None
        
        # 链表前新加一个表头，后续输出结果时候去掉即可，这样做是防止如果从链表头的位置开始反转，在多了一个表头的情况下就能保证第一个节点永远不会被反转，不会到后面去
        newhead = ListNode(-1)
        newhead.next = head

        # 遍历链表长度
        leng = newhead.next
        i = 0
        while leng:
            i = i + 1
            leng = leng.next
        
        # 设置前序指针和当前指针
        pre = newhead
        cur = pre.next

        # 分组进行判断 即满足链表中依然有节点且满足反转数量，然后一组组进行反转
        while head and i>=k:
            # 当前组进行反转
            for j in range(k-1):
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            # 当前组已经反转完成，开始准备下一组
            i = i-k
            pre = cur
            cur = pre.next

        return newhead.next 
