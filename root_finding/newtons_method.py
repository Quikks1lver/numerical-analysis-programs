# Adam Fernandes
# February 2021
# Newton's Method, Secant Method for finding roots

from math import cos, sin, tan, pi
from helpers import convertDegreeToRadian
from typing import List

class Val:
   """
   A class to represent past values
   """
   def __init__(self, val: float):
      self.val = val

   def isPositive(self) -> bool:
      """
      Returns True if positive, False otherwise
      """
      return True if self.val > 0 else False
   
   def __repr__(self):
      return f"{self.val}"

def f(x: float) -> float:
   """
   DEFINE THIS YOURSELF!
   """
   return x ** 2 - 6

def f_prime(x: float) -> float:
   """
   Derivative of f(x). DEFINE THIS YOURSELF!
   """
   return 2 * x

def newtonsMethod(p0: float, tolerance: float, maxIterations: int, moreOutput: bool) -> None:
   """
   Undergoes Newton's method, you need to do the function operations though
   """
   print(f"\t--- Newton's Method ---\n")

   numIterations: int = 1
   prev, px, diff = p0, p0, p0

   while diff >= tolerance and numIterations <= maxIterations:
      prev = px
      
      try:
         # change this! f_prime and f = . . .
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

def secantMethod(p0: float, p1: float, tolerance: float, maxIterations: int, moreOutput: bool, falsePosition: bool) -> None:
   """
   Undergoes secant method, you need to do the function operations though
   Haven't implemented false position (yet)
   """
   print(f"\t--- Secant Method ---\n")

   numIterations: int = 1
   pastVals: List[Val] = []
   
   pastVals.append(Val(p0))
   pastVals.append(Val(p1))

   diff = p1
   px = 0

   while diff >= tolerance and numIterations <= maxIterations:
      prev = px

      try:
         prev1 = pastVals[-1]
         prev2 = pastVals[-2]

         px = prev1.val - ((f(prev1.val) * (prev1.val - prev2.val)) / (f(prev1.val) - f(prev2.val)))
         px_val = Val(px)
         pastVals.append(px_val)
         
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

   p0: float = 1
   tolerance: float = 1e-10
   maxIterations: int = 10
   moreOutput: bool = True

   # newtonsMethod(p0, tolerance, maxIterations, moreOutput) # CHANGE THE FUNCTION F FROM ABOVE TO TEST!!
   
   p0 = 3
   p1 = 2
   secantMethod(p0, p1, tolerance, 10, True, False)

if __name__ == "__main__":
   main()