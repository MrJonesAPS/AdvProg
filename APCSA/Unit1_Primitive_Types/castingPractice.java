public class castingPractice{
    public static void main(String[] args){
        
        //10.0 is a double
        //double is the default in java
        //if we want to store as a float,
        //we need to convert explicitly
        float a = (float)10.0;
        
        //this works fine
        double b = 10.0;
      
         //this also gives loss of precision error
        //int c = 10.0;
        
        //this is how we convert to an int
        int d = (int)10.0;
        
        /*
        Ok, now for some math
        */
        
        int e = 1;
        
        //this is totaly fine
        e = e + 1;
        
        //this is not fine
        //e = e + 1.0;
        
        //the right way to add a double into an int
        e = (int)(e + 1.0);
        
        //this is fine
        e += 1.0;

        /**********
        Rounding
        ***********/        
        double f = 10.1;
        
        //int g = (int)f;
        
        f = (int)f;
        
        //here's a way to round
        
        System.out.println((int)(f+0.5));
        
        
        /**********
        Division
        **********/
        
        //this is 0 because math with ints gives an int
        int h = 5/8;
        
        //this is still 0. The fact that we're
        //storing the answer in a double, doesn't
        //change the fact that the division is with ints
        double i = 5/8;
        
        //this gives an error. The division gives a double
        //and we're storing the double into an int
        //int j = 5.0/8;
        
        //if we want remainder form int division,
        //we use the mod operator
        int remainder = 100 % 3;
       }
}