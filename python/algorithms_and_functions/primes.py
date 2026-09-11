def isPrime(num):
  n=0
  
  while (n < n*n <= num):
    if (num%n==0):
      return 0
      
  return 1
  

for n in range(1,100):
  if isPrime(n):
    print(n, end=",")
  
  
#================================================================================

