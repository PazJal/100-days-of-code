#Write your code below this line 👇
from math import ceil, sqrt

def prime_checker(number):
  limit = ceil(sqrt(number))
  for i in range(2,limit + 1):
    if number % i == 0:
      print("It's not a prime number.")
      return;

  print("It's a prime number.")
  return;



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
