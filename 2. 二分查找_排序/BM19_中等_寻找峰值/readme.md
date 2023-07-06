## BM19_中等_寻找峰值

#### 题目链接 [BM19_中等_寻找峰值](https://www.nowcoder.com/practice/fcf87540c4f347bcb4cf720b5b350c76?tpId=295&tqId=2227748&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/RPZB3r6/20230705074235.png)
![img](https://i.ibb.co/Srt0Wp5/20230705074245.png)

---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 给定一个长度为n的数组，返回其中任何一个峰值的索引
2. 峰值元素是指其值严格大于左右相邻值的元素
3. 数组两个边界可以看成是最小，nums[−1]=nums[n]=−∞
4. 峰值不存在平的情况，即相邻元素不会相等


---
### 解题步骤
1. 创建左右指针 分别指向头尾
2. 左指针小与右指针就一直循环
3. 设置中间指针
4. 如果中间指针的数字大于其下一个数字则令右指针等于它
5. 反之则令左指针等于它    
---

### 最终代码
```
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here

        # 创建左右指针 分别指向头尾
        left = 0
        right = len(nums) - 1

        # 左指针小与右指针就一直循环
        while left < right:
            # 设置中间指针
            mid = int((left + right) / 2)
            # 如果中间指针的数字大于其下一个数字则令右指针等于它
            if nums[mid] > nums [mid + 1]:
                right = mid
            # 反之则令左指针等于它    
            else:
                left = mid + 1

        return right
```