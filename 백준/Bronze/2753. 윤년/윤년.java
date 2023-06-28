import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        int isLeapYear;

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            isLeapYear = 1;
        } else {
            isLeapYear = 0;
        }

        System.out.println(isLeapYear);

        scanner.close();
    }
}
