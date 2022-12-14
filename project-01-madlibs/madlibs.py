# Extras
# Extra #1 (Done): Instead of specifying the sentences or story to convert, 
# write a story in a file and read it from your program. 
# Make sure to include the file in your repo and that your program reads it correctly.
# Extra #2 (Done): Add some replacements that are unique, that is, the first time 
# you see them you select on randomly but then you keep reusing that replacement. 

# Imports the module random.
import random

# Opens a file, and returns it as a file object.
story = open("story.dat")
adj = open("adj.dat")
nouns = open("nouns.dat")
verbs = open("verbs.dat")
hero = open("hero.dat")

# Spare code for file directories.
#story = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/story.dat")
#adj = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/adj.dat")
#nouns = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/nouns.dat")
#verbs = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/verbs.dat")
#hero = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/project-01-madlibs/hero.dat")

# Reads data previously written to a file.
storyr = story.read()
adjr = adj.read()
nounsr = nouns.read()
verbsr = verbs.read()
heror = hero.read()

# Separate the words into strings.
adjlist = adjr.split()
nounslist = nounsr.split()
verbslist = verbsr.split()
herolist = heror.split()

# Calling these functions for madlibs function.
def random_adj():
    return adjlist[random.randrange(len(adjlist))]

def random_noun():
    return nounslist[random.randrange(len(nounslist))]

def random_verb():
    return verbslist[random.randrange(len(verbslist))]

def random_hero():
    return herolist[random.randrange(len(herolist))]

# Edit this part and below
def madlibs(story):
    # Creates a new story list.
    lol = storyr.split()     
    # This is to show the index being tracked.    
    tracker = 0           
    tracker_name = -1    

    for p in lol:
        # HERO code                              
        if p == "<HERO>":
            if tracker_name == -1:              
                lol[tracker] = random_hero()        
                tracker_name = tracker             
            else:                                 
                lol[tracker] = lol[tracker_name]

        # Nouns code
        elif p == "<NOUN>":                       
            lol[tracker] = random_noun()
            if(tracker == 0 or lol[tracker-1].find('.')):
                lol[tracker]

        # Verbs code
        elif p == "<VERB>":                       
            lol[tracker] = random_verb().lower()
            if(tracker == 0 or lol[tracker-1].find('.')):
                lol[tracker]

        # Adjectives code
        elif p == "<ADJ>":                    
            lol[tracker] = random_adj()
            if(tracker == 0 or lol[tracker-1].find('.')):
                lol[tracker]
                
        tracker = tracker + 1

    # Turns new list back into a string and returns
    return ' '.join(lol)                         

# Print the code.
print(madlibs(storyr))