###idea
通过r=x^y可以直接得到x和y的汉明距离。之后问题转化为，如何快速求解r中1的个数。小套路：通过r&(r-1)可以快速去掉r中的一个1。

###hot solution
最高票答案的思路基本一样。只是没有再引入新变量，而是直接用x和y。并且在循环中放弃!=0的条件判断，直接用```while x```。
不过经运行，发现hot solution的时间没有减少。

###time consuming
#####my solution
46ms-->beats 42.14%
#####hot solution
59ms-->beats 12.10%