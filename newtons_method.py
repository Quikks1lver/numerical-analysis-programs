# Adam Fernandes
# February 2021
# Uses Newton's Method to find roots for functions

from math import cos, sin, tan, pi
from Helpers import convertDegreeToRadian

def f(x: float) -> float:
   """
   DEFINE THIS YOURSELF!
   """
   return cos(x) - x

def f_prime(x: float) -> float:
   """
   Derivative of f(x). DEFINE THIS YOURSELF!
   """
   return (-1 * sin(x)) - 1

def newtonsMethod(p0: float, tolerance: float, maxIterations: int, moreOutput: bool) -> None:
   """
   Undergoes Newton's method, you need to do the function operations though
   """
   numIterations: int = 1
   prev, px, diff = p0, p0, p0

   while diff >= tolerance and numIterations <= maxIterations:
      prev = px
      
      try:
         # change this! px = ...
         deriv = f_prime(prev)
         if deriv == 0:
            print(f"\n\tDerivative = 0 at {numIterations}. Abort.\n")
            return

         px = prev - (f(prev) / deriv)
      except:
         print(f"\n\tSomething wack happened at iteration {numIterations}. Caught error.\n")
         return

      if moreOutput:
         print(f"\tIteration #{numIterations} -- {round(px, 5)} <- f({round(prev, 3)})")

      diff = abs(px - prev)
      numIterations += 1
   
   numIterations -= 1 # account for last for while loop increment
   if numIterations >= maxIterations:
      print(f"\n\tExceeded max iterations ({maxIterations}), yielded {px}\n")
   else:
      print(f"\n\tAfter {numIterations} iterations -- {px}\n")
   
   return

def main():
   print("\n\tRemember to change function!\n")

   p0: float = (pi / 4)
   tolerance: float = 1e-10
   maxIterations: int = 10
   moreOutput: bool = True

   newtonsMethod(p0, tolerance, maxIterations, moreOutput) # CHANGE THE FUNCTION F FROM ABOVE TO TEST!!

if __name__ == "__main__":
   main()