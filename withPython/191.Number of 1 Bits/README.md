###idea
��ĿҪͳ�ƶ�������1�ĸ������ӵ�λ���λͳ��ֻ��Ҫ�ж���ż����Ȼ�������뵽��
֮��ͨ��������2���Խ�ĩλ1��0Ĩ�����ύ֮�󻹿��ǵ���ͨ����λ����Ч�ʸ��ߡ�

###hot solution
����1��Ȼ��������������python�ļ�ࡣ
����2������λ������ȡÿһλ�����ǲ���1��ʵ���my solutionЧ��һ����
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
�ų�ÿ��```n &= n - 1```��������һ��1������ò�ƺܿ죬��ԭ����û̫����������[����](https://leetcode.com/discuss/27609/short-code-by-time-the-count-and-another-several-method-time)
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