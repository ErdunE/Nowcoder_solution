## BM4 简单 合并两个排序的列表

#### 题目链接 [BM4 简单 合并两个排序的列表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=295&tqId=23267&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

### 描述
> 输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。 \
> 数据范围： 0≤n≤1000，−1000≤节点值≤1000  \
> 要求：空间复杂度 O(1)，时间复杂度 O(n)
>
> 如输入{1,3,5},{2,4,6}时，合并后的链表为{1,2,3,4,5,6}，所以对应的输出为{1,2,3,4,5,6}，转换过程如下图所示：\
> ![img](https://uploadfiles.nowcoder.com/images/20211014/423483716_1634208575589/09DD8C2662B96CE14928333F055C5580)
> 或输入{-1,2,4},{1,3,4}时，合并后的链表为{-1,1,2,3,4,4}，所以对应的输出为{-1,1,2,3,4,4}，转换过程如下图所示：
> ![img](https://uploadfiles.nowcoder.com/images/20211014/423483716_1634208729766/8266E4BFEDA1BD42D8F9794EB4EA0A13)
> ### 示例1
> 输入：{1,3,5},{2,4,6}  \
> 返回值：{1,2,3,4,5,6}
> ### 示例2 
> 输入：{},{}  \
> 返回值：{}
> ### 示例3 
> 输入：{-1,2,4},{1,3,4}  \
> 返回值： {-1,1,2,3,4,4}

---
## 解题思路
---
### 使用方法：递归
---
### 题目关键信息

> 合并这两个链表并使新链表中的节点仍然是递增排序的
---
### 解题步骤

1. 特殊情况，如果一个链表为空那么结果返回另一个链表
2. 从头结点开始考虑，比较两表头结点的值，值较小的list的头结点后面接merge好的链表（进入递归了）；
3. 返回结果即可
---

### 最终代码
``` 
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