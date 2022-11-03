# Chapter 12 Exercises 1, 2, and 3

# Exercise 1

x = input("Write a sentence: ")

x = x.lower()   # convert to all lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])

# Exercise 2
def add_fruit(inventory, fruit, quantity=0):
     pass

# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
#  test that new_inventory['strawberries'] is 10
add_fruit(new_inventory, 'strawberries', 25)
#  test that new_inventory['strawberries'] is now 35)


# Exercise 3

f = open('/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/dictionary/alice.txt', 'r')

count = {}

for line in f:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")