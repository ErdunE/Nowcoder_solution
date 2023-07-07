## BM83_简单_字符变形串

#### 题目链接 [BM83_简单_字符变形串](https://www.nowcoder.com/practice/28eb3175488f4434a4a6207f6f484f47?tpId=295&tqId=732&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj)

![img](https://i.ibb.co/Xsk63sP/20230707130530.png)

---
## 解题思路
---
### 使用方法：双逆转
---
### 题目关键信息

1. 将字符串大小写反转
2. 将整个字符串的所有单词位置反转

---
### 解题步骤

1. 遍历字符串，遇到小写字母，转换成大写，遇到大写字母，转换成小写，遇到空格正常不变。
2. 第一次反转整个字符串，这样基本的单词逆序就有了，但是每个单词的字符也是逆的。
3. 再次遍历字符串，以每个空间为界，将每个单词反转回正常。
---

### 最终代码
```
class Solution:
    def trans(self , s: str, n: int) -> str:
        # write code here

        if n==0:
            return s
        res = ""
        for i in range(n):
            #大小写转换
            if s[i] <= 'Z' and s[i] >= 'A': 
                res += chr(ord(s[i]) - ord('A') + ord('a'))
            elif s[i] >= 'a' and s[i] <= 'z':
                res += chr(ord(s[i]) - ord('a') + ord('A'))
            else :
                #空格直接复制
                res+=s[i] 
        #单词反序
        res = list(res.split(' '))[::-1]
        print(res)
        return ' '.join(res)
```