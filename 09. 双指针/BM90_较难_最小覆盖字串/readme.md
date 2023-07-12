## BM90_较难_最小覆盖字串

#### 题目链接 [BM90_较难_最小覆盖字串](https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=295&tqId=670&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295)

![img](https://i.ibb.co/9NvHcyZ/20230627102459.png)

---
## 解题思路
---
### 使用方法：双指针+哈希表
---
### 题目关键信息

1. 两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串

---
### 解题步骤
1. 创建哈希表用来装分别需要的字符数量，包括必要的和非必要的，需要的必要字符数量>0，非必要的字符数量<0
2. 初始化需要的必要字符数量
3. 创建变量用来判断总共需要多少字符才能达到要求
4. 只有必要字符的数量才可能>0
5. 任意值都可以装进need_dict，但是非必要字符只可能<0
6. 如果需要的字符都足够了 
7. 开始准备右移左指针，缩短距离 
8. 如果字符串更短，替换答案
9. 在移动左指针之前先将左指针的值加回来，这里可以是非必要字符
10. 确认是必要字符且不多于所需要的数量（有多余的话只可能<=0，因为上一句我们已经将字符+1了）后，将need_cnt+1
11. 右移左指针，寻找下一个符合的子串 
---

### 最终代码
```
import collections

class Solution:
    def minWindow(self , S: str, T: str) -> str:
        # write code here

        # 用来装分别需要的字符数量，包括必要的和非必要的，需要的必要字符数量>0，非必要的字符数量<0
        need_dict = collections.defaultdict(int) 
        # 初始化需要的必要字符数量
        for ch in T:   
            need_dict[ch] += 1
        # 用来判断总共需要多少字符才能达到要求
        need_cnt = len(T) 

        i = j = 0
        res = [0,float('inf')]

        for j in range(len(S)):
            # 只有必要字符的数量才可能>0
            if need_dict[S[j]] > 0: 
                need_cnt -= 1
            # 任意值都可以装进need_dict，但是非必要字符只可能<0
            need_dict[S[j]] -= 1 
            # 需要的字符都足够了 
            if need_cnt == 0: 
                # 开始准备右移左指针，缩短距离 
                while need_cnt == 0: 
                    # 字符串更短，替换答案
                    if j-i < res[1] - res[0]: 
                        res = [i,j]
                    # 在移动左指针之前先将左指针的值加回来，这里可以是非必要字符
                    need_dict[S[i]] += 1    
                    # 确认是必要字符且不多于所需要的数量（有多余的话只可能<=0，因为上一句我们已经将字符+1了）后，将need_cnt+1
                    if S[i] in T and need_dict[S[i]] > 0: 
                        need_cnt += 1   
                    # 右移左指针，寻找下一个符合的子串 
                    i += 1   
        return S[res[0]:res[1]+1] if res[1]-res[0]<len(S) else ''  
```