[<< 메인으로](https://github.com/AtomicLiquors/Algorithm_Wiki_Chb)

&nbsp;  
&nbsp;  
# 해시 테이블 / 딕셔너리 / 맵

데이터를 Key-Value 형식으로 저장하는 방식. 
트리 형태를 이용하거나, 해시를 이용하여 구현할 수 있다.

[키워드 ]

- 해싱 : 문자를 특정 숫자로 변환하는 과정
- 해시 함수 : 문자를 특정 숫자로 변환하는 코드
- 충돌
    - 분리 연결법
    - 부하율 : 실제 데이터와 총 셀의 비율. 0.7이면 이상적으로 간주된다.
    - 성능이 O(1)이 아닌 사실상 O(N)이 되는 경우는?

```
💡 좋은 해시 테이블은 
불필요한 셀을 줄이면서(메모리 낭비를 줄이면서), 
균형을 유지하며, 
충돌을 피한다.
다행히 대부분의 프로그래밍 언어는 해시테이블을 구현하고 충돌 처리를 디자인해 뒀다.
```

&nbsp;  
체이닝 방식 : 인스타그램 해시태그  
오픈 어드레싱 방식

&nbsp;  
### **효율성**

**매우 빠른 룩업 : 데이터를 O(1)만에 룩업할 수 있다.**

**궁극적으로 다음 세 요인에 따라 결정된다.**

- 얼마나 많은 데이터를 저장하는가.
- 얼마나 많은 셀을 쓸 수 있는가.
    
    → 셀이 적고, 데이터가 많으면 충돌이 잦을 것이다.
    
- 어떤 해시 함수를 사용하는가.
    
    → 데이터를 넓게 퍼뜨릴수록 충돌이 적다.
    
    <aside>
    💡 좋은 해시함수는 사용가능한 **모든** 셀에 데이터를 분산시킨다.
    
    </aside>
    

&nbsp;  
### **활용**

[**else if문 대체]**

before)

```python
def status_code(number)
	if number == 200
		return "OK"
	elif number == 301
		return "Moved Permanently"
	elif number == 404
		return "Not Found"
```

after)

```python

STATUS_CODES = {200: "OL", 301: "Moved Permanently", 404: "Not Found"}

def status_code(number)
	return status_
```

[**다양한 속성을 갖는 객체를 표현할 때 ]**
배열 안에 여러 해시 테이블을 넣는다.

```python
[

{”Name”: “Fido”, “Breed”: “Pug”, “Age”: 3, “Gender”, “Male”}.

{”Name”: “Lady”, “Breed”: “Poodle”, “Age”: 6, “Gender”, “Female”}.

{”Name”: “Fido”, “Breed”: “Dalmatian”, “Age”: 2, “Gender”, “Male”}.

]
```

**[수 찾기 시간 단축]**

일반적으로 배열에서 수를 찾을 때 시간복잡도는 O(N)이다.

```python
array = [61, 30, 91, 11, 54, 38, 72]
```

다음과 같은 해시 테이블을 만들어서 수를 찾는 시간을 O(1)으로 단축할 수 있다.

```python
array = {61: true, 30: true, 91: true, 11: true, 54: true, 38: true, 72: true}
```

Q.  억지로 저렇게 쌍으로 만들지 말고, 일반 배열의 항목을 키값처럼 탐색할 수는 없나?

&nbsp;  
&nbsp;  
## 문제

배열의 교집합을 O(N)복잡도로 구하는 알고리즘을 작성하라.

```python
def intersect(arr1, arr2):
    

    d = dict.fromkeys(arr2, 1)
    arr_result = []

    for item in arr1:
        if(item in d):
            arr_result.append(item)
    return arr_result

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]

print(intersect(arr1, arr2))
```

첫 중복 항목 찾기

```python
arr = ['a','b','c','d','c']
d = {}

for i in arr:
    if(i in d):
        print(i)
    else:
        d[i] = 1
```

사용하지 않은 알파벳 찾기

```python
abc = 'abcdefghijklmnopqrstuvwxyz'

str = 'the quick brown box jumps over a lazy dog'

d = dict.fromkeys(str, 1)
for i in abc:
    if not (i in d):
        print(i)
```

한 번만 등장하는 첫 번째 문자 찾기

```python
str = 'minimum'
d = {}
for i in str:
    if (i in d):
        d[i] += 1
    else:
        d[i] = 1

for i in str:
    if d[i]==1:
        print(i)
        break
```