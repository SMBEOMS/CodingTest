import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int N = input.nextInt(); // 배열의 크기
        
        int min = Integer.MAX_VALUE; // 최솟값을 저장하는 변수. 초기값은 가장 큰 값으로 설정
        int max = Integer.MIN_VALUE; // 최댓값을 저장하는 변수. 초기값은 가장 작은 값으로 설정
        
        // 배열의 숫자 입력 및 최솟값, 최댓값 갱신
        for (int i = 0; i < N; i++) {
            int num = input.nextInt();
            
            if (num < min) {
                min = num;
            }
            
            if (num > max) {
                max = num;
            }
        }
        
        System.out.println(min + " " + max);
        
        input.close();
    }
}
