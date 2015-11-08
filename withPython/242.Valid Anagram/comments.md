###idea
最早想到建立两个存储数组，从a到z，存放两个字符串中字母出现的次数，之后对两个数组进行比较。
之后想到，python中有字典类型可以使用，并且稍微简洁。于是有了提交版本的代码。

###hot solution
方法1采用了字典的方案，比my solution更加简洁。
方法2是最早的idea。
方法3直接用了排序并比较，写法更简洁。

比较时间效率后，发现还是方法2更快。
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
在看hot solution中，最热的java代码比较有趣。
只建立一个存储数组，两个字符串同时对一个存储数组操作，一加一减，最后看是否为0。
不过这种办法只适用与26小写字母的情况。
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
可以想见，这种方法应该比python方法2还要快，因为只操作一个数组，最后比较时也只需要读一个数组。

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