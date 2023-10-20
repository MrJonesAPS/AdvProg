import java.util.Scanner;

public class ForLoopVsWhileLoop{
    public static void main(String[] args){

        Scanner s = new Scanner(System.in);

        for(int x = 100;x >= 0;x -= 2){
            //Write one more line here
            System.out.println(x);
        }


        System.out.print("Guess the password");
        String password = "asdf";
        String guess = s.next();

        while(guess != password){
            System.out.print("Nope! Guess Again");

            //Write one more line here
            guess = s.next();
        }

    }
}
            



