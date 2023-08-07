import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param arr int整型一维数组 the array
     * @return int整型
     */
    public int maxLength (int[] arr) {
        // write code here
        // 空字符串
        if(arr.length == 0){
            return 0;
        }
        
        int len = arr.length;
        List<Integer> list = new ArrayList<>();
        int count = 0;

        for(int i = 0; i < len; i++){
            // 找出以i位置开头的最长的不重复子串
            for(int j = i; j < len; j++){
                if(list.contains(arr[j])){ // 有重复的就退出循环
                    break;
                }else{
                    list.add(arr[j]); // 不重复就一直add
                }
            }
            // 计算最大不重复子串
            count = Math.max(count, list.size());
            // 当count大于等于剩下的长度时就不再遍历了
            if(count >= len - 1 - i){
                break;
            }
            // 清空记录
            list.clear();
        }
        return count;
    }
}