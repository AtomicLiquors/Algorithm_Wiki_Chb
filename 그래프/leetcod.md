
[https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3881/](https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3881/)

Quick Union이 시간복잡도가 Find보다 밀릴 땐 오직 '최악의 경우'일 때만.
내가 제대로 들었나?

**find** : 인덱스가 가리키는 노드를 따라 루트 노드까지 도달한다.

    

**union** : 그래프를 합친다.
connects two previously unconnected vertices by giving them the same root node.

connected :
checks the “connectivity” of two vertices.
두 개의 루트 노드가 같은지 판단.

**Quick Find**

union 연산에 의하여 해당 인덱스에는 루트 노드를 넣고,
find 연산을 호출할 땐 곧바로 루트 노드를 찾을 수 있게 한다. 

**Quick Union**

union 연산에 의하여 해당 인덱스에는 루트 노드를 넣는다.,

union이 quick find랑 quick union이 어떻게 다르지.
quick union에서 find도 o(1)하면 되는 거 아냐?

왜 while문 쓰지?

이 때 find는 그래프가 수직 1자형일 때 최악[O(N)]

Quick Rank는 Quick Union과 흡사.

Quick Rank의 Union이 중요… 
“합치는 두 개의 루트 노드가 같은가?? 랭크 작은 쪽이 랭크 더 높은 루트로 “

Path Compression

find()에 재귀 도입

Union By Rank를 하는 이유

We have implemented two kinds of “disjoint sets” so far, and they both have a concerning inefficiency. Specifically, 

quick find imp : will always spend O(n) time on the union operation 

quick union imp : it is possible, as shown below, for all the vertices to form a line after connecting them using `union`, which results in the worst-case scenario for the `find` function. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/043aa6c3-1b6b-4fc3-a1e6-5b2f8431f6ac/Untitled.png)

Is there any way to optimize these implementations?

Of course, there is; it is to union by rank. 

Previously, for the `union` function, we always chose the root node of `x` and set it as the new root node for the other vertex. 
However, by choosing the parent node based on certain criteria (by rank), 
we can limit the maximum height of each vertex. — ?

To be specific, the “rank” refers to the height of each vertex. 
When we `union` two vertices, instead of always picking the root of `x` or `y`  as the new root node, 
we choose the root node of the vertex with a larger “rank”. We will merge the shorter tree under the taller tree and assign the root node of the taller tree as the root node for both vertices. In this way, we effectively avoid the possibility of connecting all vertices into a straight line. This optimization is called the “disjoint set” with union by rank.

The code for the disjoint set is highly modularized. 
Become familiar with the implementation. 
Understand and **memorize** the implementation of 
“disjoint set with path compression and union by rank”.