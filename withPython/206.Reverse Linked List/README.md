###idea
利用堆栈，把链表的next指针反着改过来就行。

有一个细节：在处理弹栈最后一个节点r的时候，需要注意r.next仍指向的是原链表第二个节点，需要手动修改为NULL。
###hot solution
最热答案是java版，循环法没有使用额外空间，只需要开两个指针，分别记录head和head.next，之后腾挪一下，使得head和newhead都往后移一个节点。
```java
public ListNode reverseList(ListNode head) {
    ListNode newHead = null;
    while(head != null){
        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        head = next;
    }
    return newHead;
}
```
还有一个递归法，基本思路是一样的，不过要新建一个函数，空间消耗也大。

之后贴个python版代码，也是两种方法，循环和递归，思路也一样。
循环法，详细思路见每行注释。
```python
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head			#curr记录当前head的位置/上轮循环时head往后移了一步，现在curr跟上。
        head = head.next	#head往后移一个节点
        curr.next = prev	#修改curr.next往前指
        prev = curr			#修改prev往后移一个节点
    return prev
```
递归法。
```python
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
```

###time consuming
#####my solution
52ms-->55.06%
#####hot solution
#####循环法
56ms-->35.71%
#####递归法
64ms-->17.27%