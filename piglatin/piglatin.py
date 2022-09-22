#Test bondify
def bondify(name):
  """
  input: string in the form “first last”
  return: “Last, First Last”
  """
  location = name.find(' ')
  first = name[0:location].capitalize()

  last = name[location+1:].capitalize()

  result = last + ', ' + first + ' ' + last
  return result

result = bondify("james bond")
print("james bond -->", result)


def piglatin(word):
  """
  input: a string representing a word
  returns: a new string with the word converted to piglatin
  
  Rules:
  if the first letter is a consonent, move it from the start to the end and add "ay"
  so "hello" becomes "ellohay"
  
  If the first letter is a vowel, just add "yay" to the end
  
  try to also handle upper case words
  
  """
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  if word[0] in vowels:
    final = word + "yay"
  else:
    final = word.replace(word[1:], "") + word[1:] + "ay"  
  return final

final = piglatin("Rotting")
print(final)

final = piglatin("Oatting")
print(final)



  #vowels = ('a','e','i','o','u','A','E','I','O','U')
  #for char in word:
    #if char in vowels:
      #final = word + "yay"
    #else:
      #final = word.replace(word[0:1], "") + word[0:1] + "ay" 
  #return final

#answer = piglatin("uppers")
#print(answer)


#def piglatinify(word):
  #first = word[0]
  #if first in 'aeiou':
    #result = word +'ay'
  #else: 
    #result =  word[1:] + first +'ay'
  #return result

#Testing
#test_word = "hello"
#result = piglatinify(test_word)
#print(test_word, "->", result)