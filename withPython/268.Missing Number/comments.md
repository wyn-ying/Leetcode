###idea
最开始想建立一个0到n的数组，之后把nums中的每个元素从自己建立的数组中删除，但这样不符合题目要求的线性复杂度。

后来想法变成了检查每个数i与其下标的关系，发现case不是有序排列的。

最后想法是：已知是从0到n，因此可以先求出总和sum，把nums中的数字依次从sum中剪掉，最后sum剩下的值就是missing number。
最后简化成了1行代码。

###hot solution
hot solution中的python code和我最终的代码一样，只是为了相对快，变成了2行，`n=len(nums)`单独一行，避免执行2次。但效率差不太多。

#####other code
看到most votes solution是c++代码，用了比特运算，很巧妙。在看过一些题目后，发现这种加一次减一次的程序很适合使用异或运算进行。
```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int result = nums.size();
        int i=0;

        for(int num:nums){
            result ^= num;
            result ^= i;
            i++;
        }

        return result;
    }
};
```

###time consuming
#####my solution
60ms