- Graph 용어 정리
- Graph 구현
- Graph 탐색
- Minimum Spanning Tree
    - Kruskal algorithm
    - Prim algorithm

> SNS 친구 관계 등을 O(1) 시간 만에 조회하기.
> 

<aside>
💡  데이터의 연결 관계를 잘 나타내는 “관계에 특화된 자료 구조”

</aside>

- 정점(vertex) : 그래프의 각 데이터
- 간선(edge) : 정점을 잇는 선분
- 인접(adjacent) : 두 정점이 간선으로 연결되어 있는 상태
- 이웃(neighbor) : 인접해 있는 두 정점
- **경로(path)** : 한 정점에서 다른 정점으로 가는 간선들의 순열.

방향 그래프 : 간선의 연결관계가 상호적이지 않고 일방적인 경우.

### 객체 지향 그래프 구현

그간 해시 테이블로 구현하는 예시만 봐 왔지만, 이제부터는 객체지향 방식으로 구현하겠다.

(코드)

이 책에서는 리스트를 이용해 각 정점의 이웃들을 저장했지만,(인접 리스트 구현)
리스트 대신 2차원 배열로 구현하는 방식도 알아두면 좋다(인접 행렬 구현)

### 탐색

**[용도]**

“어떤 그래프 탐색 알고리즘이든, 핵심은 지금까지 방문한 정점을 기록하는 것.”

ㅡ 그렇지 않으면 무한 루프가 발생하기 때문이다.

- 방문한 정점 기록은 해시 테이블을 이용한다.
- 탐색에는 자료의 크기에 구애받지 않는 ‘재귀함수’를 사용한다.

**정점 찾기**

임의의 정점 하나만 접근할 수 있으면, 탐색을 통해 어떤 정점이든 찾을 수 있다.

**정점의 연결 여부 확인**

**순회**

각 정점에 연산 수행

[유형]

깊이 우선 탐색, 너비 우선 탐색

개념 확실히 잡으세요.

코드로 구현하세요.

[시간복잡도]

순회하는 각 정점의 인접 정점까지 모두 순회한다.
(이미 방문했더라도, 방문했는지 확인하는 연산이 필요하다.)

**O(V + E)**

정점 + 간선

정확히는 V + 2E지만 빅오표기법대로 상수를 버린 것.

왜 V+2E인지는 코드 짜면서 파악하세요.

### **가중 그래프**

간선에 정보를 추가한 것. (길이, 요금 등)

“최단 경로 문제”

**데이크스트라 알고리즘(다익스트라 알고리즘)**

- 현재 정점에서 인접 정점으로 연결되는 가중치(길이/비용)를 확인한다.

이것도 풀면서 정리할까?

여러가지 변형이 있다.

예를 들어 배열 대신 우선순위 큐로 구현하면 속도가 더 빠르다.

또한 다익스트라 말고도 다양한 알고리즘이 있다.