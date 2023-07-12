## BM18_中等_二维数组中的查找

#### 题目链接 [BM18_中等_二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=295&tqId=23256&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/Dr0N0pq/20230705074118.png)

---
## 解题思路
---
### 使用方法：暴力法
---
### 题目关键信息
1. 二维数组array中（每个一维数组的长度相同）
2. 每一行都按照从左到右递增的顺序排序
3. 每一列都按照从上到下递增的顺序排序
4. 搜索数组array中是否有目标值
---
### 解题步骤
1. 如果array为空即返回False
2. 遍历每一行
3. 遍历每一列
4. 如果当前数字等于目标值则返回Ture
5. 反之列+1 继续搜索
6. 所有列搜完后，行+1
7. 如果遍历整个二维数组后还没发现目标值，则返回False

---

### 最终代码
```
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        
        if len(array) == 0:
            return False

        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == target:
                    return True
                else:
                    j += 1
                    continue
            i += 1
        return False
```