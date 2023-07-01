import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int price = input.nextInt();
        int num = input.nextInt();
        int total = 0;
        
        for(int i = 0; i < num; i++) {
            int unitPrice = input.nextInt();
            int quantity = input.nextInt();
            
            total += unitPrice * quantity;
        }
        
        if(total == price) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
