import java.util.*;

/*
 * public class TreeNode {
 *   int val = 0;
 *   TreeNode left = null;
 *   TreeNode right = null;
 *   public TreeNode(int val) {
 *     this.val = val;
 *   }
 * }
 */

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param root TreeNode类 
     * @return bool布尔型
     */
    int pre = Integer.MIN_VALUE;
    //中序遍历
    public boolean isValidBST (TreeNode root) {
        // write code here
        if(root == null){
            return true;
        }
        //先进入左子树
        if(!isValidBST(root.left)){
            return false;
        }
        if(root.val < pre){
            return false;
        }
        //更新最值
        pre = root.val;
        //再进入右子树
        return isValidBST(root.right);
        
    }
}