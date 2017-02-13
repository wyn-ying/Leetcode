###idea
������Ŀ��һ��Ӧ��������ö�̬�滮(DP)����������Ϊ��ѧ���Ƚ������뵽��
���㵽��ÿ��̨�׵Ŀ���·�������Բ�ֳɴ�����һ������һ�����������ϴ�������������һ�������ĺ͡�Ȼ���1��2����˳����n���ɡ�

�����뵽�����ž��Ǹ�쳲��������С�

###hot solution
[���ȵ�solution](https://leetcode.com/discuss/16866/basically-its-a-fibonacci)Ҳֱ��˵����fibonacci���⣬����û��������洢��ֻ��������������ǰһ�׺�ǰ���׵��������ռ临�Ӷȵ͡�
```c++
public int climbStairs(int n) {
    // base cases
    if(n <= 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 2;

    int one_step_before = 2;
    int two_steps_before = 1;
    int all_ways = 0;

    for(int i=2; i<n; i++){
        all_ways = one_step_before + two_steps_before;
        one_step_before = two_steps_before;
        two_steps_before = all_ways;
    }
    return all_ways;
}
```
�뵽��쳲���������֮�󣬸��ּ�����ŵĽⷨ�����ˣ���������˼·û�б仯��

������һ�������python���롣
```python
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

###time consuming
#####my solution
44ms-->24.75%
#####hot solution
40ms-->47.96%