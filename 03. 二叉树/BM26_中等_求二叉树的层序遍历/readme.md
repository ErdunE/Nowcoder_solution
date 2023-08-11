## BM26_中等_求二叉树的层序遍历

#### 题目链接 [BM26_中等_求二叉树的层序遍历](https://www.nowcoder.com/practice/04a5560e43e24e9db4595865dc9c63a3?tpId=295&tqId=644&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/Y2Ysv7m/20230810130358.png)

---
## 解题思路
---
### 使用方法：二叉树递归
---
### 题目关键信息

1. 将给定二叉树按行从上到下、从左到右的顺序输出
2. 输出到一个二维数组中，数组中每行就是二叉树的一层

---
### 解题步骤

1. 首先判断二叉树是否为空，空树没有遍历结果。
2. 使用递归进行层次遍历输出，每次递归记录当前二叉树的深度，每当遍历到一个节点，如果为空直接返回。
3. 如果遍历的节点不为空，输出二维数组中一维数组的个数（即代表了输出的行数）小于深度，说明这个节点应该是新的一层，我们在二维数组中增加一个一维数组，然后再加入二叉树元素。
4. 如果不是step 3的情况说明这个深度我们已经有了数组，直接根据深度作为下标取出数组，将元素加在最后就可以了。
5. 处理完这个节点，再依次递归进入左右节点，同时深度增加。因为我们进入递归的时候是先左后右，那么遍历的时候也是先左后右，正好是层次遍历的顺序。
---

### 最终代码
```
import java.util.*;
public class Solution {

    //记录输出
    ArrayList<ArrayList<Integer>> res = new ArrayList();
    void traverse(TreeNode root, int depth){
        if(root != null){
            //新的一层
            if(res.size() < depth){
                ArrayList<Integer> row = new ArrayList();
                res.add(row);
                row.add(root.val);
            //读取该层的一维数组，将元素加入末尾
            }else{
                ArrayList<Integer> row = res.get(depth - 1);
                row.add(root.val);
            }
        }else{
            return;
        }
        //递归左右时深度记得加1
        traverse(root.left, depth + 1);
        traverse(root.right, depth + 1);
    }

    public ArrayList<ArrayList<Integer>> levelOrder (TreeNode root) {
        // write code here
        //如果是空，则直接返回
        if(root == null){
            return res;
        }
        //递归层次遍历
        traverse(root, 1);
        return res;
    }
}
```