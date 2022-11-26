# Extras Done:
# 1) Handle upper and lower case and/or punctuation.
# 2) Try to tackle more advanced translations like converting parts of words 
# rather than straight substitutions or inserting pirate phrases at appropriate points 
# in your document. For example adding a sentence like “Shiver me timbers” or “Walk the plank” 
# between sentences specified in input.txt
# 3) Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”

pirate = open('pirate.dat').read()  
text = open('input.txt').read()
lowertext = text.lower().split() # Puts everything in lowercase and splits it.
piratesplit = pirate.split('\n') # Split new lines as well

piratespeak = {} # Creates dictionary piratespeak
for word in piratesplit: # Inserts the specified items to the dictionary
    piratespeak.update({word[:word.index(":")]:word[word.index(':')+1:]})

keys = [] # Creates list for keys
for word in piratesplit: # Checks words by detecting : in key and value pairs dictionary
    keys.append(word[:word.index(":")])

punc = [] # Creates a list for punctuation
for word in lowertext:
    if ',' in word or '.' in word or '!' in word: # Move word to the end
        punc.append(word[:-1])
    else:
        punc.append(word) # Otherwise, add word

newstory = [] # List for the new and updated story
i = 0 # tracker

for word in punc:                                 
    if word in keys: # Add the translated pirate word
        newstory.append(piratespeak[word])
    elif word == "<one>": # Replaces <one> with "Shiver me timbers"
        newstory.append("Shiver me timbers!")
    elif word == "<two>": # Replaces <two> with "Shiver me timbers"
        newstory.append("Go away scallywag.")
    else: # Replace with same word
        newstory.append(word) 
    if i == 0 or word == 'i' or '.' in lowertext[i-1] or '!' in lowertext[i-1]: # If the index 
    # is at 0 , or has a period before it, or exclamation mark before it, capitalize the first letter.
        newstory[i] = newstory[i].capitalize() 
    if "." in lowertext[i]: # If there is a period, add it
        newstory[i] = newstory[i] + "."
    elif "," in lowertext[i]: # Else, if there is a comma, add it 
        newstory[i] = newstory[i] + ","
    elif "!" in lowertext[i]: # Else, if there is an exclamation mark, add it
        newstory[i] = newstory[i] + "!"
    i = i + 1
updated = ' '.join(newstory) # Join after splitting story

print(updated) # Prints the final and updated story

# Old directores:
# pirate = open('/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-02-speak/pirate.dat').read()  
# text = open('/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-02-speak/input.txt').read()