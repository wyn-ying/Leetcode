###idea
看到题目第一反应好像可以用动态规划(DP)做，可能因为刚学，比较容易想到。
计算到达每个台阶的可能路径，可以拆分成从它下一阶迈了一步上来，加上从它下两阶迈了一大步上来的和。然后从1，2往上顺序求到n即可。

后来想到，这大概就是个斐波那契数列。

###hot solution
[最热的solution](https://leetcode.com/discuss/16866/basically-its-a-fibonacci)也直接说明是fibonacci问题，而并没有用数组存储，只用了两个变量存前一阶和前两阶的数量，空间复杂度低。
```c++
public int climbStairs(int n) {
    // base cases
    if(n <= 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 2;

    int one_step_before = 2;
    int two_steps_before = 1;
    int all_ways = 0;

    for(int i=2; i<n; i++){
        all_ways = one_step_before + two_steps_before;
        one_step_before = two_steps_before;
        two_steps_before = all_ways;
    }
    return all_ways;
}
```
想到是斐波那契数列之后，各种简洁优雅的解法就有了，不过基本思路没有变化。

这里贴一个最简洁的python代码。
```python
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

###time consuming
#####my solution
44ms-->24.75%
#####hot solution
40ms-->47.96%