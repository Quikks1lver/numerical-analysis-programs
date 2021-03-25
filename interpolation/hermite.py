# Adam Fernandes
# March 2021
# Utilizes a tabular procedure to calculate coefficients for osculating Hermite polynomials

from typing import List
import sys
from math import floor

EMPTY_CELL = sys.maxsize 

def hermite(xVals: List[float], yVals: List[float], yPrimeVals: List[float]) -> None:
   """
   Uses a tabular procedure to calculate hermite polynomial coefficients
   Prints double array of values
   """
   table: List[List[float]] = [[EMPTY_CELL for i in range(2 * len(xVals))] for j in range(2 * len(xVals))]
   newXVals: List[float] = [xVals[floor(i/2)] for i in range(2 * len(xVals))]

   for index, y in enumerate(yVals):
      table[index * 2][0] = table[index * 2 + 1][0] = y
   
   for index, yPrime in enumerate(yPrimeVals):
      table[(index * 2) + 1][1] = yPrime
   
   for i in range(1, len(newXVals), 1):
      for j in range(1, i + 1, 1):
         if table[i][j] == EMPTY_CELL:
            table[i][j] = (table[i][j-1] - table[i-1][j-1]) / (newXVals[i] - newXVals[i - j])
   
   print("--- Hermite ---")
   for i in range(len(table)):
      for j in range(0, i + 1, 1):
         print(f"{table[i][j]:.7f}", end="\t")
      print("")

def main():
   # populate this with x values
   xVals: List[float] = [8.3,8.6]
   
   # populate this with y values
   yVals: List[float] = [17.56492,18.50515]

   # populate this with y' values
   yPrimeVals: List[float] = [3.116256,3.151762]

   hermite(xVals, yVals, yPrimeVals)

if __name__ == "__main__":
   main()