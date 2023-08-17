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
     * @param o1 int整型 
     * @param o2 int整型 
     * @return int整型
     */
    //记录是否找到到o的路径
    public boolean flag = false;
    //求得根节点到目标节点的路径
    public void dfs(TreeNode root, ArrayList<Integer> path, int o){
        if(flag || root == null){
            return;
        }
        path.add(root.val);
        //节点值都不同，可以直接用值比较
        if(root.val == o){
            flag = true;
        }
        //dfs遍历查找
        dfs(root.left, path, o);
        dfs(root.right, path, o);
        //找到
        if(flag){
            return;
        }
        //回溯
        path.remove(path.size() - 1);
    }
    public int lowestCommonAncestor (TreeNode root, int o1, int o2) {
        // write code here
        ArrayList<Integer> path_o1 = new ArrayList<Integer>();
        ArrayList<Integer> path_o2 = new ArrayList<Integer>();
        //求根节点到两个节点的路径
        dfs(root, path_o1, o1);
        //重置flag，查找下一个
        flag = false;
        dfs(root, path_o2, o2);
        int res = 0;
        //比较两个路径，找到第一个不同的点
        for(int i = 0; i < path_o1.size() && i < path_o2.size(); i++){
            int x = path_o1.get(i);
            int y = path_o2.get(i);
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