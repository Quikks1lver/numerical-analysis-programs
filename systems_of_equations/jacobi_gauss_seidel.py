# Adam Fernandes
# April 2021
# Computes Jacobi & Gauss-Seidel approximations for 3d matrices; can easily be extended to N-dimensions

from typing import List, Union

def x1(x2: float, x3: float) -> float:
   """
   Define this yourself! Represents x1 = ... in terms of x2, x3, etc.
   """
   return (9 + x2) / 10

def x2(x1: float, x3: float) -> float:
   """
   Define this yourself! Represents x2 = ... in terms of x1, x3, etc.
   """
   return (7 + x1 + 2*x3) / 10

def x3(x1: float, x2: float) -> float:
   """
   Define this yourself! Represents x3 = ... in terms of x1, x2, etc.
   """
   return (6 + 2*x2) / 10

def jacobiGaussSeidel(initialValues: Union[None, List[float]], numIterations: int, useGaussSeidel: bool) -> None:
   """
   Prints Jacobi or Gauss-Seidel method to specified number of iterations
   """
   matrix: List[List[float]] = [[0 for i in range(3)] for i in range(numIterations + 1)]
   
   # copy over initial values if they exist
   if initialValues != None:
      matrix[0] = initialValues.copy()
   
   for i in range(1, numIterations + 1):
      # populate x_1
      matrix[i][0] = x1(matrix[i - 1][1], matrix[i - 1][2])
      x_1: float = matrix[i][0] if useGaussSeidel else matrix[i-1][0]
      
      # populate x_2
      matrix[i][1] = x2(x_1, matrix[i-1][2])
      x_2: float = matrix[i][1] if useGaussSeidel else matrix[i-1][1]
      
      # populate x_3
      matrix[i][2] = x3(x_1, x_2)

      print(f"Iteration #{i}")
      print(matrix)

def main():
   initialValues: List[float] = [0, 0, 0]
   numIterations: int = 2
   useGaussSeidel: bool = True

   jacobiGaussSeidel(initialValues, numIterations, useGaussSeidel)

if __name__ == "__main__":
   main()