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

# def buildRandomList(size, maxvalue):
    # result = []
    # for x in range(size):
        # result.appened(random.randrange(maxvalue))
    # return result

    ## or

    ## List Comprehensions
    # result = [random.randrange(max value) for x in range(size)]
    # return result

# dataset = buildRandomList(20,30)
# print(findLargest(dataset))
# print(freq(dataset,3))