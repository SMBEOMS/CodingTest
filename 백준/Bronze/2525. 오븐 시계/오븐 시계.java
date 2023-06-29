import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int currentHour = scanner.nextInt();
        int currentMinute = scanner.nextInt();
        int cookingTime = scanner.nextInt();

        int hour = currentHour;
        int minute = currentMinute + cookingTime;

        if (minute >= 60) {
            hour += minute / 60;
            minute %= 60;
        }

        if (hour >= 24) {
            hour %= 24;
        }

        System.out.println(hour + " " + minute);

        scanner.close();
    }
}
