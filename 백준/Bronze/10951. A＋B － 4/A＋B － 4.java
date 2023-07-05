import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        while (input.hasNextInt()) {
            int A = input.nextInt();
            int B = input.nextInt();
            
            int sum = A + B;
            System.out.println(sum);
        }
        
        input.close();
    }
}
