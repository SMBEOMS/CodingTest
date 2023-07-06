import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int max = 0; // 최댓값을 저장하는 변수. 초기값은 가장 작은 값으로 설정
        int index = 0;
		
		for(int i = 1; i < 10 ; i ++) {
			int A= input.nextInt();
			if (A >max) {
				max = A;
				index = i;
			}
		}
		System.out.println(max);
        System.out.println(index);
        input.close();

	}

}
