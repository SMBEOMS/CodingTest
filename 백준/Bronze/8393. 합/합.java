import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int A;
		int B = 0;
		A = input.nextInt();
		for(int i = 0; i <= A; i++) {
			B += i;
			
		}System.out.print(B);
	}

}
