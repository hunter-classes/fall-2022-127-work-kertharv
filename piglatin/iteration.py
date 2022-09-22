#this is a foreach loop
for i in range(4):
  print(i)

for counter in range(4):
  print(counter)

for i in range(2,20,3):
  print(i)

for counter in range(5):
  print(counter)

for counter in [0,1,2,3,4]:
  print(counter)

for letter in "this is a sentence":
  print(letter)

#while loop
#loop_counter = 0
#while random.randrange(0,100) < 80: 
  #print("hello", loop_counter)
  #loop_counter = loop_counter + 1
#print("The above loop ran this many times: ", loop_counter)

#while loop as a counting loop
#first set up a variable to hold the count
i = 0
#then use the boolean to indicate when to stop
while i < 5:
  print(i)
  i = i + 1 #don't forget to change the variable so you eventually stop

#or count down
i = 5
while i > 0:
  print(i)
  i = i - 1

#you can also traverse over a string
s = 'hello world'
i = 0
while i < len(s):
  print(s[i])
  i = i + 1

for i in range(len(s)):
  print(s[i])