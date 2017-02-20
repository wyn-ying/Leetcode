###idea
直观感觉可以用DP做，后来再一仔细分析，发现只要顺序扫描一遍list，找出每个连续的slice长度x，就可以直接sum(range(x+1))计算出可行的slice总数，于是可以直接用online实现。
然而因为一个细节出了点错，并没能一次写对。
###solutions
看了别人的算法，发现DP做代码更为简练。
```python
def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    opt, i = [0,0], 1
    for j in xrange(2,len(A)):
        if A[j]-A[j-1] == A[j-1]-A[j-2]:
            opt.append(opt[j-1]+i)
            i += 1
        else:
            opt.append(opt[j-1])
            i = 1
    return opt[-1]
```
思路是：每次检查当前元素与前面两个是否构成arithmetic，如果构成，则在上一次连续个数(i)的基础上再加(i+1)；如果不是，则i清为1，并copy上次的数。
###time consuming
#####my solution
42ms-->beats 62.29%
#####discuss solution
49ms-->beats 39.57%