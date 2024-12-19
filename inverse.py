import matplotlib.pyplot as plt
import random
from tqdm import tqdm
from sympy import *
from math import gcd
import time

def inverse(a, b):
  if b == 0:
    x = 1
    y = 0
    return a, x, y
  d, x1, y1 = inverse(b, a % b)
  x = y1
  y = x1 - y1 * a//b
  return d, x, y

i = 0
j = 1
for x in range(1000):
  start = time.time_ns()
  inverse(i, j)
  end = time.time_ns()
  plt.plot(i.bit_length(), (end-start), "bo")
  j, i = i, j+i

plt.xlabel("antal bits i fibonacci tal")
plt.ylabel("Tid (ns)")
plt.show()



