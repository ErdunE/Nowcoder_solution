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
     * @param p int整型 
     * @param q int整型 
     * @return int整型
     */
    //求得根节点到目标节点的路径
    public ArrayList<Integer> getPath(TreeNode root, int target){
        ArrayList<Integer> path = new ArrayList<Integer>();
        TreeNode node = root;
        //节点值都不同，可以直接用值比较
        while(node.val != target){
            path.add(node.val);
            //小的在左子树
            if(target < node.val){
                node = node.left;
            }else{ //大的在右子树
                node = node.right;
            }
        }
        path.add(node.val);
        return path;
    }

    public int lowestCommonAncestor (TreeNode root, int p, int q) {
        // write code here
        //求根节点到两个节点的路径
        ArrayList<Integer> path_p = getPath(root, p);
        ArrayList<Integer> path_q = getPath(root, q);
        int res = 0;
        //比较两个路径，找到第一个不同的点
        for(int i = 0; i < path_p.size() && i < path_q.size(); i++){
            int x = path_p.get(i);
            int y = path_q.get(i);
            //最后一个相同的节点就是最近公共祖先
            if(x == y){
                res = x;
            }else{
                break;
            }   
        }
        return res;
    }
}