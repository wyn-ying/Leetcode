###hot solution

#####idea主要利用“最终结果只剩1位”的要求以及数字9的特性。

先将0的情况单独考虑。

之后考虑一般情况。以一个特殊情况为例：若num为9的倍数，则根据9的性质，加到1位数时必定为9。
这点想明白之后，其他num%9则不难理解。
需要注意的是，若num为9的倍数，num%9结果是0而不是9，因此需要单独列出num%9==0的情况。

以下是hot solution代码：

```python
def addDigits(self, num):
    if num==0:
        return 0
    if num%9==0:
        return 9
    return num%9
```

再运用语言特性，可以有更简洁的改进版本：

```python
def addDigits(self, num):
	return num % 9 or num and 9
```