## BM37_简单_二叉搜索树的最近公共祖先

#### 题目链接 [BM37_简单_二叉搜索树的最近公共祖先](https://www.nowcoder.com/practice/d9820119321945f588ed6a26f0a6991f?tpId=295&tqId=2290592&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/rZnhWM8/20230810133504.png)

---
## 解题思路
---
### 使用方法：搜索路径比较
---
### 题目关键信息

1. 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先
2. 对于该题的最近的公共祖先定义：对于有根树T的两个节点p、q，最近公共祖先LCA(T,p,q)表示一个节点x，满足x是p和q的祖先且x的深度尽可能大
3. 一个节点也可以是它自己的祖先
4. 二叉搜索树是若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值
5. 所有节点的值都是唯一的，可以通过节点值直接比较
6. p、q 为不同节点且均存在于给定的二叉搜索树中

---
### 解题步骤

1. 根据二叉搜索树的性质，从根节点开始查找目标节点，当前节点比目标小则进入右子树，当前节点比目标大则进入左子树，直到找到目标节点。这个过程成用数组记录遇到的元素。
2. 分别在搜索二叉树中找到p和q两个点，并记录各自的路径为数组。
3. 同时遍历两个数组，比较元素值，最后一个相等的元素就是最近的公共祖先。
---

### 最终代码
```
import java.util.*;
public class Solution {
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
```