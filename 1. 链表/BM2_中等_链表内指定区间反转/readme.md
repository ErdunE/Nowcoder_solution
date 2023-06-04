## BM2 中等 链表内指定区间反转

#### 题目链接 [BM2 链表内指定区间反转](https://www.nowcoder.com/practice/b58434e200a648c589ca2063f1faf58c?tpId=295&tqId=654&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

> ### 描述
> 将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 O(n)，空间复杂度 O(1)。\
> 例如：\
> 给出的链表为 1→2→3→4→5→NULL, m=2,n=4,\
> 返回 1→4→3→2→5→NULL.
>
> 数据范围： 链表长度 0<size≤1000，0<m≤n≤size，链表中每个节点的值满足 ∣val∣≤1000\
> 要求：时间复杂度 O(n) ，空间复杂度 O(n)\
> 进阶：时间复杂度 O(n)，空间复杂度 O(1)
> 
> ### 示例1
> 输入：{1,2,3,4,5},2,4 \
> 返回值：{1,4,3,2,5}\
> 
> ### 示例2
> 输入：{5},1,1\
> 返回值：{5}\
> 说明：空链表则输出空 

---
## 解题思路
---
### 使用方法：迭代法
---
### 题目关键信息

将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转\
链表其他部分不变，返回头节点

---
### 解题步骤

1. 链表前新加一个表头，后续输出结果时候去掉即可，这样做是防止如果从链表头的位置开始反转，在多了一个表头的情况下就能保证第一个节点永远不会被反转，不会到后面去
2. 使用两个指针，一个指向当前节点，一个指向前序节点
3. 依次遍历链表，直到第m个位置
4. 对于m到n中的节点，依次断掉后续的指针，反转指针方向
5. 返回链表，去掉表头

---

### 最终代码
```
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
#
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        # 链表前新加一个表头
        newhead = ListNode(-1)
        newhead.next = head

        # 当前节点
        cur = head
        # 前序节点
        pre = newhead

        # 找到m 
        for i in range (1,m):
            pre = cur
            cur = cur.next

        # 从m开始反转
        for i in range (m,n):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        # 去掉表头
        return newhead.next
```