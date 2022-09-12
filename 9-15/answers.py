#Exercise 7 
def is_even(n):
  if n % 2 == 0:
    return True
  else: 
    return False
  
n = float(input("Input number: "))
print(is_even(n))

#Exercise 8
def is_odd(n):
  if n % 2 == 0:
    return False
  else:
    return True

n = float(input("Input number: "))
print(is_odd(n))

#Exercise 10
def is_rightangled(a,b,c):
  if abs(c**2 - (a**2 + b**2) < 0.001):
    return "True"
  else:
    return "False"

  
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

print(is_rightangled(a,b,c))