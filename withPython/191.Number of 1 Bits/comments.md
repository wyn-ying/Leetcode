###idea
题目要统计二进制中1的个数，从低位向高位统计只需要判断奇偶，显然更容易想到。
之后通过整数除2可以将末位1或0抹掉。提交之后还考虑到，通过移位可能效率更高。

###hot solution
方法1虽然很慢，但体现了python的简洁。
方法2是用移位方法提取每一位，看是不是1，实测和my solution效率一样。
```python
class Solution(object):
    def hammingWeight1(self, n):
        return str(bin(n)).count('1')

    def hammingWeight2(self, n):
		rst = 0
        mask = 1
        for i in range(32):
            if n & mask:
                rst += 1
            mask = mask << 1
        return rst
```
#####other code
号称每次```n &= n - 1```都会消掉一个1，并且貌似很快，但原理还是没太看懂。留下[链接](https://leetcode.com/discuss/27609/short-code-by-time-the-count-and-another-several-method-time)
```c++
int hammingWeight(uint32_t n)
{
    int res = 0;
    while(n)
    {
        n &= n - 1;
        ++ res;
    }
    return res;
}
```

###time consuming
#####my solution
52ms
#####hot solution
######solution1
64ms
######solution2
52ms