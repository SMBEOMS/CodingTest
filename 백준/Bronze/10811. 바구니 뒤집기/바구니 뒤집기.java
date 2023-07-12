import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt(); // 바구니의 개수
        int M = input.nextInt(); // 바구니의 순서를 뒤집을 횟수

        int[] baskets = new int[N + 1]; // 바구니의 개수만큼 배열 생성

        // 초기 바구니 상태 입력
        for (int i = 1; i <= N; i++) {
            baskets[i] = i;
        }

        // 바구니 순서 뒤집기
        for (int i = 0; i < M; i++) {
            int start = input.nextInt(); // 시작 바구니 번호
            int end = input.nextInt(); // 끝 바구니 번호

            // 바구니 순서 뒤집기
            while (start < end) {
                int temp = baskets[start];
                baskets[start] = baskets[end];
                baskets[end] = temp;
                start++;
                end--;
            }
        }

        // 바구니 상태 출력
        for (int i = 1; i <= N; i++) {
            System.out.print(baskets[i] + " ");
        }

        input.close();
    }
}
