# Adam Fernandes
# April 2021
# Simple program for easily getting input/output for f(t,y) differential equations

from typing import Union

STOP_VAL: int = -1000

def equation(t: float, y: float) -> Union[float, None]:
   """
   Define this yourself!
   """
   try:
      return (y/t) - (y/t)**2
   except:
      print("\n\tERROR with calculation")

def main():
   while True:
      print(f"Input t-value (then ENTER) and y-value (then ENTER). {STOP_VAL} for either to quit.")
      
      t = float(input())
      if t == STOP_VAL:
         break
      y = float(input())
      if y == STOP_VAL:
         break

      print(f"\n\tEquation evaluated at t = {t}, y = {y}\t=\t{equation(t, y)}\n")

if __name__ == "__main__":
   main()