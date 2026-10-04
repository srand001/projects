#------------------------------------------------------------------------------
# Prime numbers
# Functions to check if a number is prime.
#
# Note: A prime number is a number greater than 1 that has no positive 
# divisors other than 1 and itself.
#
# Designed by Surjit Randhawa 2026
#-----------------------------------------------------------------------------

from math import sqrt  # Square root function


from math import sqrt

def isPrime(num):
  if num <= 1:  # Numbers less than or equal to 1 are not prime
    return False
  
  max = int(sqrt(num)) + 1
  
  for n in range(2,max):
    if (num % n) == 0:
      return False

  return True
  

for n in range(100):
  if isPrime(n):
    print(n, end=",")

# Output:
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
