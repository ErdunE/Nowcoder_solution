## BM29_简单_二叉树中和为某一值的路径(一)

#### 题目链接 [BM29_简单_二叉树中和为某一值的路径(一)](https://www.nowcoder.com/practice/508378c0823c423baa723ce448cbfd0c?tpId=295&tqId=634&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/dmyMRMM/20230810131526.png)

---
## 解题思路
---
### 使用方法：
---
### 题目关键信息

1. 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径
2. 路径定义为从树的根节点开始往下一直到叶子节点所经过的节点
3. 路径只能从父节点到子节点，不能从子节点到父节点

---
### 解题步骤

1. 每次检查遍历到的节点是否为空节点，空节点就没有路径。
2. 再检查遍历到是否为叶子节点，且当前sum值等于节点值，说明可以刚好找到。
3. 检查左右子节点是否可以有完成路径的，如果任意一条路径可以都返回true，因此这里选用两个子节点递归的或。
---

### 最终代码
```
import java.util.*;
public class Solution {
    public boolean hasPathSum (TreeNode root, int sum) {
        // write code here
        //空节点找不到路径
        if(root == null){
            return false;
        }
        //叶子节点，且路径和为sum
        if(root.left == null && root.right == null && sum - root.val == 0){
            return true;
        }
        //递归进入子节点
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
```