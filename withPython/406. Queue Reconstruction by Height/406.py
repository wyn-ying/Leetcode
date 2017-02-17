class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        for p in people:
            if p[0] in d:
                d[p[0]].append(p)
            else:
                d[p[0]] = [p]
        s=sorted(d.keys(),reverse=True)
        r=[]
        for k in s:
            t=sorted(d[k], key=lambda x: x[1])
            if len(r) != 0:
                for p in t:
                    r.insert(p[1], p)
            else:
                r=t
                
        return r