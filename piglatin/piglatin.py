#Test bondify
def bondify(name):
  """
  input: string in the form “first last”
  return: “Last, First Last”
  """
  location = name.find(' ')
  first = name[0:location].capitalize()

  last = name[location+1:].capitalize()

  result = last.capitalize() + ', ' + first + ' ' + last
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