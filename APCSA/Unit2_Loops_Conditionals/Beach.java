public class Beach {
    /*
     * Warmup: Write a java if statement that replicates this sentence:

        “If it’s sunny, OR if the temperature is greater than 80 and it’s not raining, 
        I will go to the beach.”

        Assume these variables already exist:

     */
    public static void main(String[] args){
        boolean sunny = true;
        int temperature = 75;
        boolean raining = true;
        
        //In class discussion - this is ambiguous.
        //depending on whether you do the && or || first
        //you might get different answers. Java does && first.
        //we add parenthesis when we want to make the order more clear
        if(sunny || temperature > 80 && !raining ){
            System.out.println("Go to the beach!");
        }else{
            System.out.println("don't go to the beach");
        }
    }
}


