## BM100_较难_设计LRU缓存结构

#### 题目链接 [BM100_较难_设计LRU缓存结构)](https://www.nowcoder.com/practice/5dfded165916435d9defb053c63f1e84?tpId=295&tqId=2427094&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/k5XnJjB/20230712130749.png)

---
## 解题思路
---
### 使用方法：哈希表+双向链表
---
### 题目关键信息

1. 实现LRU缓存的模拟结构，包括加入函数set，访问函数get
2. 结构有长度限制，加入新数时，超出长度则需要删除最不常访问的，其中set与get都访问
3. 两个函数都是O(1)

---
### 解题步骤
1. 构建一个双向链表的类，记录key值与val值，同时一前一后两个指针。用哈希表存储key值和链表节点，这样我们可以根据key值在哈希表中直接锁定链表节点，从而实现在链表中直接访问，能够做到O(1
)时间访问链表任意节点。
2. 设置全局变量，记录双向链表的头、尾及LRU剩余的大小，并全部初始化，首尾相互连接好。
3. 遍历函数的操作数组，检查第一个元素判断是属于set操作还是get操作。
4. 如果是set操作，即将key值与val值加入链表，我们先检查链表中是否有这个key值，可以通过哈希表检查出，如果有直接通过哈希表访问链表的相应节点，修改val值，并将访问过的节点移到表头；如果没有则需要新建节点加到表头，同时哈希表中增加相应key值（当然，还需要检查链表长度还有无剩余，若是没有剩余则需要删去链表尾）。
5. 不管是新节点，还是访问过的节点都需要加到表头，若是访问过的，需要断开原来的连接，再插入表头head的后面。
6. 删除链表尾需要断掉尾节点前的连接，同时哈希表中去掉这个key值。
7. 如果是get操作，检验哈希表中有无这个key值，如果没有说明链表中也没有，返回-1，否则可以根据哈希表直接锁定链表中的位置进行访问，然后重复step 5，访问过的节点加入表头。
---

### 最终代码
```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

class Solution:

    def __init__(self, capacity: int):
        # write code here
        self.cap = capacity
        self.hash = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        # write code here
        if key in self.hash:
            if self.hash[key].pre!=None:
                self.freshListNode(self.hash[key])
            return self.hash[key].val[0]
        else:
            return -1
        
    def set(self, key: int, value: int) -> None:
        # write code here
        value = [value, key]
        if key in self.hash:
            self.hash[key].val = value
            if self.hash[key].pre!=None:
                self.freshListNode(self.hash[key])
            return
        if self.cap > 0:
            ele = ListNode(value)
            self.hash[key] = ele
            self.addOneNode(ele)
            self.cap-=1
        else:
            del self.hash[self.tail.val[1]]
            self.hash[key] = self.tail
            self.tail.val = value
            if self.tail.pre != None:
                self.freshListNode(self.tail)

    def freshListNode(self, ele):
        ele.pre.next = ele.next
        if self.tail == ele:
            self.tail = ele.pre
        else:
            ele.next.pre = ele.pre
        ele.pre = None
        self.head.pre = ele
        ele.next = self.head
        self.head = ele

    def addOneNode(self, ele):
        if self.head == None:
            self.head = ele
            self.tail = ele
        else:
            ele.pre = None
            ele.next = self.head
            self.head.pre = ele
            self.head = ele
```