###idea
�����뵽���������洢���飬��a��z����������ַ�������ĸ���ֵĴ�����֮�������������бȽϡ�
֮���뵽��python�����ֵ����Ϳ���ʹ�ã�������΢��ࡣ���������ύ�汾�Ĵ��롣

###hot solution
����1�������ֵ�ķ�������my solution���Ӽ�ࡣ
����2�������idea��
����3ֱ���������򲢱Ƚϣ�д������ࡣ

�Ƚ�ʱ��Ч�ʺ󣬷��ֻ��Ƿ���2���졣
```python
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2

def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)
```

#####other code
�ڿ�hot solution�У����ȵ�java����Ƚ���Ȥ��
ֻ����һ���洢���飬�����ַ���ͬʱ��һ���洢���������һ��һ��������Ƿ�Ϊ0��
�������ְ취ֻ������26Сд��ĸ�������
```java
public class Solution {
    public boolean isAnagram(String s, String t) {
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i) - 'a']--;
        for (int i : alphabet) if (i != 0) return false;
        return true;
    }
}
```
������������ַ���Ӧ�ñ�python����2��Ҫ�죬��Ϊֻ����һ�����飬���Ƚ�ʱҲֻ��Ҫ��һ�����顣

###time consuming
#####my solution
92ms
#####hot solution
######solution1
104ms
######solution2
88ms
######solution3
96ms