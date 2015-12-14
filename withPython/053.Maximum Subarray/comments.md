###idea
首先，这个题以前见过，并且用动态规划(DP)能达到On，肯定是最快的，于是就先写了一个之前背过的DP的算法。但写完后发现test cases中有都是负数的情况。
后来想到可以记录最大值，如果最大值为负则直接返回负值就行，如果为正，则按之前写的在线处理程序进行。

之后发现程序速度beat了99%的网友，再回头看发现有more practice要求除了On的算法，再考虑分治法……

再之后想想分治法好像还不那么容易写出来……有时间再补一个，

###hot solution
首先，同样是动态规划，下面的java代码在处理正负的时候显得更简洁。
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
下面贴个python版的DP算法：
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
但执行效率并不高，可能主要是因为使用了max函数。

讨论区用分治法的不占主流，大概还是因为慢吧。下面贴个分治法的java代码，来源于一个问题中的[高票回答](https://leetcode.com/discuss/694/how-solve-maximum-subarray-using-divide-and-conquer-approach)，还有详细说明，稍微学习一下。
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