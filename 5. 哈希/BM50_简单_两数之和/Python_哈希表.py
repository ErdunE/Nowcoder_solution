#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
#
class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # write code here

        # 创建结果变量
        res = []
        # 创建哈希表,两元组分别表示值、下标
        hash = dict()

        # 在哈希表中查找target-numbers[i]
        for i in range(len(numbers)):
            temp = target - numbers[i]
            
            if temp not in hash:
                # 如果哈希表中没有临时变量，给哈希表中当前值加入下标
                hash[numbers[i]] = i            
            else:
                # 如果哈希表中有临时变量，将哈希表中临时变量的下标+1
                res.append(hash[temp]+1)
                # 将当前值下标+1
                res.append(i+1)
                break
        return res