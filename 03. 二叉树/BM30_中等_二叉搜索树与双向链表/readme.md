## BM30_中等_二叉搜索树与双向链表

#### 题目链接 [BM30_中等_二叉搜索树与双向链表](https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=295&tqId=23253&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/kJ2c6Ss/20230810132106.png)

---
## 解题思路
---
### 使用方法：递归中序遍历
---
### 题目关键信息

1. 将二叉搜索树转化成递增序的双向链表
2. 不能添加新的节点，要在原节点基础上添加链表链接
3. 返回链表中的第一个节点的指针
4. 二叉树节点的左右指针看成双向链表的前后指针

---
### 解题步骤

1. 创建两个指针，一个指向题目中要求的链表头（head），一个指向当前遍历的前一节点（pre)。
2. 首先递归到最左，初始化head与pre。
3. 然后处理中间根节点，依次连接pre与当前节点，连接后更新pre为当前节点。
4. 最后递归进入右子树，继续处理。
5. 递归出口即是节点为空则返回。
---

### 最终代码
```
import java.util.*;
public class Solution {
    //返回的第一个指针，即为最小值，先定为null
    public TreeNode head = null;
    //中序遍历当前值的上一位，初值为最小值，先定为null
    public TreeNode pre = null;
    public TreeNode Convert(TreeNode pRootOfTree) {
        if(pRootOfTree == null){
            //中序递归，叶子为空则返回
            return null;
        }
        //首先递归到最左最小值 
        Convert(pRootOfTree.left);
        //找到最小值，初始化head与pre       
        if(pre == null){
            head = pRootOfTree;
            pre = pRootOfTree;
        }else{  //当前节点与上一节点建立连接，将pre设置为当前值
            pre.right = pRootOfTree;
            pRootOfTree.left = pre;
            pre = pRootOfTree;
        }
        Convert(pRootOfTree.right);
        return head;
    }
}

```