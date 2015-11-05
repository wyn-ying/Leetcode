###idea
用set筛选出唯一元素的集合，记为s，在nums中除掉这些唯一元素，剩下的就是出现两次的元素的集合。再在set中把出现两次的元素都从s中去掉，最后s剩下的就是出现一次的。
写的时候感觉自己的思路很绕，不过是能想到的相对简洁的做法。
最后跑下来耗时很长，只beat了5.88%

###hot solution
在hot solution里看到了在线疯狂的答案，并给了[链接](http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/)。代码如下：
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
以及简洁版：
```python
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]
```
开始没有看懂。
后来仔细思考大概明白了思路：
通过两个出现一次的数“与”lowbit不相同，可以将两个数区分的放在a和b中，
而其他出现两次的元素可能随机放到a和b中，但肯定两个数会去一个地方，且“异或”后为0，不会影响a和b。
思路还是很巧妙的，尤其是构造lowbit并用来区分两个数，不太容易想到。

###time comsuming
######my solution
600ms
#####hot solution
40ms