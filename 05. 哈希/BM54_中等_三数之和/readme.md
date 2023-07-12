## BM54_中等_三数之和

#### 题目链接 [BM54_中等_三数之和)](https://www.nowcoder.com/practice/345e2ed5f81d4017bbb8cc6055b0b711?tpId=295&tqId=731&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/hgzr8G8/20230703102150.png)


---
## 解题思路
---
### 使用方法：双指针
---
### 题目关键信息
1. 有n个元素的数组S
2. S中是否有元素a,b,c满足a+b+c=0？
---
### 解题步骤
1. 设置结果数组
2. 如果不够三元组则返回结果数组即空
3. 对当前数组进行排序
4. 遍历
5. 后续的收尾双指针
6. 设置当前数的负值为目标
7. 双指针指向的二值相加为目标，则可以与num[i]组成0
8. 去重
9. 双指针向中间收缩
10. 双指针指向的二值相加大于目标，右指针向左
11. 双指针指向的二值相加小于目标，左指针向右
---

### 最终代码
```
class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        # write code here

        # 设置结果数组
        res = list(list())
        n = len(num)
        # 如果不够三元组则返回结果数组即空
        if n < 3:
            return res
        # 对当前数组进行排序
        num.sort()

        # 遍历
        for i in range(n - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue
            # 后续的收尾双指针
            left = i + 1
            right = n - 1
            # 设置当前数的负值为目标
            target = -num[i]
            while left < right:
                # 双指针指向的二值相加为目标，则可以与num[i]组成0
                if num[left] + num[right] == target:
                    res.append([num[i], num[left], num[right]])
                    while left + 1 < right and num[left] == num[left + 1]:
                        # 去重
                        left += 1
                    while right - 1 > left and num[right] == num[right - 1]:
                        # 去重
                        right -= 1
                    # 双指针向中间收缩
                    left += 1
                    right -= 1
                # 双指针指向的二值相加大于目标，右指针向左
                elif num[left] + num[right] > target:
                    right -= 1
                # 双指针指向的二值相加小于目标，左指针向右
                else:
                    left += 1
        return res 
```