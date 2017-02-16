class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        for i in range(0, n):
            if not ((i+1)%15):
                r.append('FizzBuzz')
            elif not ((i+1)%5):
                r.append('Buzz')
            elif not ((i+1)%3):
                r.append('Fizz')
            else:
                r.append(str(i+1))
        return r