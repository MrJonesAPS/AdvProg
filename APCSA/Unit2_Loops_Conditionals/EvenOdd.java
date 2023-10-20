import java.util.Scanner;

public class EvenOdd {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        System.out.println("gimme a number and I'll tell you if it's even or odd");
        
        int num = s.nextInt();

        if(num % 2 == 0){
            //the num is even
            System.out.println("Your number is even!");
        }else{
            System.out.println("Your number is odd");
        }

    }
}
