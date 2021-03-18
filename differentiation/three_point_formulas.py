# Adam Fernandes
# March 2021
# Feed an array, and this will calculate the f' values using 3 point endpoint and midpoint formulas

from typing import List

def prettyPrintFPrime(fPrime: float, isMidPoint: bool, fx: float) -> None:
   """
   Pretty prints out f' information
   """
   formulaType: str = "Midpoint" if isMidPoint else "Endpoint"
   print(f"\tf' for {fx} using {formulaType} formula: {round(fPrime, 6)}")

def threePointEndpoint(fx1: float, fx2: float, fx3: float, dx: float) -> None:
   """
   Calculates and prints f' using fx1, fx2, and fx3
   """
   fPrime: float = (1.0 / (2.0 * dx)) * ( (-3.0 * fx1) + (4.0 * fx2) - (fx3))
   prettyPrintFPrime(fPrime, False, fx1)

def threePointMidpoint(fx: float, fx_prev: float, fx_next: float, dx: float) -> None:
   """
   Calculates and prints f' using fx_prev, and fx_next
   """
   fPrime: float = (1.0 / (2.0 * dx)) * (fx_next - fx_prev)
   prettyPrintFPrime(fPrime, True, fx)

def main():
   # populate below list with f(x) values
   values: List[float] = [3.6887963, 3.6905701, 3.6688192, 3.6245909]
   # populate dx
   dx: float = 0.1

   for i in range(len(values)):
      if i == 0:
         print("")
         threePointEndpoint(values[i], values[i+1], values[i+2], dx)
      elif i == len(values) - 1:
         threePointEndpoint(values[i], values[i-1], values[i-2], -dx)
         print("")
      else:
         threePointMidpoint(values[i], values[i-1], values[i+1], dx)

if __name__ == "__main__":
   main()