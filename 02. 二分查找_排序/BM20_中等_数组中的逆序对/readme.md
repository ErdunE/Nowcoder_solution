## BM20_中等_数组中的逆序对

#### 题目链接 [BM20_中等_数组中的逆序对](https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=295&tqId=23260&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/StynmhH/20230705074352.png)

---
## 解题思路
---
### 使用方法：
---
### 题目关键信息
1. 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
2. 输入一个数组，求一个数组的全部逆序对，答案对1000000007取模
3. 保证输入的数组中没有的相同的数字


---
### 解题步骤
不理解需要复查
https://blog.nowcoder.net/n/55c9f7f11fb04ab29b38d4430a766912?f=comment
---

### 最终代码
```
class Solution:
    mod = 1000000007
    def MergeSort(self, left: int, right: int, data: List[int], temp: List[int]) -> int:
         # 停止划分
        if left >= right:
            return 0
        # 取中间
        mid = int((left + right) / 2)
        # 左右划分合并
        res = self.MergeSort(left, mid, data, temp) + self.MergeSort(mid + 1, right, data, temp)
        # 防止溢出
        res %= self.mod
        i, j = left, mid + 1
        for k in range(left, right+1):
            temp[k] = data[k]
        for k in range(left, right+1):
            if i == mid + 1:
                data[k] = temp[j]
                j += 1
            elif j == right + 1 or temp[i] <= temp[j]:
                data[k] = temp[i]
                i += 1
            # 左边比右边大，答案增加
            else:
                data[k] = temp[j]
                j += 1
                # 统计逆序对
                res += mid - i + 1
        return res % self.mod
             
    def InversePairs(self , data: List[int]) -> int:
        n = len(data)
        res = [0 for i in range(n)]
        return self.MergeSort(0, n - 1, data, res)
```