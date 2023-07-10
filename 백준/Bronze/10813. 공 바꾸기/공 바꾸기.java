import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt(); // 바구니의 개수
        int M = input.nextInt(); // 공을 바꿀 횟수

        int[] baskets = new int[N + 1]; // 바구니의 개수만큼 배열 생성

        // 초기 바구니 상태 입력
        for (int i = 1; i <= N; i++) {
            baskets[i] = i;
        }

        // 공 위치 바꾸기
        for (int i = 0; i < M; i++) {
            int x = input.nextInt(); // 바꿀 공의 위치
            int y = input.nextInt(); // 바꿀 공의 위치

            // 공 위치 바꾸기
            int temp = baskets[x];
            baskets[x] = baskets[y];
            baskets[y] = temp;
        }

        // 바구니 상태 출력
        for (int i = 1; i <= N; i++) {
            System.out.print(baskets[i] + " ");
        }

        input.close();
    }
}
