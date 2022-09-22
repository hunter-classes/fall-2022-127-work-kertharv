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

#Exercise 10 and 11

def is_rightangled(a,b,c):
  if a > b and a > c:
    a,b,c = b,c,a
  elif b > a and b > c:
    a,b,c = a,c,b
  return abs(a**2 + b**2 - c**2) < 0.001
  
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

print(is_rightangled(a,b,c))

#CodingBat
#hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#first_two
def first_two(str):
  return str[:2]