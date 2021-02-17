# Adam Fernandes
# February 2021
# iterative algorithm for approximating square root 2

def approximateSqrt2(start: float, tolerance: float) -> None:
   """
   Gives a close approximation square root of 2, given a starting number and a tolerance
   """
   prev, cur, diff = start, start, start
   iteration: int = 0
   
   while diff >= tolerance:
      iteration += 1

      prev = cur
      cur = (prev / 2) + (1 / prev)
      diff = abs(cur - prev)
   
   print(f"Reached convergence after {iteration} iterations. Approximation: {prev}")

approximateSqrt2(100000000000, .000001)