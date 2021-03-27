# Adam Fernandes
# March 2021
# Conducts Romberg integration

from typing import List
from math import sin, cos, tan, pi, log, e

TOLERANCE: float = 1e-7

# Of course, code reuse is sub optimal, and I would have rather called this function from the other
# file, but this is easier for now.
def modifiedCompositeTrapezoidalApproximation(leftXVal: float, rightXVal: float, n: float) -> float:
   """
   Modified version of ./composite_integration.py
   """
   h: float = n
   approx: float = f(leftXVal) + f(rightXVal)   
   curX: float = leftXVal + h

   while abs(curX - rightXVal) > TOLERANCE and curX < rightXVal:
      approx += (2 * f(curX))
      curX += h
   
   return approx

def romberg(leftXVal: float, rightXVal: float) -> None:
   """
   Computes up to R_5,5 romberg integrals
   """
   table: List[List[float]] = [[0 for i in range(0, 5)] for i in range(0, 5)]
   
   multiplier: int = 0
   for i in range(len(table[0])):
      dx: int = (2 * multiplier if i != 0 else 1)
      table[i][0] = modifiedCompositeTrapezoidalApproximation(leftXVal, rightXVal, (rightXVal - leftXVal) / dx) * ((rightXVal - leftXVal) / (dx * 2))
      multiplier += 1
   
   for i in range(1, 5):
      for j in range(1, i + 1):
         table[i][j] = table[i][j-1] + ((1 / ((4**j) - 1)) * (table[i][j - 1] - table[i - 1][j - 1]))
   
   print("--- Romberg ---")
   for i in range(len(table)):
      for j in range(0, i + 1, 1):
         print(f"R_{i+1},{j+1}: {table[i][j]:.7f}", end="\t")
      print("")

def f(x: float) -> float:
   """
   Represents a function -- you NEED TO MODIFY this function to use the program
   """
   return (sin(x)**2) - 2*x*sin(x) + 1

def main():
   left: float = 1
   right: float = 4
   
   romberg(left, right)

if __name__ == "__main__":
   main()