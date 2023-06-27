## BM87_简单_合并两个有序的数组

#### 题目链接 [BM87_简单_合并两个有序的数组](https://www.nowcoder.com/practice/89865d4375634fc484f3a24b7fe65665?tpId=295&tqId=658&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/WvjBBDn/20230627101950.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 有序的整数数组 A 和有序的整数数组 B
2. 数组 B 合并到数组 A 中
3. 变成一个有序的升序数组
4. A的数组空间大小足够大 m+n

---
### 解题步骤
1. 设置3个指针 分别指向数组A的最后一个 数组B的最后一个，以及数组A实际的最后一个
2. 比较数组A和数组B的最后一个数字，较大的放入到数组A实际最后一个
3. 每次比较完放入较大数后将数组A最后一个数字往前进1
4. 遍历完后如果数组B还有数字，直接遍历覆盖到数组A中
---

### 最终代码
```
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        
        # 设置3个指针 分别指向数组A的最后一个 数组B的最后一个，以及数组A实际的最后一个
        i = m - 1
        j = n - 1
        p = m + n - 1

        # 比较数组A和数组B的最后一个数字，较大的放入到数组A实际最后一个
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[p] = A[i]
                i = i - 1
            else:
                A[p] = B[j]
                j = j - 1

            # 每次比较完放入较大数后将数组A最后一个数字往前进1    
            p = p - 1

        # 遍历完后如果数组B还有数字，直接遍历覆盖到数组A中
        while j >= 0:
            A[p] = B[j]
            j = j - 1
            p = p - 1
```