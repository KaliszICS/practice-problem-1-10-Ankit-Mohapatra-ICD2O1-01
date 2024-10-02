import math
import numpy as np
def q1(): 
  x = float(input("Enter a integer: "))
  print(math.sqrt(x))


def q2(): 
  y = int(input("Input a number: "))
  yY = np.float64(y)
  print(math.isqrt(yY))


def q3(): 
  z = int(input("Input a number: "))
  zZ = np.float64(z)
  print(math.trunc(zZ))


def q4(): 
  print(math.ceil(float("Input a number: ")))


def q5(): 
  x = float(input("Input a number: "))
  y = float(input("Input another number: "))
  print(math.trunc((x*y)/2))



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
