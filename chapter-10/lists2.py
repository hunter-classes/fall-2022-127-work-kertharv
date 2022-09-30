#Exercise 4
numlist = [1, 2, 3, 4]

def average(numlist):

  total = 0
  for num in numlist:
    total = total + num

  return total / len(numlist)

avg = average(numlist)
print(avg)

#Exercise 6
import random
xs = [2, 3, 4]
def sum_of_squares(xs):
  sumSquares = 0
  for number in xs:
    sumSquares += number ** 2
  return sumSquares

result = sum_of_squares(xs)
print(result)
