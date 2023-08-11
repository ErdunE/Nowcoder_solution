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
     * @return int整型一维数组
     */

    public void pastorder(List<Integer> list, TreeNode root){
        // 遇到空节点则返回
        if(root == null){
            return;
        }
        //先去左子树
        pastorder(list, root.left);
        //再去右子树
        pastorder(list, root.right);
        //最后访问根节点
        list.add(root.val);
    }

    public int[] postorderTraversal (TreeNode root) {
        // write code here
        //添加遍历结果的数组
        List<Integer> list = new ArrayList();
        //递归后序遍历
        pastorder(list, root);
        //返回的结果
        int[] res = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            res[i] = list.get(i);
        }
        return res;
    }
}