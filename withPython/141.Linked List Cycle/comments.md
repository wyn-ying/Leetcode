###idea
���������û�гɹ���
��ʼ���뷨�ǰѡ�ͷ���Ͽ�����һ���ڱ���֮��ָ�������ߣ������������ڱ���֪�����л��ˣ�����None���޻���

���ȣ����ڱ�ֵ�����-1������һ��֮����linklist���и������ڿ���discuss֮���ֻ��и�����߼�©��������һ����head����ȥ���硰6���͵Ļ���

###hot solution
����õıȽϴ����İ취������ָ��׷�ϵķ�����
֮�������쳣�Ĵ���next����None��������ܹ��뵽������л�����Ȼ�������None.next�������쳣ֱ���ж�Ϊ�޻����ɡ�
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
����һ�����ò����쳣�İ汾��
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
�ܵ���˵����������ͬС�졣

###time consuming
#####hot solution
76ms