###idea
ûʲô���ʵģ����������ַ����Ĳ�������˲�ͬ���Բ��Ƚϴ�����û��ʵ��д���������һ�¡�

�����Ŀ�Ƚ��ʺ���python������Ϊ�ַ���������python��ǿ������뵽���ֵ䣬֮��һ���ַ�һ���ַ�����������Ӧ�Ӻ;Ϳ����ˡ�
���ǱȽ�û������ĵط��Ƕ���IV��IX����С��λ�ڴ�λǰ�����ô����
�Ƚϱ��İ취��ƥ����λ�ģ�֮���ӵ��ٴ�����һλ�ġ�

###hot solution
����python���ԱȽ�����İ취�����ǰ��һ����λ�Ⱥ���һ����λС�����ü���������ӡ���Ҳ��������������������˼·��
```python
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
```
###time consuming
#####hot solution
172ms-->55.59%