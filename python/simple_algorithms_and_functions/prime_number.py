#--------------------------------------------------------------------
# Prime numbers
# Functions to check if a number is prime
#
# Designed by Surjit Randhawa 2026
#--------------------------------------------------------------------

from math import sqrt  # Square root function


def isPrime(n):
  max = int(sqrt(n)) + 1
  
  for k in range(2,max):
    if n % k==0:
      return False

  return True


n=2
while n < 100:
  if isPrime(n):
    print(n,end=",")
  n=n+1

