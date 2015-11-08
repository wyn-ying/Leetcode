class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ds = dict()
        dt = dict()
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] = ds[s[i]] + 1
            if t[i] not in dt:
                dt[t[i]] = 1
            else:
                dt[t[i]] = dt[t[i]] + 1
        
        
        if ds == dt:
            return True
        else:
            return False
