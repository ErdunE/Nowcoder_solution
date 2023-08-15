## BM31_简单_对称的二叉树

#### 题目链接 [BM31_简单_对称的二叉树](https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=295&tqId=23452&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/YcjLX1g/20230810132216.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 判断一棵二叉树是否是镜像，即判断二叉树是否是轴对称图形

---
### 解题步骤

1. 两种方向的前序遍历，同步过程中的当前两个节点，同为空，属于对称的范畴。
2. 当前两个节点只有一个为空或者节点值不相等，已经不是对称的二叉树了。
3. 第一个节点的左子树与第二个节点的右子树同步递归对比，第一个节点的右子树与第二个节点的左子树同步递归比较。
---

### 最终代码
```
import java.util.*;
public class Solution {
    boolean recursion(TreeNode root1, TreeNode root2){
        // 可以两个都为空
        if(root1 == null & root2 == null){
            return true;
        }
        // 只有一个为空或者节点值不同，必定不对称
        if(root1 == null || root2 == null || root1.val != root2.val){
            return false;
        }
        // 每层对应的节点进入递归比较
        return recursion(root1.left, root2.right) && recursion(root1.right, root2.left);
    }
    public boolean isSymmetrical (TreeNode pRoot) {
        // write code here

        return recursion(pRoot, pRoot);
    }
}
```