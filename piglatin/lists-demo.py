s = "this is a string"
elist = []
l1 = [12,33,15,20]
l2 = ['one','two','three']
l3 = ['one', 2, 122, 33, 'something', 23]
l4 = ['one', 23, ['a','b','c'], 5, [10,11,12]]
slice = l1[3:5]
longer_string =  s + s
long_list = l1 + l3
#s[5] = "I" <-- Can't do this - strings are immutable
#We have to do this:
new_string = s[:5] + 'I' + s[6:]
#On the other hand, we can change lists directly
l1[4] = 999999

#you can change a list's elements in a function
#but this is generally frowned upon
#since you don't return anything
#which can be confusing to many programmers
def change in_place(l,index,new_value):
    l[index] = new_value
print(l1)
change_in_place(l1,4,123)
print(l1)

# This is slightly better
def change_in_place_and_return(l,index,new_value):
    """
    THIS CHANGES 1 and returns it
    """
    l[index] = new_value
    return l

print(l1)
change_in_place_and_return(l,4,321)
print(l2)
print(l1)
