numberlist = [1,2,3,4]
numberlistv2 = [1,2,3,4,5,6,7]
wordlist = ["these", "are", "all", "random", "words"]
strlist = ["random word", "random letter", "capitalized Letter", "CAPITALIZED WORD!"]
randomlist = numberlist + wordlist + strlist
sam_list = ["Hello", "I", "am", "sam", "I", "like", "ham."]

#Write a function to find the smallest value in a listKfind smallest in a list of items
def fix_value_error(list):  
  newlist = []
  for x in list:
    try:
      newlist.append(int(x)) 
    except ValueError:
      continue
  return newlist

def smallest_num_in_list(list):
  newlist = fix_value_error(list)
  smallest_value = newlist[0]
  for K in newlist:
    if K < smallest_value:
      smallest_value = K
  return smallest_value

print(smallest_num_in_list(randomlist))

def smallest_value_in_list(list):
  smallest_value = list[0]
  for K in list:
    if K < smallest_value:
      smallest_value = K
  return smallest_value

print(smallest_value_in_list(numberlist))

def shortest_word_in_list(list):
  shortest_word = list[0]
  for K in list:
    if len(K) < len(shortest_word):
      shortest_word = K
  return shortest_word

print(shortest_word_in_list(wordlist))

print("------------------------------")

#Write a function that returns a new list that contains all the odd items in the original list
def odd_nums_list(list):
    newlist = fix_value_error(list)
    newlistv2 = []
    for number in newlist:
        if number % 2 == 1:
            newlistv2.append(number)
    return newlistv2

print(odd_nums_list(randomlist))

print("------------------------------")

# Write a function that takes a string and returns a new string where all the words are capitalized.
def capitalize_all(word):
  return word.upper()

print(capitalize_all("ilovenewyorkjustkiddingmaybe"))

print("------------------------------")

# Write a function that takes a string and returns a new string with every word 
# that's longer than 5 character turned into upper case
def capitalize_longer_word(word):
  final = []
  word_bank = word.split()
  for word in word_bank:
    if len(word) > 5:
      word = word.upper()
    final.append(word)
  sentence = " ".join(final)
  return sentence

print(capitalize_longer_word("Do not do it or I will do it like a memorable person."))

print("------------------------------")

# Write a function that takes a list of numbers and returns a new list with each item squared
def sqr_all_nums(numlist):
  final_list = []
  for num in numlist:
    num = num **2
    final_list.append(num)
  return final_list

print(sqr_all_nums(numberlist))

print("------------------------------")

# Write a function that takes two lists of numbers and 
# returns a new list where each item is the corresponding values of the original lists 
# added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
def add_both_lists_nums(l1,l2):
  n = 0
  final_list = []
  for num1 in l1:
    final_list.append(num1+l2[n])
    n = n + 1
  return final_list

print(add_both_lists_nums(numberlist,numberlistv2))

print("------------------------------")

# Chapter 10 Exercises 10, 11, and 12

def five_letter_list(word_list):
  final_list = []
  for word in word_list:
   if len(word) == 5:
     final_list.append(word)
  return final_list

print(five_letter_list(wordlist))

def sumToEven(list):
  evenNumberIndex = 0
  sum = 0
  for index in range(len(list)):
    if list[index] % 2 == 0:
      evenNumberIndex = index
  for index in range(evenNumberIndex):
    sum += list[index]
  return sum 
      
print(sumToEven(numberlist))

def sam_stopper_counter(list):
  n = 0
  for item in list:
    n = n + 1
    if item == "sam":
      return n
print(sam_stopper_counter(sam_list))
