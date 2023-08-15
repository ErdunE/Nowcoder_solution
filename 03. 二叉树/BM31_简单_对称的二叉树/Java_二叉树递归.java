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
     * @param pRoot TreeNode类 
     * @return bool布尔型
     */
    boolean recursion(TreeNode root1, TreeNode root2){
        // 可以两个都为空
        if(root1 == null & root2 == null){
            return true;
        }
        // 只有一个为空或者节点值不同，必定不对称
        if(root1 == null || root2 == null || root1.val != root2.val){
            return false;
        }
        // 每层对应的节点进入递归比较
        return recursion(root1.left, root2.right) && recursion(root1.right, root2.left);
    }
    public boolean isSymmetrical (TreeNode pRoot) {
        // write code here

        return recursion(pRoot, pRoot);
    }
}