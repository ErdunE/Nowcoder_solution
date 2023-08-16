## BM36_简单_判断是不是平衡二叉树

#### 题目链接 [BM36_简单_判断是不是平衡二叉树](https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=295&tqId=23250&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/gMHLdjZ/20230810133403.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 判断给出的二叉树是否是平衡二叉树
2. 需要判断任意一节点两边子树深度相差是否绝对值大于1，同时它的子树也符合平衡二叉树的规则

---
### 解题步骤

1. 第一个函数递归遍历二叉树所有节点。
2. 对于每个节点判断，调用第二个函数获取子树深度。
3. 第二个函数递归获取子树深度，只需要不断往子节点深度遍历，累加左右深度的较大值。
4. 根据深度判断该节点下的子树是否为平衡二叉树。
---

### 最终代码
```
import java.util.*;
public class Solution {
    //计算该子树深度函数
    public int deep(TreeNode root){
        //空节点深度为0
        if(root == null){
            return 0;
        }
        //递归算左右子树的深度
        int left = deep(root.left);
        int right = deep(root.right);
        //子树最大深度加上自己
        return (left > right) ? left + 1 : right + 1;
    }
    public boolean IsBalanced_Solution (TreeNode pRoot) {
        // write code here
        //空树为平衡二叉树
        if(pRoot == null){
            return true;
        }
        int left = deep(pRoot.left);
        int right = deep(pRoot.right);
        //左子树深度减去右子树相差绝对值大于1
        if(left - right > 1 || left - right < -1){
            return false;
        }
        //同时，左右子树还必须是平衡的
        return IsBalanced_Solution(pRoot.left) && IsBalanced_Solution(pRoot.right);
    }
}
```