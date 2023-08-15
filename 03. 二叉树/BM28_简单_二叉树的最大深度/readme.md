## BM23_简单_二叉树的前序遍历

#### 题目链接 [BM23_简单_二叉树的前序遍历](https://www.nowcoder.com/practice/5e2135f4d2b14eb8a5b06fab4c938635?tpId=295&tqId=2291302&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/BtL6pm7/20230810110749.png)

---
## 解题思路
---
### 使用方法：递归
---
### 题目关键信息

1. 给定一棵二叉树的根节点，求这棵树的最大深度
2. 深度是指树的根节点到任一叶子节点路径上节点的数量
3. 最大深度是所有叶子节点的深度的最大值
4. 叶子节点是指没有子节点的节点

---
### 解题步骤

1. 对于每个节点，若是不为空才能累计一次深度，若是为空，返回深度为0.
2. 递归分别计算左子树与右子树的深度。
3. 当前深度为两个子树深度较大值再加1。
---

### 最终代码
```
import java.util.*;
public class Solution {
    public int maxDepth (TreeNode root) {
        // write code here
        // 空节点没有深度
        if(root == null){
            return 0;
        }
        // 返回子树深度+1
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```