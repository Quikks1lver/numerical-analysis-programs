# Adam Fernandes
# March 2021
# Feed a function and a few points, and calculates trapezoid approx. for integral

from typing import List
from math import sin, cos, tan, pi

def f(x: float) -> float:
   """
   Represents a function -- you need to change this function to use the program
   """
   return x * sin(x)

def trapezoidApproximation(y1: float, y2: float, dx: float) -> None:
   """
   Calculates and prints trapezoid approximation for a function
   """
   approx: float = (dx / 2) * (y1 + y2)
   print(f"\n\tTrap Approx using {round(y1, 4)} and {round(y2, 4)} = {round(approx, 5)}\n")

def main():
   xVals: List[float] = [0, pi / 4]

   trapezoidApproximation(f(xVals[0]), f(xVals[1]), abs(xVals[1] - xVals[0]))

if __name__ == "__main__":
   main()