import java.util.Scanner;
public class Digits{

    public static void main(String[] args){
        //Input: an integer
        //Output: The digits of the number, 
        //          one on each line
        //          starting with the 1's place
        //HINT: You'll need to use integer division
        //          and the % operator

        //Example: if input is 6425345346
        //Output:
        //6
        //4
        //3
        //etc
        
        Scanner s = new Scanner(System.in);
        System.out.print("Type a number");
        int num = s.nextInt();


        while(num > 0){
            //Take the 1's place
            int thisDigit = num % 10;
            System.out.println(thisDigit);

            //Divide by 10 to chop off the 1's place
            //and num will be a new number that is one digit shorter
            num /= 10;
        }


    }
}