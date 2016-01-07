class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = abs(num)
    
        if num == 1: # 1 is ugly number
            return True
    
        prime = [2,3,5]
            
        for i in range(7,num+1):
            i_is_prime = True
            for j in prime:
                if (i // j * j == i): # i is not prime
                    i_is_prime = False
                    break
            if i_is_prime:
                prime.append(i)
                if num // i * i == num:
                    return False
        return True