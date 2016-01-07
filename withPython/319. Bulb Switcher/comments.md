###idea
开始被题目给唬住了。后来仔细写了n=4~8的case之后恍然大悟。

对于i<n，如果有i是j的平方，那么在第j轮，i作为j的倍数被关闭，而到第i轮，i又被打开。
而对其他数字k，除了第一轮，只有到第k轮它才会被触发，所以一定是off的。所以n个灯玩n轮之后，所有平方数是on的，非平方数都是off的。

###hot solution
清一色的one line math method，都是这一思路。

###time consuming
#####my solution
40ms-->48.24%