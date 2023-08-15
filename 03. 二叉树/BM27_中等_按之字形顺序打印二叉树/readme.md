## BM28_简单_二叉树的最大深度

#### 题目链接 [BM28_简单_二叉树的最大深度](https://www.nowcoder.com/practice/8a2b2bf6c19b4f23a9bdb9b233eefa73?tpId=295&tqId=642&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/mR3F09P/20230810131332.png)

---
## 解题思路
---
### 使用方法：非递归层次遍历
---
### 题目关键信息

1. 给定一个二叉树，返回该二叉树的之字形层序遍
2. 第一层从左向右，下一层从右向左，一直这样交替


---
### 解题步骤

1. 首先判断二叉树是否为空，空树没有打印结果。
2. 建立辅助队列，根节点首先进入队列。不管层次怎么访问，根节点一定是第一个，那它肯定排在队伍的最前面，初始化flag变量。
3. 每次进入一层，统计队列中元素的个数，更改flag变量的值。因为每当访问完一层，下一层作为这一层的子节点，一定都加入队列，而再下一层还没有加入，因此此时队列中的元素个数就是这一层的元素个数。
4. 每次遍历这一层这么多的节点数，将其依次从队列中弹出，然后加入这一行的一维数组中，如果它们有子节点，依次加入队列排队等待访问。
5. 访问完这一层的元素后，根据flag变量决定将这个一维数组直接加入二维数组中还是反转后再加入，然后再访问下一层。
   
---

### 最终代码
```
import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> Print (TreeNode pRoot) {
        // write code here

        TreeNode head = pRoot;
        ArrayList<ArrayList<Integer> > res = new ArrayList<ArrayList<Integer>>();
        if(head == null)
            //如果是空，则直接返回空list
            return res;
        //队列存储，进行层次遍历
        Queue<TreeNode> temp = new LinkedList<TreeNode>();
        temp.offer(head);
        TreeNode p;
        boolean flag = true;
        while(!temp.isEmpty()){
            //记录二叉树的某一行
            ArrayList<Integer> row = new ArrayList<Integer>(); 
            int n = temp.size();
            //奇数行反转，偶数行不反转
            flag = !flag;
            //因先进入的是根节点，故每层节点多少，队列大小就是多少
            for(int i = 0; i < n; i++){
                p = temp.poll();
                row.add(p.val);
                //若是左右孩子存在，则存入左右孩子作为下一个层次
                if(p.left != null)
                    temp.offer(p.left);
                if(p.right != null)
                    temp.offer(p.right);
            }
            //奇数行反转，偶数行不反转
            if(flag) 
                Collections.reverse(row);
            res.add(row);
        }
        return res;
    }
}
```