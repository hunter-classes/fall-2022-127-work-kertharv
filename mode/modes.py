import random
import datetime

#findLargest(l) which takes in a list of numbers and returns the value of the smallest number 
numList = [6,10,43,12,3,19,32]
def findLargest(l):
    length = len(l)
    l.sort() #Orders the list from least to greatest.
    return l[0] #Prints the first and least number of the list.

print(findLargest(numList))


#freq(l,v) which takes a list of numbers (l) and a value (v). 
#The function will return the frequency
#of v, that is, the number of times that v appears in l.

value = 5
list_1 = [5,8,2,5,2,5,7,100,4,5,8]

def freq(l,v):
    count = 0
    for x in l:
        if x == v: 
            count +=1 #+=1 is the same as count = count + 1
    return count

print(freq(list_1,value))

## Prof Zamansky's code:

# def findLargest(dataset)
    # largeSoFar = l[0]
    # for item in dataset[1:]:
        # if item > largeSoFar:
            # largeSoFar = item
    # return largeSoFar

# def freq(dataset,v)
    # count = 0
    # for item in dataset:
        # if item == v:
            # count = count + 1
    # return count

    ## or

    # [x for x in data set if x==19]
    ## x == number
    # len([x for x in dataset if x==3]) ## Counts how many 3s appear
    # len([x for x in dataset if x==10]) ## Counts how many 10s appear
    # len([x for x in dataset if x==15]) ##Counts how many 15s appear

def buildRandomList(size, maxvalue):
     result = []
     for x in range(size):
         result.appened(random.randrange(maxvalue))
     return result

    ## or

    ## List Comprehensions
    # result = [random.randrange(max value) for x in range(size)]
    # return result

# dataset = buildRandomList(20,30)
# print(findLargest(dataset))
# print(freq(dataset,3))

## Classwork Code
def mode(dataset):
    """
    Returns a mode of the dataset,
    that is the value that appears most frequently

    if multiple values appear the same # of times and are
    most frequent, return any of them.

    Ex mode[(5,4,5,6,7,8,5,4)] --> 5 since appears the most
    mode [(5,5,5,4,4,4,2,2,7,7,8,8,9)] --> return 5 or 4 since
    both of those values appear 3 times which is the most

    Strategy:
    assume the first value is the mode
    we can grab its frequency

    for each remaining item in the dataset:
        count that items frequence and see if it's the new mode so far.
    """
    ## My code
    #counter = 0
    #number = dataset[0]

    #for i in dataset:
        #frequency = dataset.count(i)
        #if frequency > counter:
            #counter = frequency
            #number = i
        #return number

#print(mode(mode_list))

    modeSoFar = dataset[0]
    freqSoFar = freq(dataset,modeSoFar)
    for item in dataset[1:]:
        if freq(dataset,item) > freqSoFar:
            modeSoFar = item
            freqSoFar = freq(dataset,item)

mode_list = [5,5,5,4,4,4,2,2,7,7,8,8,9]
print(mode(mode_list))

def testMode(size,maxValue):
    dataset = buildRandomList(size,maxValue)
    #print(dataset)
    t = datetime.datetime.now()
    starttime = t.microsecond / 1000
    m = mode(dataset)
    end = datetime.datetime.now()
    elapsed = (end.microsecond / 1000)-starttime
    print("size: ", size, " time: ", elapsed)
