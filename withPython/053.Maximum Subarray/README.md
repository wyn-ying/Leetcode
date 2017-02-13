###idea
���ȣ��������ǰ�����������ö�̬�滮(DP)�ܴﵽOn���϶������ģ����Ǿ���д��һ��֮ǰ������DP���㷨����д�����test cases���ж��Ǹ����������
�����뵽���Լ�¼���ֵ��������ֵΪ����ֱ�ӷ��ظ�ֵ���У����Ϊ������֮ǰд�����ߴ��������С�

֮���ֳ����ٶ�beat��99%�����ѣ��ٻ�ͷ��������more practiceҪ�����On���㷨���ٿ��Ƿ��η�����

��֮��������η����񻹲���ô����д����������ʱ���ٲ�һ����

###hot solution
���ȣ�ͬ���Ƕ�̬�滮�������java�����ڴ���������ʱ���Եø���ࡣ
```java
public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
        dp[0] = A[0];
        int max = dp[0];

        for(int i = 1; i < n; i++){
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);//code in (...) is the point
            max = Math.max(max, dp[i]);
        }

        return max;
}

```
��������python���DP�㷨��
```python
class Solution(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
```
��ִ��Ч�ʲ����ߣ�������Ҫ����Ϊʹ����max������

�������÷��η��Ĳ�ռ��������Ż�����Ϊ���ɡ������������η���java���룬��Դ��һ�������е�[��Ʊ�ش�](https://leetcode.com/discuss/694/how-solve-maximum-subarray-using-divide-and-conquer-approach)��������ϸ˵������΢ѧϰһ�¡�
```java
class Solution {
public:
    int maxSubArray(int A[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(n==0) return 0;
        return maxSubArrayHelperFunction(A,0,n-1);
    }

    int maxSubArrayHelperFunction(int A[], int left, int right) {
        if(right == left) return A[left];
        int middle = (left+right)/2;
        int leftans = maxSubArrayHelperFunction(A, left, middle);
        int rightans = maxSubArrayHelperFunction(A, middle+1, right);
        int leftmax = A[middle];
        int rightmax = A[middle+1];
        int temp = 0;
        for(int i=middle;i>=left;i--) {
            temp += A[i];
            if(temp > leftmax) leftmax = temp;
        }
        temp = 0;
        for(int i=middle+1;i<=right;i++) {
            temp += A[i];
            if(temp > rightmax) rightmax = temp;
        }
        return max(max(leftans, rightans),leftmax+rightmax);
    }
};
```
###time consuming
#####my solution
44ms-->98.80%
#####hot solution
60ms-->33.85%