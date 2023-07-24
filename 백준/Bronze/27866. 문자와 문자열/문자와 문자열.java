import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String S = input.nextLine(); // 단어 S 입력
        int i = input.nextInt(); // 정수 i 입력

        char result = S.charAt(i - 1); // S의 i번째 글자를 가져옴

        System.out.println(result); // 결과 출력
    }
}
