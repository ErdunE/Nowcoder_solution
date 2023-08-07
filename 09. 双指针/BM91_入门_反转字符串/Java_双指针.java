import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 反转字符串
     * @param str string字符串 
     * @return string字符串
     */
    public String solve (String str) {
        // write code here
        char[] s = str.toCharArray();
        //左右双指针
        int left = 0;
        int right = str.length() - 1;
        //两指针往中间靠
        while(left < right){
            char c = s[left];
            //交换位置
            s[left] = s[right];
            s[right] = c;
            left++;
            right--;
        }

        return new String(s);
    }
}