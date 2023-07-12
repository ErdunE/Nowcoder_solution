#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param S string字符串 
# @param T string字符串 
# @return string字符串
#

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
        
               