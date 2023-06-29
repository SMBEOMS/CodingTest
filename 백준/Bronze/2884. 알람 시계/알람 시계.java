import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hour = scanner.nextInt();
        int minute = scanner.nextInt();

        // 45분 뺀 시간 계산
        minute -= 45;
        if (minute < 0) {
            hour -= 1;
            minute += 60;
        }

        // 음수 시간 처리
        if (hour < 0) {
            hour += 24;
        }

        System.out.println(hour + " " + minute);

        scanner.close();
    }
}
