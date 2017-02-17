###idea
��ʼ˼·�е���ƫ�����Ű�h��k����һ����һ�����򣬺���˼·���������h�����ֵ���ٺ�k����һ�𣬰�sum����sum��ͬʱ�ٰ�k���򡣵�������ȥ���һֱ���ԣ��о����������ˡ�

�������۵�˼·֮������д�˳���˳��ͨ��
###solutions
�������۴𰸵�˼·�����Ȱ�h˳������ߵģ��ź�֮����h�Ӹߵ��͵�˳���𽥲��롣
�������˵ı��Լ�ʵ�ֵ�Ҫ��
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
���⻹������pythonic�Ĵ���
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
�����ٶȿ��˺ܶ�
###time consuming
#####my solution
165ms-->beats 53.08%
#####discuss solution
135ms-->beats 93.05%