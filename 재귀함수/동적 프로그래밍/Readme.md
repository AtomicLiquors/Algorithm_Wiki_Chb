[<< 메인으로](https://github.com/AtomicLiquors/Algorithm_Wiki_Chb)

&nbsp;  
&nbsp;  
# 동적 프로그래밍 


```
💡 “동적”이란 단어에 너무 얽매이지 말자. 왜 “동적”이라고 하는지 논란이 많은데,  
(나동빈 - 별다른 의미 없이 사용된 단어)
실제로 동적 프로그래밍이라고 해서 반드시 동적인 요소가 포함되는 건 아니다.
```

재귀는 잘못 쓰면 속도가 느려진다.
그 주요 원인을 파악하고 문제를 개선하는 법을 배워보자.

&nbsp;  


<나동빈> https://www.youtube.com/watch?v=5Lu34WIx2Us
메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상.  
이미 계산된 작은 문제는 별도의 메모리 영역에 결과를 저장하고,  
다시 계산하지 않습니다.  
일반적으로 탑-다운(하향식) 또는 바텀-업(상향식) 두 가지 방식으로 구현합니다.


 
&nbsp;
 
도입 요건 :  
문제가 다음 조건을 만족한다면 DP를 사용할 수 있습니다.

1. 최적 부분 구조
큰 문제를 작은 하위 문제로 나눌 수 있다.   
하위 문제의 답을 모아서 큰 문제로 해결할 수 있다.
2. 중복(Overlap)되는 하위 문제  
동일한 하위 문제를 반복적으로 해결해야 한다.  
 
&nbsp;
 

&nbsp;

### 분할 정복과는 무엇이 다른가?
공통점 : 최적 부분 구조를 요건으로 한다.  
차이점 : 분할정복에서는 하위 문제가 반복되지 않는다.
 
&nbsp;
 

아무래도 처음엔 난해할 수 있으나 점화식을 세우고 아래 두 가지 규칙을 만족하는지를 체크해보시면 좀 더 수월하게 푸실 수 있을 겁니다!
1. 한 노드에 중복적으로 탐색을 하는가.
2. 한 번 탐색이 완료된 노드의 값은 불변하는가.

위 두 가지 조건을 모두 만족할 경우 대부분 동적계획법으로 풀립니다 :)

https://st-lab.tistory.com/127


<!--
## 릿코드
동적 프로그래밍은 다음과 같은 문제에 대한 모든 가능한 해결 방법을 체계적으로 탐색합니다.  
- "중첩 하위 문제"로 분해할 수 있는 문제. 원래 문제를 작게 만든 다음, 반복해서 사용할 수 있어야 합니다.
- "최적의 하위 구조 optimal substructure"를 가진 문제. 중첩된 하위 문제의 최적의 솔루션으로부터 원래 문제의 최적의 솔루션을 도출할 수 있습니다.

### 피보나치 수열

If you wanted to find the n^{th}n 
th
피보나치 수열의 n번째 항 F(n)은 F(n−1), F(n−2)라는 작은 문제로 분해될 수 있습니다.

Then, adding the solutions to these subproblems together gives the answer to the original question,   
F(n - 1) + F(n - 2) = F(n)  
F(n−1)+F(n−2)=F(n),   
최적의 하위 구조를 
which means the problem has optimal substructure,   
since a solution F(n)F(n) to the original problem can be formed from the solutions to the subproblems. These subproblems are also overlapping - for example, we would need F(4)F(4) to calculate both F(5)F(5) and F(6)F(6).

These attributes may seem familiar to you. Greedy problems have optimal substructure, but not overlapping subproblems. Divide and conquer algorithms break a problem into subproblems, but these subproblems are not overlapping (which is why DP and divide and conquer are commonly mistaken for one another).

Dynamic programming is a powerful tool because it can break a complex problem into manageable subproblems, avoid unnecessary recalculation of overlapping subproblems, and use the results of those subproblems to solve the initial complex problem. DP not only aids us in solving complex problems, but it also greatly improves the time complexity compared to brute force solutions. For example, the brute force solution for calculating the Fibonacci sequence has exponential time complexity, while the dynamic programming solution will have linear time complexity because it reuses the results of subproblems rather than recalculating the results for previously seen subproblems. The difference in work required by the brute force approach compared to the dynamic programming approach is visually demonstrated on the next page.

-->
