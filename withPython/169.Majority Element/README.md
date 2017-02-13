###idea
最直接的想法是：用字典存储统计结果，之后从字典里找出频率（value）超过`? n/2 ?`的数（key）即可。

###hot solution
发现解法很多，有一个各种思路的汇总，包括了字典，位操作，排序，分治等，贴出[链接](https://leetcode.com/discuss/47783/different-solutions-dictionary-manipulation-sorting-conquer)。

下面贴一个十分简洁漂亮的python程序，用的排序思路，速度也很快。
很巧妙利用了题目条件，即频率超过`? n/2 ?`的数一定存在。因此经过排序后，数组中间位置的数一定是要找的数。
（想象一段长度过半的数字段在整个数组段中前后移动）
```python
class Solution(object):
    def majorityElement(self, nums):
	    return sorted(nums)[len(nums)/2]
```

#####other code
传说中的在线处理，只要前面的major累积下来小于一半（加加减减为0），就抛弃掉前面所有的。
理由也很容易想到：major在数组中的数量超过一半，因此在线处理时，无论major是用来被累加，还是用来抵消别人，怎样都是够用的。
最后还是会有多出来的major被记录下来。

当然，这样的算法也是巧妙利用题目条件的，即频率超过`? n/2 ?`的数必须存在的情况下才可以得到正确结果。
```c++
public class Solution {
    public int majorityElement(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;

        }
        return major;
    }
}
```
可以想见，这种方法应该比python方法2还要快，因为只操作一个数组，最后比较时也只需要读一个数组。

###time consuming
#####my solution
60ms
#####hot solution
44ms