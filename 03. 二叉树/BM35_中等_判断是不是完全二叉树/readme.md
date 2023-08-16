## BM35_中等_判断是不是完全二叉树

#### 题目链接 [BM35_中等_判断是不是完全二叉树](https://www.nowcoder.com/practice/8daa4dff9e36409abba2adbe413d6fae?tpId=295&tqId=2299105&ru=/exam/interview&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Finterview%3Forder%3D0)

![img](https://i.ibb.co/xmyPgt7/20230810133230.png)
![img](https://i.ibb.co/qWKvT2Q/20230810133239.png)

---
## 解题思路
---
### 使用方法：队列
---
### 题目关键信息

1. 判断给定二叉树是否为完全二叉树
2. 首先我们需要知道什么是完全二叉树：叶子节点只能出现在最下层和次下层，且最下层的叶子节点集中在树的左部。
3. 需要注意的是，满二叉树肯定是完全二叉树，而完全二叉树不一定是满二叉树。

---
### 解题步骤

1. 先判断空树一定是完全二叉树。
2. 初始化一个队列辅助层次遍历，将根节点加入。
3. 逐渐从队列中弹出元素访问节点，如果遇到某个节点为空，进行标记，代表到了完全二叉树的最下层，若是后续还有访问，则说明提前出现了叶子节点，不符合完全二叉树的性质。
4. 否则，继续加入左右子节点进入队列排队，等待访问。
---

### 最终代码
```
import java.util.*;
public class Solution {
    public boolean isCompleteTree (TreeNode root) {
        // write code here
        //空树一定是完全二叉树
        if(root == null){
            return true;
        }
        // 辅助队列
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        TreeNode cur;
        //定义一个首次出现的标记位
        boolean notComplete = false;
        while(!queue.isEmpty()){
            //标记第一次遇到空节点
            cur = queue.poll();
            if(cur == null){
                notComplete = true;
                continue;
            }
            //后续访问已经遇到空节点了，说明经过了叶子
            if(notComplete){
                return false;
            }
            queue.offer(cur.left);
            queue.offer(cur.right);
        }
        return true;

    }
}
```