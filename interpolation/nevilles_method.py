# Adam Fernandes
# March 2021
# Utilize's Neville's method to help with interpolation

from typing import List

def nevillesMethod(xVals: List[int], yVals: List[int], z: float) -> None:
   """
   Conducts neville's method on the x vals, y vals, and x-val in question.
   Prints double array of values
   """
   table: List[List[float]] = [[0 for i in range(len(xVals))] for j in range(len(xVals))]
   
   for index, y in enumerate(yVals):
      table[index][0] = y
   
   for i in range(1, len(xVals), 1):
      for j in range(1, i + 1, 1):
         term1: float = (z - xVals[i - j]) * table[i][j - 1]
         term2: float = (z - xVals[i]) * table[i - 1][j - 1]
         table[i][j] = (term1 - term2) / (xVals[i] - xVals[i - j])
   
   for i in range(len(xVals)):
      for j in range(0, i + 1, 1):
         print(round(table[i][j], 7), end="\t")
      print("")

def main():
   # populate this with x values
   xVals: List[float] = [1, 1.3, 1.6, 1.9, 2.2]
   
   # populate this with y values
   yVals: List[float] = [.7651977, .620086, .4554022, .2818186, .1103623]
   
   # populate this with x-value in question
   z: float = 1.5

   nevillesMethod(xVals, yVals, z)

if __name__ == "__main__":
   main()