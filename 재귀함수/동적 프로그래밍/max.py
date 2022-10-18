def max_b4(array):
	if len(array) == 1: 
		return array[0] 
	
	if array[0] > max_b4(array[1, array.length - 1]):
		return array[0]
	else:
		return max_b4(array[1, len[array]-1])

"""
Q. 위 코드를 보면, 
조건식에서 한번,
else 분기에서 또 한 번 재귀함수 호출이 있다.

배열 [1, 2, 3, 4]를 실행했다고 할 때… 끝까지 실행할 경우
max 함수는 총 15번 호출이 된다.

특히 배열 [1, 2, 3, 4]와 같이 ‘최악의 경우’에는
재귀함수 호출 횟수는 (2^n - 1)번이 되고,
연산 횟수는 (함수 내의 일정한 연산 개수)*(함수의 호출 횟수)가 될 것이며,
빅 오 표기법으로 상수와 계수를 생략하면 시간복잡도는 O(2^n)이다.
"""

def max_after(array):
	if len(array) == 1: 
		return array[0] 
	
	max_num = max_after(array[1, array.length - 1])

	if array[0] > max_num:
		return array[0]
	else:
		return max_num

"""
Solution : 변수를 하나 만들고, 재귀함수의 결과값을 대입한다.
재귀함수가 종전처럼 조건식에서 한 번, else분기에서 한번 총 두 번 호출되는 게 아니라,
변수에 값을 집어넣기 위해 한 번만 호출될 것이다.

배열 [1, 2, 3, 4]를 대입했다면, 끝까지 실행할 경우, max 함수는 단 4번만 호출된다.

배열 내의 값의 개수에 **비례**하여 재귀호출이 발생하며, 
빅 오 표기법으로 시간복잡도는 O(N)이다.
"""