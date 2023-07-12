# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 设置HashSet
        node = set()

        # 设置循环
        while pHead:

            # 如果节点在HashSet中，返回对应值
            if pHead in node:
                return pHead
            # 如果节点不在HashSet中 加入Hashset并且节点往前移
            else:
                node.add(pHead)
                pHead = pHead.next

        # 如果都不是 返回空        
        return None