###idea
ֱ�۸о�������DP����������һ��ϸ����������ֻҪ˳��ɨ��һ��list���ҳ�ÿ��������slice����x���Ϳ���ֱ��sum(range(x+1))��������е�slice���������ǿ���ֱ����onlineʵ�֡�
Ȼ����Ϊһ��ϸ�ڳ��˵����û��һ��д�ԡ�
###solutions
���˱��˵��㷨������DP�������Ϊ������
```python
def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    opt, i = [0,0], 1
    for j in xrange(2,len(A)):
        if A[j]-A[j-1] == A[j-1]-A[j-2]:
            opt.append(opt[j-1]+i)
            i += 1
        else:
            opt.append(opt[j-1])
            i = 1
    return opt[-1]
```
˼·�ǣ�ÿ�μ�鵱ǰԪ����ǰ�������Ƿ񹹳�arithmetic��������ɣ�������һ����������(i)�Ļ������ټ�(i+1)��������ǣ���i��Ϊ1����copy�ϴε�����
###time consuming
#####my solution
42ms-->beats 62.29%
#####discuss solution
49ms-->beats 39.57%