[<< 메인으로](https://github.com/AtomicLiquors/Algorithm_Wiki_Chb)

&nbsp;  
&nbsp;  
# 동적 프로그래밍 


```
💡 “동적”이란 단어에 너무 얽매이지 않도록 합시다. 왜 “동적”이라고 하는지 논란이 많은데,  
(나동빈 - 별다른 의미 없이 사용된 단어)
실제로 동적 프로그래밍이라고 해서 반드시 동적인 요소가 포함되는 건 아닙니다.
```


 
&nbsp;
 
## 적용 요건
문제가 다음 조건을 만족한다면 DP를 사용할 수 있습니다.

1. 최적 부분 구조(Optimal Substructure)
큰 문제를 작은 하위 문제로 나눌 수 있다.   
하위 문제의 답을 모아서 큰 문제로 해결할 수 있다.

2. 중복(Overlap)되는 하위 문제  
동일한 하위 문제를 반복적으로 해결해야 한다.  
 
&nbsp;
 

### 티스토리 팁
아무래도 처음엔 난해할 수 있으나 점화식을 세우고 아래 두 가지 규칙을 만족하는지를 체크해보시면 좀 더 수월하게 푸실 수 있을 겁니다!
1. 한 노드에 중복적으로 탐색을 하는가.
2. 한 번 탐색이 완료된 노드의 값은 불변하는가.

위 두 가지 조건을 모두 만족할 경우 대부분 동적계획법으로 풀립니다 :)

https://st-lab.tistory.com/127
 

&nbsp;

### 분할 정복과는 무엇이 다른가?
- 공통점 : 최적 부분 구조를 요건으로 한다.  
- 차이점 : 분할정복에서는 하위 문제가 반복되지 않는다.
 
&nbsp;
 


### 릿코드 팁

첫 번째 특징
- 최대/최솟값 구하기
- 특정 조건을 만족하는 방법 수 찾기
- 특정 지점에 도달 가능한지 여부

하지만 이 중에는 탐욕법으로도 풀리는 문제도 있습니다.

&nbsp;  

두 번째 특징
장래의 결정이 이전의 결정에 기초하여 이루어지는지
<!--

House Robber is an excellent example of a dynamic programming problem. The problem description is:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

In this problem, each decision will affect what options are available to the robber in the future. For example, with the test case \text{nums = [2, 7, 9, 3, 1]}nums = [2, 7, 9, 3, 1], the optimal solution is to rob the houses with \text{2}2, \text{9}9, and \text{1}1 money. However, if we were to iterate from left to right in a greedy manner, our first decision would be whether to rob the first or second house. 7 is way more money than 2, so if we were greedy, we would choose to rob house 7. However, this prevents us from robbing the house with 9 money. As you can see, our decision between robbing the first or second house affects which options are available for future decisions.

Longest Increasing Subsequence is another example of a classic dynamic programming problem. In this problem, we need to determine the length of the longest (first characteristic) subsequence that is strictly increasing. For example, if we had the input \text{nums = [1, 2, 6, 3, 5]}nums = [1, 2, 6, 3, 5], the answer would be 4, from the subsequence \text{[1, 2, 3, 5]}[1, 2, 3, 5]. Again, the important decision comes when we arrive at the 6 - do we take it or not take it? If we decide to take it, then we get to increase our current length by 1, but it affects the future - we can no longer take the 3 or 5. Of course, with such a small example, it's easy to see why we shouldn't take it - but how are we supposed to design an algorithm that can always make the correct decision with huge inputs? Imagine if nums contained 10,00010,000 numbers instead.

When you're solving a problem on your own and trying to decide if the second characteristic is applicable, assume it isn't, then try to think of a counterexample that proves a greedy algorithm won't work. If you can think of an example where earlier decisions affect future decisions, then DP is applicable.

To summarize: if a problem is asking for the maximum/minimum/longest/shortest of something, the number of ways to do something, or if it is possible to reach a certain point, it is probably greedy or DP. With time and practice, it will become easier to identify which is the better approach for a given problem. Although, in general, if the problem has constraints that cause decisions to affect other decisions, such as using one element prevents the usage of other elements, then we should consider using dynamic programming to solve the problem. These two characteristics can be used to identify if a problem should be solved with DP.

Note: these characteristics should only be used as guidelines - while they are extremely common in DP problems, at the end of the day DP is a very broad topic.
-->
