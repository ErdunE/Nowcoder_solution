#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param strs string字符串一维数组 
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        # write code here
        
        #空字符串数组
        if len(strs) == 0:
            return ""
        
        #遍历第一个字符串的长度
        for i in range(len(strs[0])):
            temp = strs[0][i]
            #遍历后续的字符串
            for j in range(1, len(strs)):
                #比较每个字符串该位置是否和第一个相同                
                if i == len(strs[j]) or strs[j][i] != temp:
                    #不相同则结束
                    return strs[0][0:i]
        #后续字符串有整个字一个字符串的前缀
        return strs[0]
