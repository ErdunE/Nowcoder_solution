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
    //计算该子树深度函数
    public int deep(TreeNode root){
        //空节点深度为0
        if(root == null){
            return 0;
        }
        //递归算左右子树的深度
        int left = deep(root.left);
        int right = deep(root.right);
        //子树最大深度加上自己
        return (left > right) ? left + 1 : right + 1;
    }
    public boolean IsBalanced_Solution (TreeNode pRoot) {
        // write code here
        //空树为平衡二叉树
        if(pRoot == null){
            return true;
        }
        int left = deep(pRoot.left);
        int right = deep(pRoot.right);
        //左子树深度减去右子树相差绝对值大于1
        if(left - right > 1 || left - right < -1){
            return false;
        }
        //同时，左右子树还必须是平衡的
        return IsBalanced_Solution(pRoot.left) && IsBalanced_Solution(pRoot.right);
    }
}