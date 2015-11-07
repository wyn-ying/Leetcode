class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in s:
            r = r*26 + ord(i) - ord('A') + 1
        
        return r
