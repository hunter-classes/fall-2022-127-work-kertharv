# Extras
# Extra #1: Instead of specifying the sentences or story to convert, 
# write a story in a file and read it from your program. 
# Make sure to include the file in your repo and that your program reads it correctly.
# Extra #2: Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, 
# it should be capitalized, otherwise, lowercase. 
# This is except in the case of proper nouns which should always be capitalized.

import random

# Opens a file, and returns it as a file object.
story = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/story.dat")
adj = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/adj.dat")
nouns = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/nouns.dat")
verbs = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/verbs.dat")

# Reads data previously written to a file.
storyread = story.read()
adjread = adj.read()
nounsread = nouns.read()
verbsread = verbs.read()

# Separate the words into strings.
adjlist = adjread.split()
nounslist = nounsread.split()
verbslist = verbsread.split()

def randAdj():
    return adjlist[random.randrange(len(adjlist))]

def randNounName():
    return nounslist[random.randrange(len(nounslist))]

def randVerb():
    return verbslist[random.randrange(len(verbslist))]

#Edit this part and below
def madlibs(story):
    new = storyread.split()         # new list of the story
    ind = 0                     # index tracker
    indName = -1                # keeps track if a name is established yet, and what index it is
    for i in new:                                 
        if i == "<NOUN>":                     # names
            if indName == -1:                     # if this is the first time name is used
                new[ind] = randNounName()         # calls premade random function at index of <NOUNName> (repeated)
                indName = ind                
            else:                                 # else, use the name from the index of first use
                new[ind] = new[indName]
        elif i == "<VERB>":                       # verbs
            new[ind] = randVerb().lower()
            if(ind == 0 or new[ind-1].find('.')):
                new[ind].capitalize()
        elif i == "<ADJ>":                         # adjectives
            new[ind] = randAdj().lower()
            if(ind == 0 or new[ind-1].find('.')):
                new[ind].capitalize()
        ind+=1
    return ' '.join(new)                         #turns new list back into a string and returns

print(madlibs(storyread))