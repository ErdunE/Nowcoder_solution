#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# lfu design
# @param operators int整型二维数组 ops
# @param k int整型 the k
# @return int整型一维数组
#
class Cache:
    def __init__(self, k):
        self.cap = k
        self.data = dict()
     
    def getFirstKey(self):
        k = sorted(self.data.items(), key=lambda x:[x[1][1], x[1][2]])[0][0]
        return k
         
    def isFull(self):
        return len(self.data) == self.cap
     
    def setKey(self, key, val, tp):
        if not self.isFull():
            if key not in self.data:
                self.data[key] = [val, 1, tp]
            else:
                self.data[key][0] = val
                self.data[key][1] += 1
                self.data[key][2] = tp
        elif self.isFull() and key in self.data:
            self.data[key][0] = val
            self.data[key][1] += 1
            self.data[key][2] = tp
        else:
            self.data.pop(self.getFirstKey())
            self.data[key] = [val, 1, tp]
     
    def getKey(self, key, tp):
        if key in self.data:
            self.data[key][1] += 1
            self.data[key][2] = tp
        return -1 if key not in self.data else self.data[key][0]    
         
         
class Solution:
    def LFU(self , operators: List[List[int]], k: int) -> List[int]:
        # write code here
        res = []
        cache = Cache(k)
        for i in range(len(operators)):
            if operators[i][0] == 1:
                cache.setKey(operators[i][1], operators[i][2], i)            
            elif operators[i][0] == 2:
                res.append(cache.getKey(operators[i][1],i))
        return res
