import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int result;

        if (A == B && B == C) {
            result = 10000 + A * 1000;
        } else if (A == B || B == C || A == C) {
            if (A == B) {
                result = 1000 + A * 100;
            } else {
                result = 1000 + C * 100;
            }
        } else {
            result = Math.max(Math.max(A, B), C) * 100;
        }

        System.out.println(result);

        scanner.close();
    }
}
