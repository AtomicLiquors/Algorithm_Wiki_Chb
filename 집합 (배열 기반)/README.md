[<< 메인으로](https://github.com/AtomicLiquors/Algorithm_Wiki_Chb)

&nbsp;  
&nbsp;  
# 집합

중복을 불허하는 자료구조

```
💡 단 하나의 규칙으로 효율성이 달라진다.
```

본장에서 논의하는 집합은 배열 기반 집합이다.  
다른 건 배열과 똑같지만 중복을 허용하지 않는다는 점에서 다르다.
 

### 읽기

배열이랑 똑같다.

### 검색

배열이랑 똑같다.

### 삭제

배열이랑 똑같다.

### 삽입

---

**문제는 삽입이다.**

중복을 허용하지 않는다고 했다.
새 값을 넣는다면? 기존 데이터와 일치하지 않아야 한다.
따라서 삽입을 할 때마다 기존 데이터와 일치하는지 **검색**이 필요하다.

삽입해도 된다면 = 기존에 없는 데이터로 확인됐다면 = 기존 데이터를 처음부터 끝까지 검색해 봤다면
그제서야 삽입이 수행된다.

```java
[ 검색() ] + [ 삽입() ] 
 = [ 데이터 처음부터 끝까지 검색 ] + [ 데이터를 밀어내고 + 삽입 연산 ]
 = [ 검색할 데이터 갯수 ] + [ 밀어낼 데이터 갯수 + 1 ]
 <= [ N ] + [ N+1 ] = [ 2N + 1 ]
```