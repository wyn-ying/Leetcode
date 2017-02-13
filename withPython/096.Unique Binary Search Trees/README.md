###idea
刚学了动态规划(DP)，所以知道是用动态规划做。但是准备落实时，发现还是有点眼高手低。
是抄了一个有注释的[c++版代码](https://leetcode.com/discuss/17674/dp-problem-10-lines-with-comments)，
还有一个[java版的最热答案](https://leetcode.com/discuss/24282/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i)，说明也很多。
顺便自己重新梳理一遍DP的思路。

DP的基本思路是通过减少重复的计算提高效率。以此题为例，计算n个节点的BST的结构数，等价于n个节点的二叉树的个数。
因为有一个二叉树就可以唯一分配节点值满足BST。二叉树的个数问题可以这样思考：
若n个节点构成的二叉树个数记为F(n)，除掉一个root节点，把剩下n-1个节点扔在左右两个子树，最后总的二叉树的个数就是`Sum(F(i)*F(n-1-i))`，i是左子树可能的节点数，遍历0~n-1。
因此，要算n个几点的就需要算前面从1到n-1个节点的所有结果……反过来说，算完前n-1个节点的之后，再计算n个节点的时候，只需要用前面n-1个结果计算就可以很快。
所以从节点数等于1算上来，每多一个节点时都是用前面的结果加加乘乘，算完后保存下来供后面的计算使用。

总的思路是这样，不过自己写的代码效率还是很低……

###hot solution
看过讨论区的答案后发现对python答案大同小异。感觉这类纯算法题与python语言相合度不高。效率方面也差不太多。
```python
def numTrees1(self, n):
    res = [0] * (n+1)
    res[0] = 1
    for i in xrange(1, n+1):
        for j in xrange(i):
            res[i] += res[j] * res[i-1-j]
    return res[n]
```

另外还有一种[数学解法](https://leetcode.com/discuss/34569/very-simple-straight-based-math-catalan-number-times-space)。虽然快但是不具有通用性。

###time consuming
#####my solution
48ms-->18.78%
#####hot solution
40ms-->47.89%