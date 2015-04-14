__author__ = 'kaigen'
import sys

mylist = []

def is_it_prime(num):
 # returns 1 if prime 0 if not
  if(num == 0):
    sys.exit(0)
  if(num == 1):
      return 1
  if(num == 2):
      return 1
  if(num == 3):
      return 1
  if(num % 2 == 0):
      return 0
  if(num % 3 == 0):
      return 0
  else:
     return 1


number = 1
while(number != 0):
    number =  int(input("Hi and welcome, Please input a number and we will find out if it is prime: "))
    int(number)
    check = is_it_prime(int(number))
    if(check == 1):
     print("%d is prime!" % number)
    else:
     (print("%d is not prime!" % number))



