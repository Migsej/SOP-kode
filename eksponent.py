import matplotlib.pyplot as plt
from math import log
import time

def pow_fast(a, x, n):
  s = 1
  t = a
  while x > 0:
    if x&1 != 0:
      s = s*t % n
    t = t*t % n
    x >>= 1
  return s

def pow_naive(a, x, n):
  s = 1
  while x > 0:
    s = s*a
    x -= 1
  return s % n

for i in range(1, 1000):
  start = time.time_ns()
  fast = pow_fast(27, i, 100)
  end = time.time_ns()

  start = time.time_ns()
  naive = pow_naive(27, i, 100)
  end = time.time_ns()

  start = time.time_ns()
  naive = pow(27, i, 100)
  end = time.time_ns()

for i in range(1, 100):
  start = time.time_ns()
  fast = pow_fast(35, i, 200)
  end = time.time_ns()
  plt.plot(i, (end-start), "bo")

  start = time.time_ns()
  naive = pow_naive(35, i, 200)
  end = time.time_ns()
  plt.plot(i, (end-start), "ro")

  start = time.time_ns()
  naive = pow(35, i, 200)
  end = time.time_ns()
  plt.plot(i, (end-start), "g-")

plt.xlabel("størrelse af eksponent")
plt.ylabel("Tid (ns)")
plt.show()

