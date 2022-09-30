#Exercise 3
myList = [76, 92.3, 'hello', True, 4, 76]

myList.append(76)
myList.append("apple")
myList.insert(3, "cat")
myList.insert(0, 99)

#index = myList.index("hello")
#print(index)
print(myList.index('hello'))
print(myList.count(76))
print(myList)
myList.remove(76)
myList.pop(myList.index(True))
print(myList)