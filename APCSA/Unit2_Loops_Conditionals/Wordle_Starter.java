import java.util.Scanner;

public class Wordle_Starter{
    public static void main(String[] args){
        char SecretWord_1 = 'T';
        char SecretWord_2 = 'R';
        char SecretWord_3 = 'A';
        char SecretWord_4 = 'S';
        char SecretWord_5 = 'H';
        Scanner s = new Scanner(System.in);

        System.out.println("Enter your first guess, one letter on each line");
        char guess_1 = s.next().charAt(0);
        char guess_2 = s.next().charAt(0);
        char guess_3 = s.next().charAt(0);
        char guess_4 = s.next().charAt(0);
        char guess_5 = s.next().charAt(0);

        System.out.println("Here is feedback on your guess:");

        /************
         * TO DO:
         *  1. Write some code that compares each letter in the guess
         *      To each letter in the SecretWord
         *  2. For each letter in the guess, print out one of these messages:
         *      - "This char is correct!"
         *      - "This char is in the word, but not in the correct position"
         *      - "This char is not in the word"
         *  3. Put this whole thing in a loop - allow 6 guesses
        */

    }
}
