import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * max water
     * @param arr int整型一维数组 the array
     * @return long长整型
     */
    public long maxWater (int[] arr) {
        // write code here

        int n = arr.length;

        if(n < 1){
            return 0;
        }

        int res = 0;
        int left = 0;
        int right = n - 1;
        int maxL = 0;
        int maxR = 0;

        while(left < right){
            maxL = Math.max(maxL, arr[left]);
            maxR = Math.max(maxR, arr[right]);

            if(maxL < maxR){
                res = res + maxL - arr[left];
                left++;
            }else{
                res =  res + maxR - arr[right];
                right--;
            }
        }
        return res;
    }
}