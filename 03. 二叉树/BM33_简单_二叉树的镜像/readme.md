## BM33_简单_二叉树的镜像

#### 题目链接 [BM33_简单_二叉树的镜像](https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?tpId=295&tqId=1374963&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/Rvwt678/20230810132840.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 将二叉树镜像，即将其所有左右子树交换

---
### 解题步骤

1. 先深度最左端的节点，遇到空树返回，处理最左端的两个子节点交换位置。
2. 然后进入右子树，继续按照先左后右再回中的方式访问。
3. 再返回到父问题，交换父问题两个子节点的值。
---

### 最终代码
```
import java.util.*;
public class Solution {
    public TreeNode Mirror (TreeNode pRoot) {
        // write code here

        // 空树返回
        if(pRoot == null){
            return null;
        }
        // 先递归子树
        TreeNode left = Mirror(pRoot.left);
        TreeNode right = Mirror(pRoot.right);
        // 交换
        pRoot.left = right;
        pRoot.right = left;

        return pRoot;
```