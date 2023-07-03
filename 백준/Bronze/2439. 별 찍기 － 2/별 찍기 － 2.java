import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        
        for (int i = 1; i <= A; i++) {
            for (int j = A - i; j > 0; j--) {
                System.out.print(" ");
            }
            
           for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            
           System.out.println();
        }
    }
}