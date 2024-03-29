## BM101_较难_设计LFU缓存结构

#### 题目链接 [BM101_较难_设计LFU缓存结构](https://www.nowcoder.com/practice/93aacb4a887b46d897b00823f30bfea1?tpId=295&tqId=1006014&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/Zzvnpw9/20230712130842.png)

---
## 解题思路
---
### 使用方法：哈希表
---
### 题目关键信息
1. 实现LFU的set与get函数，且复杂度为O(1)
2. 每次调用这两个函数会给一个频率赋值，超出长度则移除频率最少的，若有频率相同，则移除访问时间最早的
---
### 解题步骤
1. 设置 dict 记录 key-val 值,设置 cap 记录容量;
2. 根据调用次数和调用次序进行排序,得出最终的最小key.
---

### 最终代码
```
class Cache:
    def __init__(self, k):
        self.cap = k
        self.data = dict()
     
    def getFirstKey(self):
        k = sorted(self.data.items(), key=lambda x:[x[1][1], x[1][2]])[0][0]
        return k
         
    def isFull(self):
        return len(self.data) == self.cap
     
    def setKey(self, key, val, tp):
        if not self.isFull():
            if key not in self.data:
                self.data[key] = [val, 1, tp]
            else:
                self.data[key][0] = val
                self.data[key][1] += 1
                self.data[key][2] = tp
        elif self.isFull() and key in self.data:
            self.data[key][0] = val
            self.data[key][1] += 1
            self.data[key][2] = tp
        else:
            self.data.pop(self.getFirstKey())
            self.data[key] = [val, 1, tp]
     
    def getKey(self, key, tp):
        if key in self.data:
            self.data[key][1] += 1
            self.data[key][2] = tp
        return -1 if key not in self.data else self.data[key][0]    
         
         
class Solution:
    def LFU(self , operators: List[List[int]], k: int) -> List[int]:
        # write code here
        res = []
        cache = Cache(k)
        for i in range(len(operators)):
            if operators[i][0] == 1:
                cache.setKey(operators[i][1], operators[i][2], i)            
            elif operators[i][0] == 2:
                res.append(cache.getKey(operators[i][1],i))
        return res
```