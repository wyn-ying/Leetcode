###idea
��ֱ�ӵ��뷨�ǣ����ֵ�洢ͳ�ƽ����֮����ֵ����ҳ�Ƶ�ʣ�value������`? n/2 ?`������key�����ɡ�

###hot solution
���ֽⷨ�ܶ࣬��һ������˼·�Ļ��ܣ��������ֵ䣬λ���������򣬷��εȣ�����[����](https://leetcode.com/discuss/47783/different-solutions-dictionary-manipulation-sorting-conquer)��

������һ��ʮ�ּ��Ư����python�����õ�����˼·���ٶ�Ҳ�ܿ졣
��������������Ŀ��������Ƶ�ʳ���`? n/2 ?`����һ�����ڡ���˾�������������м�λ�õ���һ����Ҫ�ҵ�����
������һ�γ��ȹ�������ֶ��������������ǰ���ƶ���
```python
class Solution(object):
    def majorityElement(self, nums):
	    return sorted(nums)[len(nums)/2]
```

#####other code
��˵�е����ߴ���ֻҪǰ���major�ۻ�����С��һ�루�ӼӼ���Ϊ0������������ǰ�����еġ�
����Ҳ�������뵽��major�������е���������һ�룬������ߴ���ʱ������major���������ۼӣ����������������ˣ��������ǹ��õġ�
����ǻ��ж������major����¼������

��Ȼ���������㷨Ҳ������������Ŀ�����ģ���Ƶ�ʳ���`? n/2 ?`����������ڵ�����²ſ��Եõ���ȷ�����
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
������������ַ���Ӧ�ñ�python����2��Ҫ�죬��Ϊֻ����һ�����飬���Ƚ�ʱҲֻ��Ҫ��һ�����顣

###time consuming
#####my solution
60ms
#####hot solution
44ms