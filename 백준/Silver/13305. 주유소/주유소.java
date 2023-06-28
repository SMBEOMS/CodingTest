import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        long[] distances = new long[n - 1];
        for (int i = 0; i < n - 1; i++) {
            distances[i] = scanner.nextLong();
        }

        long[] prices = new long[n];
        for (int i = 0; i < n; i++) {
            prices[i] = scanner.nextLong();
        }

        long minCost = prices[0];
        long totalCost = minCost * distances[0];

        for (int i = 1; i < n - 1; i++) {
            if (prices[i] < minCost) {
                minCost = prices[i];
            }
            totalCost += minCost * distances[i];
        }

        System.out.println(totalCost);

        scanner.close();
    }
}
