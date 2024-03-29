## BM38_中等_在二叉树中找到两个节点的最近公共祖先

#### 题目链接 [BM38_中等_在二叉树中找到两个节点的最近公共祖先](https://www.nowcoder.com/practice/e0cc33a83afe4530bcec46eba3325116?tpId=295&tqId=1024325&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/xJvLSgC/20230810134041.png)

---
## 解题思路
---
### 使用方法：深度优先搜索（dfs）
---
### 题目关键信息

1. 给定一棵二叉树以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点
2. 二叉树非空，且每个节点值均不同

---
### 解题步骤

1. 利用dfs求得根节点到两个目标节点的路径：每次选择二叉树的一棵子树往下找，同时路径数组增加这个遍历的节点值。
2. 一旦遍历到了叶子节点也没有，则回溯到父节点，寻找其他路径，回溯时要去掉数组中刚刚加入的元素。
3. 然后遍历两条路径数组，依次比较元素值。
4. 找到两条路径第一个不相同的节点即是最近公共祖先。
---

### 最终代码
```
import java.util.*;
public class Solution {
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
```