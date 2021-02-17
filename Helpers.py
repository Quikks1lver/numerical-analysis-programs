import math

def convertDegreeToRadian(degree: float) -> float:
   """
   Converts an angle in degrees to an angle in radians
   """
   return degree * (math.pi / 180)

def convertRadianToDegree(radian: float) -> float:
   """
   Converts an angle in radians to an angle in degrees
   """
   return radian * (180 / math.pi)