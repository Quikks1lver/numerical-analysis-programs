# Adam Fernandes
# February 2021
# Computes number of iterations and answer to a fixed point problem

def f(x: float) -> float:
   """
   DEFINE THIS YOURSELF!
   """
   return (.5 * x) + (1.5 * (1/x))

def fixedPointIteration(p0: float, tolerance: float, maxIterations: int, moreOutput: bool) -> None:
   """
   Conducts a fixed point iteration technique, you need to do the function operations though
   """
   numIterations: int = 1
   prev, px, diff = p0, p0, p0

   while diff >= tolerance and numIterations <= maxIterations:
      prev = px
      
      try:
         # change this! px = ...
         px = f(prev)
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

   p0: float = 1.0
   tolerance: float = .001
   maxIterations: int = 10
   moreOutput: bool = True

   fixedPointIteration(p0, tolerance, maxIterations, moreOutput) # CHANGE THE FUNCTION F FROM ABOVE TO TEST!!

if __name__ == "__main__":
   main()