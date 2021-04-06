# Adam Fernandes
# February 2021
# Computes number of iterations and answer to a fixed point problem

from math import cos, sin, tan, pi

def g(x: float) -> float:
   """
   DEFINE THIS YOURSELF!
   Denotes the function g(x) for which we are trying to find fixed point for.
   Ex. f(x) = x^3 - x^2 + 2, and g(x) = x = (x^2 - 2) / x^2
   """
   return ((x**2 - 2) / x**2)

def fixedPointIteration(p0: float, tolerance: float, maxIterations: int, moreOutput: bool) -> None:
   """
   Conducts a fixed point iteration technique, you need to do the function operations though
   """
   print(f"\n\t--- Fixed Point Iteration ---\n")

   numIterations: int = 1
   old: float = p0

   while numIterations <= maxIterations:   
      try:
         p = g(old)
      except:
         print(f"Something strange happened at iteration {numIterations}. Caught error.")
         return
      
      print(f"\tIteration #{numIterations} -- {p:.4f}")

      diff = abs(p - old)
      if diff < tolerance:
         print(f"\n\tThe value of the root is: {p:.7f}\n")
         return

      numIterations += 1
      old = p
   
   print(f"\n\tThe method failed after {maxIterations} iteration(s)\n")

def main():
   p0: float = -150
   tolerance: float = 1e-2
   maxIterations: int = 20
   moreOutput: bool = True

   fixedPointIteration(p0, tolerance, maxIterations, moreOutput)

if __name__ == "__main__":
   main()