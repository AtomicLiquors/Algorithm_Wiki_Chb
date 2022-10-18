//팩토리얼을 재귀함수로 구현해 보자.


public class Factorial{
	public static void main(String[] args){
		int result = factorial(4); 
		System.out.println(result);
	}
	
	static int factorial (int n) {
		int result = 0;

		if (n==1){
		result = 1;	
		} else {
			result = n * factorial(n-1); //재귀호출
		}

		return result;
	}
}

