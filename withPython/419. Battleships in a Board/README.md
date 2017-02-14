###idea
此题开始没有什么思路。
最直接的想法就是对每个位置进行遍历，若找到```x```则继续找它的右侧或下侧，直到数全所有战舰。
接着Follow up中指出要O(1)的空间复杂度且不让修改原来的空位，一下限制很大。按照之前的思路实现，需要O(n^2)的空间复杂度记录哪些地方被搜索过。
最后看了hint提示说用二叉树，更让人觉得困惑。


###solutions
正统的方案提到了Flood Fill Algorithm，就是用DFS或BFS对网格进行搜索。代码比自己写的要简洁，但同样需要O(n^2)的空间复杂度记录哪些地方被搜索过。

而且这个方案在递归中，算法每次会重新检查上下左右4个位置。
这对于此题来说是一种浪费，既然最外层的遍历已经是从左上往右下走，那么每次检查只需要把右侧和下侧打标记即可。

另外还有一个巧妙的方案
```C++
public int countBattleships(char[][] board) {
    int count = 0;
    for(int i=0;i<board.length;i++)
        for(int j=0;j<board[0].length;j++)
            if(board[i][j]=='X' && (i==0 || board[i-1][j]!='X') && (j==0 || board[i][j-1]!='X')) count++;
    return count;
}
```
一开始还没有看明白，继续看了讨论才理解，只检查每个格子是否是船的左上角，数到是左上角就给```count```加1，只需要O(n^2)的时间复杂度和O(1)的空间复杂度。
###time consuming
#####my solution
68ms-->beats 23.40%
#####discuss solution
53ms-->beats 60.80%