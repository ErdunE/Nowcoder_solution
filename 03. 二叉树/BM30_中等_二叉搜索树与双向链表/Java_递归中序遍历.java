import java.util.*;
/**
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
    //返回的第一个指针，即为最小值，先定为null
    public TreeNode head = null;
    //中序遍历当前值的上一位，初值为最小值，先定为null
    public TreeNode pre = null;
    public TreeNode Convert(TreeNode pRootOfTree) {
        if(pRootOfTree == null){
            //中序递归，叶子为空则返回
            return null;
        }
        //首先递归到最左最小值 
        Convert(pRootOfTree.left);
        //找到最小值，初始化head与pre       
        if(pre == null){
            head = pRootOfTree;
            pre = pRootOfTree;
        }else{  //当前节点与上一节点建立连接，将pre设置为当前值
            pre.right = pRootOfTree;
            pRootOfTree.left = pre;
            pre = pRootOfTree;
        }
        Convert(pRootOfTree.right);
        return head;
    }
}
