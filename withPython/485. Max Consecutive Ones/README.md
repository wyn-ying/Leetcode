###idea
����Ƚϼ򵥣�ֱ����һ��online�취������1�ͽ�cnt�ۼӣ�����0ʱ�Ƚ�cnt�����е�����ȱȽϣ���������ȣ�����cnt��0��

��ʵ��ʱ��Ȼ������һ��С������bit������󣬻�Ӧ������cnt����һ�����е�����ȡ�

###solutions
˼·һ����������ͨ˳���߼��Ƕ���1��cnt�ۼӲ���������ȣ������ǵ�0�ٸ��¡�
```python
def findMaxConsecutiveOnes(self, nums):
    cnt = 0
    ans = 0
    for num in nums:
        if num == 1:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    return ans
```
�����ٶȿ��˺ܶ�
###time consuming
#####my solution
102ms-->beats 54.39%
#####discuss solution
125ms-->beats 23.05%