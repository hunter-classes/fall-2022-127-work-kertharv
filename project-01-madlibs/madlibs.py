# Extras
# Extra #1 (Done): Instead of specifying the sentences or story to convert, 
# write a story in a file and read it from your program. 
# Make sure to include the file in your repo and that your program reads it correctly.
# Extra #2 (Not Done... Fix it): Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, 
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

def random_adj():
    return adjlist[random.randrange(len(adjlist))]

def random_noun():
    return nounslist[random.randrange(len(nounslist))]

def random_verb():
    return verbslist[random.randrange(len(verbslist))]

# Edit this part and below
def madlibs(story):
    # Creates a new list of the story.
    lol = storyread.split()     
    # This is to show the index being tracked.    
    tracker = 0
    # Keeps track if a name is established yet and what index it is.            
    tracker_name = -1                
    for i in lol:
        # Adjectives code                              
        if i == "<NOUN>":
            # If this is the first time name is used.        
            if tracker_name == -1:      
                # Calls premade random function at index of <NOUN> (repeated)              
                lol[tracker] = random_noun()        
                tracker_name = tracker             
            # Else, use the name from the index of first use. 
            else:                                 
                lol[tracker] = lol[tracker_name]
        # Verbs code
        elif i == "<VERB>":                       
            lol[tracker] = random_verb().lower()
            if(tracker == 0 or lol[tracker-1].find('.')):
                lol[tracker].capitalize()
        # Adjectives code
        elif i == "<ADJ>":                    
            lol[tracker] = random_adj().lower()
            if(tracker == 0 or lol[tracker-1].find('.')):
                lol[tracker].capitalize()
        tracker = tracker + 1
    # Turns new list back into a string and returns
    return ' '.join(lol)                         

print(madlibs(storyread))