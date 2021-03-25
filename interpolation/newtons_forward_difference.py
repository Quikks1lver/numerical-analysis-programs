# Adam Fernandes
# March 2021
# Utilize's Newton's forward difference method to compute coefficients for Lagrange interpolating polynomials

from typing import List

def newtonsForwardDifference(xVals: List[int], yVals: List[int]) -> None:
   """
   Conducts newton's forward difference method on the x vals and y vals
   Prints double array of values
   """
   table: List[List[float]] = [[0 for i in range(len(xVals))] for j in range(len(xVals))]
   
   for index, y in enumerate(yVals):
      table[index][0] = y
   
   for i in range(1, len(xVals), 1):
      for j in range(1, i + 1, 1):
         table[i][j] = (table[i][j-1] - table[i-1][j-1]) / (xVals[i] - xVals[i - j])
   
   for i in range(len(xVals)):
      for j in range(0, i + 1, 1):
         print(round(table[i][j], 7), end="\t")
      print("")

def main():
   # populate this with x values
   xVals: List[float] = [8.1,8.3,8.6,8.7]
   
   # populate this with y values
   yVals: List[float] = [16.9441, 17.56492,18.50515,18.82091]

   newtonsForwardDifference(xVals, yVals, z)

if __name__ == "__main__":
   main()