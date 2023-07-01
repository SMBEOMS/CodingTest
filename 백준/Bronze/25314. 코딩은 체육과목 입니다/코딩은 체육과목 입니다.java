import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int N;
		N = input.nextInt();
		int result = N/4;
		for(int i= 0; i<result; i++) {
			System.out.print("long ");
		}System.out.print("int");
	}

}