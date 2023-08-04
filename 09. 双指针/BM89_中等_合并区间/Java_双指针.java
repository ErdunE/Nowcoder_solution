import java.util.*;

/*
 * public class Interval {
 *   int start;
 *   int end;
 *   public Interval(int start, int end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param intervals Interval类ArrayList 
     * @return Interval类ArrayList
     */
    public ArrayList<Interval> merge (ArrayList<Interval> intervals) {
        // write code here

        // 首先根据start排序，如果start相等，根据end排序
        Collections.sort(intervals, (o1, o2) -> (o1.start != o2.start ? o1.start - o2.start : o1.end - o2.end));
        ArrayList<Interval> res = new ArrayList();
        if(intervals.size() == 0)
            return res;

        // 放入第一个区间
        res.add(intervals.get(0));
        int count = 0;

        // 遍历后续区间，查看是否与末尾有重叠
        for(int i = 1; i < intervals.size(); i++){
            Interval o1 = intervals.get(i);
            Interval oright = res.get(res.size() - 1);
            // 如果当前Interval的start比List里面最后一个元素的end大，说明从开一个区间
            if(o1.start > oright.end){
                res.add(o1);
                count++;
            }else{  // 区间有重叠，更新结尾
                if(o1.end > oright.end){
                    res.get(res.size() - 1).end = o1.end;
                }
            }
        }


        return res;
    }
}