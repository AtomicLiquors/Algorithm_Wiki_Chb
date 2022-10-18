다음 코드의 시간복잡도가 O(N)인 이유는?

A. 중첩된 배열이지만, 순회하는 배열이 서로 다르다.(outer, inner)
 결국에는 안쪽 루프가 일정한 ‘총 배열 수’만큼 실행된다.

```python
arr = [
    [0,1,1,1],
    [1,0,1],
    [0,1]
]

def count_ones(outer_array):
    count = 0
    for inner_array in outer_array:
        for number in inner_array:
            if number == 1:
                count += 1

    return count

print (count_ones(arr))
```

다음과 같이 아예 별개의 배열을 곱하는 경우는 O(N*M)이라고 표현한다.(오피셜인가?)

M이 N과 크기가 같다면 시간복잡도는 O(N^2)이 된다.

N보다 M이 작다면 M을 상수로 간주하여 시간복잡도는 O(N)이 된다.

> 막상 정답 해설은 이런 경우에 그냥 O(N^2)으로 취급하는 것 같다.
> 

```python
function twoNumberProducts(array1, array2){
    let products = [];

    for(let i = 0; i < array1.length; i++){
      for(let j = 0; j < array2.length; j++){
        products.push(array1[i] * array2[j]);
      }
    }
  }
```