## BM23_简单_二叉树的前序遍历

#### 题目链接 [BM23_简单_二叉树的前序遍历](https://www.nowcoder.com/practice/5e2135f4d2b14eb8a5b06fab4c938635?tpId=295&tqId=2291302&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/BtL6pm7/20230810110749.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 给定一颗二叉树的根节点，输出其前序(根左右)遍历的结果

---
### 解题步骤

1. 准备数组用来记录遍历到的节点值
2. 从根节点开始进入递归，遇到空节点就返回，否则将该节点值加入数组
3. 依次进入左右子树进行递归
---

### 最终代码
```
import java.util.*;
public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param root TreeNode类 
     * @return int整型一维数组
     */

    public void preorder(List<Integer> list, TreeNode root){
        // 遇到空节点则返回
        if(root == null){
            return;
        }
        // 先遍历根节点
        list.add(root.val);
        // 再去左子树
        preorder(list, root.left);
        // 最后去右子树
        preorder(list, root.right);

    } 

    public int[] preorderTraversal (TreeNode root) {
        // write code here
        // 添加遍历结果的数组
        List<Integer> list = new ArrayList();
        // 递归前序遍历
        preorder(list, root);
        // 返回的结果
        int[] res = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            res[i] = list.get(i);
        }
        return res;
    }
}
```