# Adam Fernandes
# March 2021
# Feed a function and a few points, and calculates composite trapezoidal approximation

from typing import List
from math import sin, cos, tan, pi, log, e

TOLERANCE: float = 1e-7

def compositeTrapezoidalApproximation(leftXVal: float, rightXVal: float, n: float) -> None:
   """
   Feed the left and right x endpoints, along with the n size, and calculates composite trap approx.
   """
   h: float = abs(rightXVal - leftXVal) / n
   
   approx: float = f(leftXVal) + f(rightXVal)
   
   curX: float = leftXVal + h
   while abs(curX - rightXVal) > TOLERANCE:
      approx += (2 * f(curX))
      curX += h
   
   print(f"\n\t-- Composite Trap. Approx. --\n\t{approx * (h/2)}\n")


def f(x: float) -> float:
   """
   Represents a function -- you need to change this function to use the program
   """
   return tan(x)

def main():
   compositeTrapezoidalApproximation(0, (3*pi)/8, 8)

if __name__ == "__main__":
   main()