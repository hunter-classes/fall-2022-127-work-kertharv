import math

def is_even(n):
  if n%2 == 0:
    return True
  else:
    return False

def is_even_short_version(n):
  return n%2 == 0


def is_odd(n):
  return not(is_even(n))

#def isRightAngle(a, b, c):
  """
  c is longest
  """
  #return a*a + b*b == c*c

    

print("Even tests")
result = is_even(10)
print("Direct call:", result)

print("Direct call short version:", is_even_short_version(10))

print("Odd tests")
result = is_odd(11)
print("Result for 11 is:", result)

#Test Initialize
def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
    # isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper()
    result = result + first + "."

    # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result

result = initialize("james bond")
print("james bond -->", result)

#Test bondify
def bondify(name):
  """
  input: string in the form “first last”
  return: “Last, first last”
  """
  

  
