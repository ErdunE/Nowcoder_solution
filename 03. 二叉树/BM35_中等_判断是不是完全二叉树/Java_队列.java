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
    public boolean isCompleteTree (TreeNode root) {
        // write code here
        //空树一定是完全二叉树
        if(root == null){
            return true;
        }
        // 辅助队列
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        TreeNode cur;
        //定义一个首次出现的标记位
        boolean notComplete = false;
        while(!queue.isEmpty()){
            //标记第一次遇到空节点
            cur = queue.poll();
            if(cur == null){
                notComplete = true;
                continue;
            }
            //后续访问已经遇到空节点了，说明经过了叶子
            if(notComplete){
                return false;
            }
            queue.offer(cur.left);
            queue.offer(cur.right);
        }
        return true;

    }
}