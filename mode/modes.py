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

    