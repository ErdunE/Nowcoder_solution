## BM22_中等_比较版本号

#### 题目链接 [BM22_中等_比较版本号](https://www.nowcoder.com/practice/2b317e02f14247a49ffdbdba315459e7?tpId=295&tqId=1024572&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/ZK2v0kz/20230705074535.png)
![img](https://i.ibb.co/L5rGkb8/20230705074547.png)

---
## 解题思路
---
### 使用方法：暴力法
---
### 题目关键信息
1. 给出2个版本号version1和version2，比较它们的大小
2. 版本号是由修订号组成，修订号与修订号之间由一个"."连接
3. 修订号可能有前导0，按从左到右的顺序依次比较它们的修订号，比较修订号时，只需比较忽略任何前导零后的整数值
4. 如果版本号没有指定某个下标处的修订号，则该修订号视为0
5. 版本号中每一节可能超过int的表达范围


---
### 解题步骤
1. 计算两个版本的长度
2. 设置双指针
3. 当任一指针超出版本长度后 停止
4. 创建临时变量用来存储整理后的版本1
5. 从下一个点前截取数字
6. 跳过点 
7. 创建临时变量用来存储整理后的版本2
8. 从下一个点前截取数字
9. 跳过点
10. 比较数字大小
11. 版本号相同
---

### 最终代码
```
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write code here

        n1 = len(version1)
        n2 = len(version2)

        i, j = 0, 0

        while i < n1 or j < n2:
            num1 = 0

            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1            
            i += 1

            num2 = 0

            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1
            j += 1

            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
            
        return 0
```