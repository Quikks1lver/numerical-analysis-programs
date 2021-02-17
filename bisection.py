# Adam Fernandes
# February 2021
# Computes number of iterations and answer to a root bisection problem

from math import cos, sin, tan, pi
import sys

def f(x: float) -> float:
   """
   DEFINE THIS YOURSELF!
   """
   return (x**2) - 3

def calculateMidpoint(x: float, y: float) -> float:
   """
   Calculates midpoint between two numbers
   """
   minVal, maxVal = x, y
   if x > y:
      maxVal, minVal = minVal, maxVal
   
   return minVal + ((maxVal - minVal) / 2)

def convertBooleanToSign(boolean: bool) -> str:
   """
   Converts True to > and False to <
   """
   return ">" if boolean else "<"

def bisectionMethod(left: float, right: float, tolerance: float, maxIterations: int, moreOutput: bool) -> None:
   """
   Conducts a bisection method root finding, you need to do the function operations though
   """
   numIterations: int = 1
   mid, prev, diff = sys.maxsize, sys.maxsize, sys.maxsize
   midVal: float = 0.0

   leftSign: bool = True if f(left) > 0 else False
   rightSign: bool = True if f(right) > 0 else False

   while diff >= tolerance and numIterations <= maxIterations:
      prev = mid
      mid = calculateMidpoint(left, right)

      try:
         # change this! midVal = ...
         midVal = f(mid)
      except:
         print(f"\n\tSomething wack happened at iteration {numIterations}. Caught error.\n")
         return

      if moreOutput:
         print(f"\tIteration #{numIterations}: using L {round(left, 2)} {convertBooleanToSign(leftSign)} 0 & R {round(right, 3)} {convertBooleanToSign(rightSign)} 0 -- _{round(mid, 10)}_")

      diff = abs(mid - prev)
      if midVal < 0:
         if rightSign:
            left = mid
            leftSign = False
         else:
            right = mid
            rightSign = False
      else:
         if not rightSign:
            left = mid
            leftSign = True
         else:
            right = mid
            rightSign = True

      numIterations += 1
   
   numIterations -= 1 # account for last for while loop increment
   if numIterations >= maxIterations:
      print(f"\n\tExceeded max iterations ({maxIterations}), yielded {mid}\n")
   else:
      print(f"\n\tAfter {numIterations} iterations -- {mid}\n")
   
   return

def main():
   print("\n\tRemember to change function!\n")

   left: float = 1
   right: float = 2
   tolerance: float = .0001
   maxIterations: int = 15
   moreOutput: bool = True

   bisectionMethod(left, right, tolerance, maxIterations, moreOutput) # CHANGE THE FUNCTION F FROM ABOVE TO TEST!!

if __name__ == "__main__":
   main()