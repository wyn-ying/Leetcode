###idea
开始想尝试一种O(n)的办法，先对```nums```里的每个数建立它与它的next greater number的一个映射map，之后对findNums直接查map。建立映射的思路是：对```nums```里的每个数，如果它比它左侧的数小，那么它的map值等于它左侧的map值；否则再从它开始往右找next greater number。
结果发现无法处理```[3,1,2]```的情况……可能有地方想差了，没有成功。

于是转用了O(m*n)的办法，即两个循环一个个找。因此最后solution很慢。

###solutions
O(n)办法存在，并且同样用到映射。不过重点是要运用栈结构。将```nums```中的元素依次如栈，并且，每次比较新拿到的元素```x```和栈顶的元素，如果```x```较大，则弹出栈顶元素，并将出栈元素的next greater number记为```x```，继续比较```x```和新栈顶元素，直到栈为空或```x```小于栈顶，此时```x```入栈。这样操作的特点是，始终保持栈里从底到顶是递减的顺序，每次新的```x```会使得栈中比```x```小的元素被弹出并得到映射。最后没有被映射的栈中元素都是-1。

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
同时也找到了这段代码的python版本
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
运行速度快了很多
###time consuming
#####my solution
362ms-->beats 4.64%
#####discuss solution
65ms-->beats 73.37%