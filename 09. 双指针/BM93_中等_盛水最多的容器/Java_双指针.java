import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param height int整型一维数组 
     * @return int整型
     */
    public int maxArea (int[] height) {
        // write code here

        int n = height.length;

        if(n < 2){
            return 0;
        }

        int left = 0;
        int right = n - 1;
        int res = 0;

        while(left < right){
            int capacity = Math.min(height[left], height[right]) * (right - left);
            res = Math.max(res, capacity);

            if(height[left] < height[right]){
                left++;
            }else{
                right--;
            }
        }
        return res;
    }
}