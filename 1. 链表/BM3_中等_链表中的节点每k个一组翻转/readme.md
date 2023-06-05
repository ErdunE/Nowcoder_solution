## BM3 中等 链表中的节点每k个一组翻转

#### 题目链接 [BM3 中等 链表中的节点每k个一组翻转](https://www.nowcoder.com/practice/b49c3dc907814e9bbfa8437c251b028e?tpId=295&tqId=722&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

> ### 描述
> 将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表 \
> 如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样 \
> 你不能更改节点中的值，只能更改节点本身。
>
> 数据范围：0≤n≤2000 ， 1≤k≤2000 ，链表中每个元素都满足 0≤val≤1000 \
> 要求空间复杂度 O(1)，时间复杂度 O(n)
> 
> 例如： \
> 给定的链表是 1→2→3→4→5 \
> 对于 k=2 , 你应该返回 2→1→4→3→5 
> 对于 k=3 , 你应该返回 3→2→1→4→5 
> 
---
## 解题思路
---
### 使用方法：迭代
---
### 题目关键信息

> 将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表。 \
> 如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样。 \
> 你不能更改节点中的值，只能更改节点本身。 

---
### 解题步骤

1. 特殊情况 k=1的话 不用反转 没有head的话返回None
2. 链表前新加一个表头，后续输出结果时候去掉即可，这样做是防止如果从链表头的位置开始反转，在多了一个表头的情况下就能保证第一个节点永远不会被反转，不会到后面去
3. 遍历链表长度
4. 设置前序指针和当前指针
5. 分组进行判断 即满足链表中依然有节点且满足反转数量，然后一组组进行反转
6. 当前组进行反转
7. 当前组已经反转完成，开始下一组

---

### 最终代码
```
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
```