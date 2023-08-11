## BM24_中等_二叉树的中序遍历

#### 题目链接 [BM24_中等_二叉树的中序遍历](https://www.nowcoder.com/practice/0bf071c135e64ee2a027783b80bf781d?tpId=295&tqId=1512964&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/7gdGSHL/20230810125910.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 给定一颗二叉树的根节点，输出其中序(左根右)遍历的结果

---
### 解题步骤

1. 准备数组用来记录遍历到的节点值
2. 从根节点开始进入递归，遇到空节点就返回，否则优先进入左子树进行递归访问。
3. 左子树访问完毕再回到根节点访问。
4. 最后进入根节点的右子树进行递归。
---

### 最终代码
```
import java.util.*;
public class Solution {

    public void inorder(List<Integer> list, TreeNode root){
        // 遇到空节点则返回
        if(root == null){
            return;
        }
        // 先去左子树
        inorder(list, root.left);
        // 再访问根节点
        list.add(root.val);
        // 最后去右子树
        inorder(list, root.right);
    }


    public int[] inorderTraversal (TreeNode root) {
        // write code here
        // 添加遍历结果的数组
        List<Integer> list = new ArrayList();
        // 递归中序遍历
        inorder(list, root);
        // 返回的结果
        int[] res = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            res[i] = list.get(i);
        }

        return res;
    }
}
```