from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from math import gcd

p = getPrime(256)
q = getPrime(256)
n = p * q
phi_n = (p-1)*(q-1)

e = 65537

d = pow(e, -1, phi_n) # modular invers

assert isPrime(65537)
assert gcd(e, phi_n) == 1

M = bytes_to_long(b"Hemmelig Besked")
assert M < n


C = pow(M, e, n)

M_2 = pow(C, d, n)

assert M == M_2




