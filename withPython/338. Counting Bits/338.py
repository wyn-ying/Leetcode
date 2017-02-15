class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            r = [0]
        elif num == 1:
            r = [0,1]
        else:
            r = [0,1]
            for i in range(2,num+1):
                r.append(r[i>>1] if i%2 == 0 else r[i>>1]+1)
        return r