###idea
�ʼ�뽨��һ��0��n�����飬֮���nums�е�ÿ��Ԫ�ش��Լ�������������ɾ������������������ĿҪ������Ը��Ӷȡ�

�����뷨����˼��ÿ����i�����±�Ĺ�ϵ������case�����������еġ�

����뷨�ǣ���֪�Ǵ�0��n����˿���������ܺ�sum����nums�е��������δ�sum�м��������sumʣ�µ�ֵ����missing number��
���򻯳���1�д��롣

###hot solution
hot solution�е�python code�������յĴ���һ����ֻ��Ϊ����Կ죬�����2�У�`n=len(nums)`����һ�У�����ִ��2�Ρ���Ч�ʲ̫�ࡣ

#####other code
����most votes solution��c++���룬���˱������㣬������ڿ���һЩ��Ŀ�󣬷������ּ�һ�μ�һ�εĳ�����ʺ�ʹ�����������С�
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