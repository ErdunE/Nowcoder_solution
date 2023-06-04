class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        # 优先处理空链表，即空链表不需要处理
        if not head:
            return None

        # 设置两个指针，一个指向当前节点的指针，一个指向上一个节点的指针，初始设置为空
        cur = head
        pre = None

        # 遍历整个链表，每到一个节点，
        while cur:
            # 断开链表，但是要记录后一个节点
            temp = cur.next
            # 当前的next指向前一个
            cur.next = pre
            # 前一个更新为当前
            pre = cur
            # 当前更新为刚刚记录的后一个 
            cur = temp

        return pre