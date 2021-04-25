# Adam Fernandes
# April 2021
# Simple program for easily getting input/output for f(t,y) differential equations

def equation(t: float, y: float) -> float:
   """
   Define this yourself!
   """
   return (y/t) - (y/t)**2

def main():
   print("Input t-value")
   t = float(input())
   
   print("Input t-value")
   y = float(input())

   print(f"\n\tEquation evaluated at t = {t}, y = {y}\t=\t{equation(t, y)}\n")

if __name__ == "__main__":
   main()