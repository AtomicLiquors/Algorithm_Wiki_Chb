
import java.util.Scanner;

public class PrintStar {

    //Before) 반복문 사용
    /*
     public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
				int lvl = sc.nextInt();
				sc.close();
				for (int i = 0; i < lvl; i++) {
					for (int j = 0; j < i+1; j++) {
						System.out.print("*");
					}
					System.out.println("");
				}
    }
    */
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int lvl = sc.nextInt();
		sc.close();
		for (int i = 0; i < lvl; i++) {
			System.out.println( star(i+1) );
			
		}
	}
	

	public static String star(int n){
		
		String result = "";
		if(result.length() == n)
			return result; 
		
		result = "*" + star(n-1);
		
		return result; 
		
	}
}