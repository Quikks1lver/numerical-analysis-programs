/**
 * Helps with Bisection root-finding method
 */
public class BisectionMidpoint
{
   /**
    * Calculates midpoint between two integers
    */
   public static void calculateMidpoint(Double num1, Double num2)
   {
      if (num1 > num2)
      {
         double temp = num2;
         num2 = num1;
         num1 = temp;
      }

      double midpoint = num1 + ((num2 - num1) / 2);
      System.out.printf("\n\tMidpoint of %f and %f is __%f__\n\n", num1, num2, midpoint);
   }

   public static void main(String [] args)
   {
      if (args.length < 2)
      {
         System.out.println("\n\tCorrect syntax: java BisectionMidpoint <num1> <num2>");
         return;
      }

      Double num1 = Double.parseDouble(args[0]);
      Double num2 = Double.parseDouble(args[1]);

      calculateMidpoint(num1, num2);
   }
}