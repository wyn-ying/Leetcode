###idea
��setɸѡ��ΨһԪ�صļ��ϣ���Ϊs����nums�г�����ЩΨһԪ�أ�ʣ�µľ��ǳ������ε�Ԫ�صļ��ϡ�����set�аѳ������ε�Ԫ�ض���s��ȥ�������sʣ�µľ��ǳ���һ�εġ�
д��ʱ��о��Լ���˼·���ƣ����������뵽����Լ���������
�����������ʱ�ܳ���ֻbeat��5.88%

###hot solution
��hot solution�￴�������߷��Ĵ𰸣�������[����](http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/)���������£�
```python
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(lambda x, y : x ^ y, nums)
        lowbit = xor & -xor
        a = b = 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]
```
�Լ����棺
```python
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]
```
��ʼû�п�����
������ϸ˼�����������˼·��
ͨ����������һ�ε������롱lowbit����ͬ�����Խ����������ֵķ���a��b�У�
�������������ε�Ԫ�ؿ�������ŵ�a��b�У����϶���������ȥһ���ط����ҡ���򡱺�Ϊ0������Ӱ��a��b��
˼·���Ǻ�����ģ������ǹ���lowbit��������������������̫�����뵽��

###time comsuming
######my solution
600ms
#####hot solution
40ms