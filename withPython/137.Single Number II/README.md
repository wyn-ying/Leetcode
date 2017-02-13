###idea
常规思路，字典计数，遍历后找计数为1的。

###hot solution
本来以为这是一个正常题目，没想到机智的社区竟然还有能用比特串解决的。
```java
public int singleNumber(int[] A) {
    int ones = 0, twos = 0;
    for(int i = 0; i < A.length; i++){
        ones = (ones ^ A[i]) & ~twos;
        twos = (twos ^ A[i]) & ~ones;
    }
    return ones;
}
```
由于[答案解释](https://leetcode.com/discuss/6632/challenge-me-thx)太精彩，只想贴上原文。
>The code seems tricky and hard to understand at first glance. However, if you consider the problem in Boolean algebra form, everything becomes clear.

>What we need to do is to store the number of '1's of every bit. Since each of the 32 bits follow the same rules, we just need to consider 1 bit. We know a number appears 3 times at most, so we need 2 bits to store that. Now we have 4 state, 00, 01, 10 and 11, but we only need 3 of them.

>In this solution, 00, 01 and 10 are chosen. Let 'ones' represents the first bit, 'twos' represents the second bit. Then we need to set rules for 'ones' and 'twos' so that they act as we hopes. The complete loop is 00->10->01->00(0->1->2->3/0).

>>For 'ones', we can get 'ones = ones ^ A[i]; if (twos == 1) then ones = 0', that can be tansformed to 'ones = (ones ^ A[i]) & ~twos'.

>>Similarly, for 'twos', we can get 'twos = twos ^ A[i]; if (ones* == 1) then twos = 0' and 'twos = (twos ^ A[i]) & ~ones'. Notice that 'ones*' is the value of 'ones' after calculation, that is why twos is calculated later.

后面还有一个[泛化的解决方案](https://leetcode.com/discuss/31595/detailed-explanation-generalization-bitwise-operation-numbers)，太长了只大概看了一下。
这个答案的python版也很快：
```python
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for i in nums:
            a = (a ^ i) & ~b
            b = (b ^ i) & ~a
            
        return a
```

另外，用数学方法解也挺好的：
```python
class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return a
```

###time consuming
#####my solution
48ms-->66.49%
#####hot solution1
40ms-->96.81%
#####hot solution2
48ms-->66.49%