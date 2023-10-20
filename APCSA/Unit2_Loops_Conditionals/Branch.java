import java.util.Scanner;

public class Branch {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        System.out.println("guess a number");
        int guess = s.nextInt();

        while(true){
            if(guess < 185){
                System.out.println("Your guess is too low");
            }else if(guess > 185){
                System.out.println("Your guess is too high");
            }else{
                System.out.println("you got it right");
                break;
            }

            System.out.println("make a new guess");
            guess = s.nextInt();

            
        }

    }
}
