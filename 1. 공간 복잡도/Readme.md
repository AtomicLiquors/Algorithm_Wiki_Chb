**공간 복잡도** : 데이터 원소가 N개일 때, 알고리즘이 얼마나 많은 메모리 단위를 소모하는가?

**보조 공간** : 알고리즘에서 추가로 소모하는 메모리 공간

<aside>
💡 빠르고 메모리 효율적인 알고리즘만 사용하고 싶겠지만,
둘 중 하나만 택해야 되는 상황이 찾아올 것이다.

**가령, 일반적으로 빠른 정렬일수록 공간을 더 많이 차지한다.**

</aside>

**우월한 공간복잡도 예제** 
— 대문자 변환 함수

before)

```jsx
function makeUpperCase(arr){
	let newArr = [];
	for(let i = 0; i < arr.length; i++){
		newArr[i] = array[i].toUpperCase();
	}
return newArr;
```

함수가 끝났을 때 컴퓨터 메모리에는 배열이 두 개 들어있다.
(매개변수로 받은 원래 배열 + 새롭게 생성한 배열)

- 시간 복잡도는 O(N)이다.
- 함수가 데이터 원소 N개를 추가로 생성했다. 함수의 공간 효율성은 O(N)이다.

```jsx
function makeUpperCase(arr){
	for(let i = 0; i < arr.length; i++){
		array[i] = array[i].toUpperCase();
	}
return newArr;
```

- 시간 복잡도는 O(N)이다.
- 이 함수는 어떤 메모리도 추가로 소모하지 않는다. 
추가되는 메모리는 0이고, 이는 상수기 때문에 공간 효율성은 O(1)이다.
    - 공간 복잡도 계산은 연산 횟수하고 상관이 없다. 헷갈리면 안 된다.
    - 또한 추가로 생성되는 데이터만 고려하는 것이지, 
    기존 데이터가 차지하고 있는 메모리는 고려하지 않는다.
    

**우월한 공간복잡도 + 떨어지는 시간 복잡도 예제** 
— 중복 값 확인 함수

```jsx
function hasDupValue(arr){
	for(let i = 0; i < arr.length; i++){
		for(let j = 0; j < arr.length; j++){
			if(i !== j && arr[i] === arr[j]){
				return true;
			}
		}
	}
	return false;
}
```

- 시간복잡도는 O(N^2)이다.

```jsx
function hasDupValue(arr){
	let exVals = {};
	for(let i = 0; i < arr.length; i++){
		if(!exVals[arr[i]]){
				exVals[arr[i]] = true;
		}else{
			return true;
		}
	}
	return false;
}
```

해시 테이블과 루프를 활용하였다.

새 항목이 나올 때마다 키로 저장하고, 값은 true로 저장한다.
해시 테이블에 이미 키가 있다면, true를 반환한다.

시간복잡도는 O(N^2)에서 O(N)으로 줄었다.
공간복잡도가 O(1)에서 O(N)으로 늘었다.

```jsx
function hasDupValue(arr){
	arr.sort((a, b) => (a < b)? -1 : 1);
	for(let i = 0; i < arr.length-1; i++){
		if(array[i] === array[i+1]){
			return true;
		}
	}
	return false;
}
```

정렬의 시간복잡도는 O(NlogN)이다. 가장 빠른 정렬 알고리즘이 O(NlogN)이기 때문이다.
배열 순회에 걸리는 N단계는 정렬 단계에 비하면 매우 적으므로, 
결론적으로 이 함수의 O(NlogN)이다.

공간 복잡도는 일반적인 퀵 정렬이라고 봤을 때 O(logN)이다.
퀵 정렬이 재귀 호출을 O(logN)번 수행하기 때문에, 최고점에서 호출 스택 크기가 log(N)이다.

**재귀함수의 공간복잡도**

Q. 새 자료 구조를 생성하지 않기 때문에, 공간을 추가로 차지하지 않을 텐데?

A. 10장에서 배운 것처럼, 함수는 자기 자신을 호출할 때마다 **호출 스택에 항목을 추가한다.**

그래서 재귀함수는 재귀 호출 횟수만큼)
최대 O(N)의 공간을 차지한다.

같은 작업을 수행하는 **루프**라면 메모리를 추가로 소모하지 않는다.

collection : O(N^2)

O(N)

1.  O(N), O(N) 

1. O(N), O(1)

1. O(N), O(N)