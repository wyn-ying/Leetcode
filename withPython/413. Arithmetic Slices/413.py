class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0
        i=len(A)-1
        cnt=0
        while i>=2:
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                c=i
                while c>=2:
                    c -= 1
                    if not A[c]-A[c-1] == A[c-1]-A[c-2]:
                        break
                l=i-c
                cnt += sum(range(l+1))
                print(l, cnt)
                i=c-1
            else:
                i-=1
        return cnt