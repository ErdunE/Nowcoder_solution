#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str: str) -> bool:
        # write code here
        
        # 设置双指针在字符串首，尾
        lens = len(str)
        i = 0
        j = lens - 1
        
        # 依次比较是否相同
        while i <= j:
            # 如果不同则返回False
            if str[i] != str[j]:
                return False   
            # 如果相同则首指针进1，尾指针退1             
            i = i + 1
            j = j - 1
        # 直到双指针在一样位置时候，循环暂停并返回True
        return True