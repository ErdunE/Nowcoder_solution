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
     * @return int整型ArrayList<ArrayList<>>
     */
    //记录输出
    ArrayList<ArrayList<Integer>> res = new ArrayList();
    void traverse(TreeNode root, int depth){
        if(root != null){
            //新的一层
            if(res.size() < depth){
                ArrayList<Integer> row = new ArrayList();
                res.add(row);
                row.add(root.val);
            //读取该层的一维数组，将元素加入末尾
            }else{
                ArrayList<Integer> row = res.get(depth - 1);
                row.add(root.val);
            }
        }else{
            return;
        }
        //递归左右时深度记得加1
        traverse(root.left, depth + 1);
        traverse(root.right, depth + 1);
    }

    public ArrayList<ArrayList<Integer>> levelOrder (TreeNode root) {
        // write code here
        //如果是空，则直接返回
        if(root == null){
            return res;
        }
        //递归层次遍历
        traverse(root, 1);
        return res;
    }
}