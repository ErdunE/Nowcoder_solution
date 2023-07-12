#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @param n int整型 
# @return string字符串
#
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