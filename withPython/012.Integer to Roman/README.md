###idea
��013����һ�������Ҳ����˼·������4���ֵ䣬��λ��ǧλ��֮����ֵ������

###hot solution
���Ʊ�𰸵�˼·���ҿ�ʼ��Ļ���һ����
```java
public static String intToRoman(int num) {
    String M[] = {"", "M", "MM", "MMM"};
    String C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    String X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
}
```
����python����汾�Ͷ��ˡ���[��replace��](https://leetcode.com/discuss/25519/an-accepted-answer-in-python-using-s-replace)��Ҳ��1459���⴦��ġ�

������һ��1459����ģ�
```python
def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res
```
�����������ֻ��ǲ��ֵ�ķ�����죬��Ȼ�������е��ª��

###time consuming
#####my solution
112ms-->94.75%
#####hot solution
136ms-->47.24%