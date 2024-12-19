import matplotlib.pyplot as plt
import time

def to_number(string):
  result = 0
  for c in string:
    result <<= 8
    result |= c & 0xff
  return result

def to_string(number):
  result = b""
  while number > 0:
    result += bytes([number & 0xff])
    number >>= 8
  return result[::-1]



for i in range(0, 100):
  input = b"A"*i
  start = time.time_ns()
  to_number(input)
  end = time.time_ns()
  plt.plot(i, end-start, "o")

plt.xlabel("Længden af input tekst")
plt.ylabel("Tid (ns)")
plt.show()

