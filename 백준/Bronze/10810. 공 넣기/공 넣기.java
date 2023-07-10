import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt(); // 바구니의 개수
        int M = input.nextInt(); // 공을 넣을 구간의 개수

        int[] baskets = new int[N + 1]; // 바구니의 개수만큼 배열 생성

        // 각 바구니에 공 넣기
        for (int i = 0; i < M; i++) {
            int start = input.nextInt(); // 시작 구간
            int end = input.nextInt(); // 끝 구간
            int ball = input.nextInt(); // 넣을 공의 번호

            // 공을 넣는 과정
            for (int j = start; j <= end; j++) {
                baskets[j] = ball;
            }
        }

        // 각 바구니에 있는 공의 개수 출력
        for (int i = 1; i <= N; i++) {
            System.out.print(baskets[i] + " ");
        }

        input.close();
    }
}
