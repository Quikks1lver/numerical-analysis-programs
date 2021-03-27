# Adam Fernandes
# March 2021
# Feed a function and a few points, and calculates composite trapezoidal & simpson's approximations

from typing import List
from math import sin, cos, tan, pi, log, e

TOLERANCE: float = 1e-7

def compositeTrapezoidalApproximation(leftXVal: float, rightXVal: float, n: float) -> float:
   """
   Feed the left and right x endpoints, along with the n size, and calculates composite trap approx.
   """
   h: float = abs(rightXVal - leftXVal) / n
   
   approx: float = f(leftXVal) + f(rightXVal)
   
   curX: float = leftXVal + h
   while abs(curX - rightXVal) > TOLERANCE:
      approx += (2 * f(curX))
      curX += h
   
   return (approx * (h/2))

def compositeSimpsonsRule(leftXVal: float, rightXVal: float, n: float) -> float:
   """
   Feed the left and right x endpoints, along with the n size, and calculates composite simp. approx.
   """
   h: float = abs(rightXVal - leftXVal) / n

   approx: float = f(leftXVal) + f(rightXVal)
   
   curX: float = leftXVal + h
   count = 1
   while abs(curX - rightXVal) > TOLERANCE:
      approx += ((4 if count % 2 == 1 else 2) * f(curX))
      curX += h
      count += 1
   
   return (approx * (h/3))

def f(x: float) -> float:
   """
   Represents a function -- you NEED TO MODIFY this function to use the program
   """
   return e**(2*x) * sin(3*x)

def main():
   # populate these values
   leftXVal: float = 0
   rightXVal: float = 2
   n: float = 8

   print(f"\n\t-- Composite Simp.'s Approx. --\n\t{compositeSimpsonsRule(leftXVal, rightXVal, n)}\n")
   print(f"\n\t-- Composite Trap. Approx. --\n\t{compositeTrapezoidalApproximation(leftXVal, rightXVal, n)}\n")

if __name__ == "__main__":
   main()