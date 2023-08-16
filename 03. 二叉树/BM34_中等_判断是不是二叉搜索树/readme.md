## BM34_中等_判断是不是二叉搜索树

#### 题目链接 [BM34_中等_判断是不是二叉搜索树](https://www.nowcoder.com/practice/a69242b39baf45dea217815c7dedb52b?tpId=295&tqId=2288088&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/D1rrz1P/20230810133058.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 判断给定的一棵二叉树是否是二叉搜索树
2. 二叉搜索树每个左子树元素小于根节点，每个右子树元素大于根节点，中序遍历为递增序

---
### 解题步骤

1. 首先递归到最左，初始化maxLeft与pre。
2. 然后往后遍历整棵树，依次连接pre与当前节点，并更新pre。
3. 左子树如果不是二叉搜索树返回false。
4. 判断当前节点是不是小于前置节点，更新前置节点。
5. 最后由右子树的后面节点决定。
---

### 最终代码
```
import java.util.*;
public class Solution {
    int pre = Integer.MIN_VALUE;
    //中序遍历
    public boolean isValidBST (TreeNode root) {
        // write code here
        if(root == null){
            return true;
        }
        //先进入左子树
        if(!isValidBST(root.left)){
            return false;
        }
        if(root.val < pre){
            return false;
        }
        //更新最值
        pre = root.val;
        //再进入右子树
        return isValidBST(root.right);
        
    }
}
```