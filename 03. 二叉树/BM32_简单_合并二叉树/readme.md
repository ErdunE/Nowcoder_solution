## BM32_简单_合并二叉树

#### 题目链接 [BM32_简单_合并二叉树](https://www.nowcoder.com/practice/7298353c24cc42e3bd5f0e0bd3d1d759?tpId=295&tqId=1025038&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/ck95c3T/20230810132510.png)
![img](https://i.ibb.co/S015XP6/20230810132524.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 合并（相加）二叉树位置相同的节点
2. 缺少的节点用另一棵树来补，若都缺则返回NULL

---
### 解题步骤

1. 首先判断t1与t2是否为空，若为则用另一个代替，若都为空，返回的值也是空。
2. 然后依据前序遍历的特点，优先访问根节点，将两个根点的值相加创建到新树中。
3. 两棵树再依次同步进入左子树和右子树。
---

### 最终代码
```
import java.util.*;
public class Solution {
    public TreeNode mergeTrees (TreeNode t1, TreeNode t2) {
        // write code here
        //若只有一个节点返回另一个，两个都为null自然返回null
        if(t1 == null){
            return t2;
        }
        if(t2 == null){
            return t1;
        }
        //根左右的方式递归
        TreeNode head = new TreeNode(t1.val + t2.val);
        head.left = mergeTrees(t1.left, t2.left);
        head.right = mergeTrees(t1.right, t2.right);

        return head;
    }
}
```