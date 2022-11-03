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
    # n algorithm
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
     #result = []
     #for x in range(size):
         #result.append(random.randrange(maxvalue))
     #return result

    ## or

    ## List Comprehensions
    result = [random.randrange(maxvalue) for x in range(size)]
    return result

# dataset = buildRandomList(20,30)
# print(findLargest(dataset))
# print(freq(dataset,3))

# --------------------------------------

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
    counter = 0
    number = dataset[0]

    for i in dataset:
        frequency = dataset.count(i)
        if frequency > counter:
            counter = frequency
            number = i
        return number

## Prof Zamansky's code
#print(mode(mode_list))
    # n^2 algorithm
    #modeSoFar = dataset[0]
    #freqSoFar = dataset.count(modeSoFar)
    #for item in dataset[1:]: #outer loop -> n
        #calling dataset.count(item) each time is n
        #n times n = n, or n^2 = n
        #if dataset.count(item) > freqSoFar:
            #modeSoFar = item
            #freqSoFar = dataset.count(item)
    #return modeSoFar

mode_list = [5,5,5,4,4,4,2,2,7,7,8,8,9]
print("Mode results: ", mode(mode_list))

# --------------------------------------

def fastMode(dataset):
    # assume all values in dataset
    # are between 0  and 99 inclusive

    # 1. Make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
    list = [0] * 100
    # 2. Loop through a dataset
    # and for each item increment
    # (add 1) to the appropriate
    # slot in the tallies list
    for x in dataset:
        list[x] = list[x] + 1
    # 3. The index with the highest
    # value in tallies is the mode
    return max(list)

list2 = [1, 2, 2, 2, 11, 1, 3, 2, 12, 5, 3, 12, 21]

print("Fastmode results: ", fastMode(list2))

## Prof Zamansky's code
#def fastMode(dataset):
    # assume all values in dataset
    # are between 0  and 99 inclusive

    # tallies = []

    # 1. Make a list of 100 slots and set them all to 0
    # this will store our tallies

    # tallies = [0 for x in range(100)]

    # 2. Loop through a dataset and for each item increment
    # (add 1) to the appropriate slot in the tallies list

    # for item in dataset:
        # tallies[item] = tallies[item] + 1

    # 3. The index with the highest value in tallies is the mode
    
    #return tallies

# print(fastmode(list_2))

# --------------------------------------
def testMode(size, maxValue):
    dataset = buildRandomList(size, maxValue)
    # print(dataset)
    t = datetime.datetime.now()
    starttime = t.microsecond / 1000
    m = mode(dataset)
    end = datetime.datetime.now()
    elapsed = (end.microsecond / 1000) - starttime
    print("size: ", size, " time: ", elapsed)
    
testMode(40000,30)

def testFindLargest(size,maxValue):
    print("Datasize: ", size)
    dataset = buildRandomList(size,maxValue)
    #print(dataset)
    m = findLargest(dataset)
    print("Largest: ", m)

testFindLargest(10000,30)

# --------------------------------------

## pretend our program starts here
#dataset = [ some dataset]

#for item in dataset:
    #x = x do something with dataset
    #z = x + y
    #if z > something:
        #something
    #else:
        #something else


#for item in dataset:
    #do more stuff


x = 5
y = 10
if x > y:
    z = x + y
else:
    z = x * y
    z = z * z
z = x + y
z = z * z 
print(z)