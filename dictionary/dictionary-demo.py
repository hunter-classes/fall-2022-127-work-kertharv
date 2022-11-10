d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list'] = [2,3,4,5,6]
d[(1,2)] = 55

print(d)

d['list'] = 55.3

print(d)

person = {'fist' : "John",
        'last' : "Smith",
        'age' : 50,
        'height' : 60}
person['age'] = person['age'] + 1

print(person)

person['last'] = "Tang"
person.pop('height')

print(person)

k = person.keys()
print(k)
for item in k:
        print(item)

for item in k:
        print('person[',item,'] = ',person[item])

# convert the dict_keys thing into a list:
klist = [x for x in person.keys()]
print(klist)

personv = person.values()
print(personv)

# pull out the values and convert to list
vlist = [x for x in person.values()]
print(vlist)

i = person.items()
print(i)

xl = [3,5]
xt = (3,5)
yt = ('hello',44,34.5)
a,b,c = yt
print(xl)
print(xt)
print(xt[0])
print(yt)

for k,v in person.items():
        print(k,v)

for k in person.keys():
        print(k,person[k])

s1 = {'gender':'m','name':'barney','id':1,'scores':[100,90,85]}
s2 = {'gender':'f','name':'jen','id':2,'scores':[95,85]}
s3 = {'gender':'m','name':'marcel','id':3,'scores':[99,76,88,82]}
s4 = {'gender':'f','name':'sookie','id':1,'scores':[98]}

student_list = [s1,s2,s3,s4]
student_dict = {}
for item in student_list:
        student_dict[item['id']] = item

print(student_list)

print("---------------------------------------")

s="""this is a string with abunch of lower case letters. There's nothing too interesting 
about it other than the fact that there are a bunch of words over multiple lines and we're going 
to do some processing on them"""

def count_letters(s):
        """
        Count the number of times each letter appears in s
        """
        counts = {}
        for letter in s:
                if letter in counts.keys():
                        counts[letter] = counts[letter] + 1
                else:
                        counts[letter] = 1
        return counts

def count_words(s):
        counts = {}
        for word in s.split():
           counts.setdefault(word,0)
           counts[word] = counts[word] + 1
        return counts

letter_counts = count_letters(s)
word_counts = count_words(s)
print(letter_counts)
print("---------------------------------------")
print(word_counts)

translations = """a:b c:d oldword:newword"""
print(translations)
print(translations.split())
print("oldword:newword".split())
