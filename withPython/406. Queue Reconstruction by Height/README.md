###idea
开始思路有点跑偏，想着把h和k加在一起做一个排序，后来思路变成了做出h的相对值，再和k加在一起，按sum排序，sum相同时再按k排序。但做来做去结果一直不对，感觉可能想歪了。

看了讨论的思路之后，重新写了程序，顺利通过
###solutions
看了讨论答案的思路。首先按h顺序排最高的，排好之后按照h从高到低的顺序，逐渐插入。
不过别人的比自己实现的要快
```python
def reconstructQueue(self, people):
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []
        
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res
```
另外还有两段pythonic的代码
```python
def reconstructQueue(self, people):
    res = []
    for k, g in itertools.groupby(sorted(people, reverse=True), key=lambda x: x[0]):
        for person in sorted(g):
            res.insert(person[1], person)
    return res
```
and
```python
def reconstructQueue(self, people):
    res = []
    for p in sorted(people, key=lambda x: (-x[0], x[1])):
        res.insert(p[1],p)
    return res
```
运行速度快了很多
###time consuming
#####my solution
165ms-->beats 53.08%
#####discuss solution
135ms-->beats 93.05%