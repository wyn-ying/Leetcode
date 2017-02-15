###idea
��ʼ�볢��һ��O(n)�İ취���ȶ�```nums```���ÿ����������������next greater number��һ��ӳ��map��֮���findNumsֱ�Ӳ�map������ӳ���˼·�ǣ���```nums```���ÿ���������������������С����ô����mapֵ����������mapֵ�������ٴ�����ʼ������next greater number��
��������޷�����```[3,1,2]```��������������еط�����ˣ�û�гɹ���

����ת����O(m*n)�İ취��������ѭ��һ�����ҡ�������solution������

###solutions
O(n)�취���ڣ�����ͬ���õ�ӳ�䡣�����ص���Ҫ����ջ�ṹ����```nums```�е�Ԫ��������ջ�����ң�ÿ�αȽ����õ���Ԫ��```x```��ջ����Ԫ�أ����```x```�ϴ��򵯳�ջ��Ԫ�أ�������ջԪ�ص�next greater number��Ϊ```x```�������Ƚ�```x```����ջ��Ԫ�أ�ֱ��ջΪ�ջ�```x```С��ջ������ʱ```x```��ջ�������������ص��ǣ�ʼ�ձ���ջ��ӵ׵����ǵݼ���˳��ÿ���µ�```x```��ʹ��ջ�б�```x```С��Ԫ�ر��������õ�ӳ�䡣���û�б�ӳ���ջ��Ԫ�ض���-1��

```java
public int[] nextGreaterElement(int[] findNums, int[] nums) {
    Map<Integer, Integer> map = new HashMap<>(); // map from x to next greater element of x
    Stack<Integer> stack = new Stack<>();
    for (int num : nums) {
        while (!stack.isEmpty() && stack.peek() < num)
            map.put(stack.pop(), num);
        stack.push(num);
    }   
    for (int i = 0; i < findNums.length; i++)
        findNums[i] = map.getOrDefault(findNums[i], -1);
    return findNums;
}
```
ͬʱҲ�ҵ�����δ����python�汾
```pyhton
def nextGreaterElement(self, findNums, nums):
	d = {}
    st = []
    ans = []
        
    for x in nums:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)

    for x in findNums:
        ans.append(d.get(x, -1))
            
    return ans
```
�����ٶȿ��˺ܶ�
###time consuming
#####my solution
362ms-->beats 4.64%
#####discuss solution
65ms-->beats 73.37%