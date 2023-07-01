import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int A;
		int B;
		int result;
		int Num;
		
		
		Num = input.nextInt();
		
		
		for(int i = 0; i < Num; i++) {
			A = input.nextInt();
			B = input.nextInt();
			result = A + B;	
			
			System.out.println(result);
		}
	}

}
