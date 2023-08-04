import java.util.*;
public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        

        int i = m - 1;
        int j = n - 1;
        int q = m + n - 1;

        while(i >= 0 && j >= 0){
            if(A[i] > B[j])
                A[q--] = A[i--];
            else
                A[q--] = B[j--];        
        }

        if(i < 0){
            while(j >= 0){
                A[q--] = B[j--];
            }
        }
    }
}
             


