������⿨�˺þã���Ъ�����п��ԵȾ������������˺ܾá��ҵĴ���Խ�С�����ж�Ӧ�ö�û�����⣬����һ����̬��case -2147483648��ס��
ʵ���벻�����ŵİ취�㶨�����Ծ������ˡ���
###idea
˳���ҳ�С��num����������num���γ������ֳ�ȥ2��3��5�������Ӿ�˵������ugly number��
###hot solution
����python���룬�����˼Ҷ�С��0��ȫ���ж�Ϊfalse�������֮ǰû���ǵ��ġ�
֮�����ҵĴ����м��������жϺ�case 214797179��Ȼ����ͨ����Ӧ����ʹ����list��Ե�ʡ�
```python
def isUgly(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    for x in [2, 3, 5]:
        while num % x == 0:
            num = num / x
    return num == 1
```
###time consuming
#####hot solution
52ms-->89.66%