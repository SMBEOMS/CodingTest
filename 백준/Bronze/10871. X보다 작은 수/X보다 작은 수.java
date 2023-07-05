import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		
		int A;
		int B;
		
		A = input.nextInt();
		B = input.nextInt(); 
		
		for(int i = 0; i < A; i++) {
			int C = input.nextInt();
			if (C < B) {
				System.out.print(C + " ");
			}
		}
	}
}