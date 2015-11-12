###idea
首先这个题没有成功。
开始的想法是把“头”断开，设一个哨兵，之后指针往后走，如果看到这个哨兵就知道是有环了，看到None是无环。

首先，我哨兵值设成了-1，错了一次之后发现linklist中有负数，在看过discuss之后发现还有更大的逻辑漏洞：环不一定把head连进去，如“6”型的环。

###hot solution
大家用的比较聪明的办法是两个指针追赶的方案。
之后有用异常的处理next中有None的情况。能够想到，如果有环，必然不会出现None.next，发生异常直接判断为无环即可。
```python
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
```
还有一个不用捕获异常的版本：
```python
def hasCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
```
总的来说两个方案大同小异。

###time consuming
#####hot solution
76ms