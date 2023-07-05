import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int N = input.nextInt(); // 배열의 크기
        int[] arr = new int[N];  // 숫자 배열
        
        // 숫자 배열 입력
        for (int i = 0; i < N; i++) {
            arr[i] = input.nextInt();
        }
        
        int V = input.nextInt(); // 찾고자 하는 숫자
        
        int count = 0; // 특정 숫자의 개수를 저장하는 변수
        
        // 배열을 순회하며 특정 숫자의 개수를 세기
        for (int i = 0; i < N; i++) {
            if (arr[i] == V) {
                count++;
            }
        }
        
        System.out.println(count);
        
        input.close();
    }
}
