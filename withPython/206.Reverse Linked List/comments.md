###idea
���ö�ջ���������nextָ�뷴�ŸĹ������С�

��һ��ϸ�ڣ��ڴ���ջ���һ���ڵ�r��ʱ����Ҫע��r.next��ָ�����ԭ����ڶ����ڵ㣬��Ҫ�ֶ��޸�ΪNULL��
###hot solution
���ȴ���java�棬ѭ����û��ʹ�ö���ռ䣬ֻ��Ҫ������ָ�룬�ֱ��¼head��head.next��֮����Ųһ�£�ʹ��head��newhead��������һ���ڵ㡣
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
����һ���ݹ鷨������˼·��һ���ģ�����Ҫ�½�һ���������ռ�����Ҳ��

֮������python����룬Ҳ�����ַ�����ѭ���͵ݹ飬˼·Ҳһ����
ѭ��������ϸ˼·��ÿ��ע�͡�
```python
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head			#curr��¼��ǰhead��λ��/����ѭ��ʱhead��������һ��������curr���ϡ�
        head = head.next	#head������һ���ڵ�
        curr.next = prev	#�޸�curr.next��ǰָ
        prev = curr			#�޸�prev������һ���ڵ�
    return prev
```
�ݹ鷨��
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
#####ѭ����
56ms-->35.71%
#####�ݹ鷨
64ms-->17.27%