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


#def piglatin(word):
  #"""
  #input: a string representing a word
  #returns: a new string with the word converted to piglatin
  
  #Rules:
  #if the first letter is a consonent, move it from the start to the end and add "ay"
  #so "hello" becomes "ellohay"
  
  #If the first letter is a vowel, just add "yay" to the end
  
  #try to also handle upper case words
  
  #"""
  
  #vowels = ['a','e','i','o','u','A','E','I','O','U']
  #consonants = ['l]
  #'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 
  #punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

  #for ele in word:
    #if ele in punct:
      #final = word.replace(word[0:1], "")
  
  #if word[0] in vowels:
    #final = word + "yay"

  #elif word[0].upper() in vowels:
    #final = word.upper() + "yay"

  #elif word[0] in consonants:
    #final = word.replace(word[0:1], "") + word[0:1] + "ay" 
    
  #else:
    #final = word.replace(word[0:1], "") + word[0:1].upper() + "ay" 
    
  #return final

#final = piglatin(".Oatti.ng")
#print("This has a punctuation ->", final)

#final = piglatin("Utting")
#print("This has an uppercase vowel ->", final)

#final = piglatin("utting")
#print("This has a lowercase vowel ->", final)

#final = piglatin("Rotting")
#print("This has an uppercase consonant ->",final)

#final = piglatin("rotting")
#print("This has a lowercase consonant ->",final)

# TODO:
# 1. Make it work for capitalized words
#    ex: Cable -> Ablecay
# 2. Handle periods (and possibly other punctuation)
#    ex: Able. -> Ableay.
#        cable. -> ablecay.

#Punctuation
#!()-[];:'\,<>./?@#$%^&*_~
def piglatinify(name):
    if name[0] in 'AEIOUaeiou':
        if name[-1] in "!()-[];:'\,<>./?@#$%^&*_~":
            result = name[0:int(len(name))-1] + "yay" +name[-1]
            return result
        else:
            result = name + "yay"
            return result
    else:
        if name[0] == name[0].lower():
            if name[-1] in "!()-[];:'\,<>./?@#$%^&*_~":
                result = name[1:int(len(name))-1] + name[0] + "ay" + name[-1]
                return result
            else:
                result = name[1:] + name[0] + "ay"
                return result
        else:
            if name[-1] in "!()-[];:'\,<>./?@#$%^&*_~":
                result = name[1].upper() + name[2:int(len(name))-1] + name[0].lower() + "ay" + name[-1]
                return result
            else:
                result = name[1].upper() + name[2:] + name[0].lower() + "ay"
                return result

# Testing
test_word = "hello"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able."
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable."
result = piglatinify(test_word)
print(test_word," -> ",result)






  #vowels = ('a','e','i','o','u','A','E','I','O','U')
  #for char in word:
    #if char in vowels:
      #final = word + "yay"
    #else:
      #final = word.replace(word[0:1], "") + word[0:1] + "ay" 
  #return final

#answer = piglatin("uppers")
#print(answer)


#Prof Zamansky's example:
#def piglatinify(word):
  #first = word[0]
  #if first in 'aeiou':
    #result = word +'ay'
  #else: 
    #result =  word[1:] + first +'ay'
  #return result

#Prof Zamansky's example with punctuation:


#Testing
#test_word = "hello"
#result = piglatinify(test_word)
#print(test_word, "->", result)