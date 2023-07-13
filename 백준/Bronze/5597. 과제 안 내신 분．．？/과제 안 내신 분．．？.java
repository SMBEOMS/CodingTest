import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        boolean[] submitted = new boolean[31]; // 30명의 학생들의 과제 제출 여부를 저장하는 배열

        // 과제를 제출한 학생들의 번호 입력
        for (int i = 0; i < 28; i++) {
            int num = input.nextInt();
            submitted[num] = true;
        }

        // 과제를 제출하지 않은 학생들의 번호 출력
        for (int i = 1; i <= 30; i++) {
            if (!submitted[i]) {
                System.out.println(i);
            }
        }

        input.close();
    }
}
