def clean(s):
    letters = []
    for l in s:
        if l.isalpha() or l==' ' or l=='\n':
            letters.append(l)
    result = "".join(letters)
    result = result.lower()
    return result 

def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts

def get_words_min_max(bag,mincount,maxcount):
    results = []
    for word in bag.keys():
        if bag[word] >= mincount and bag[word] <= maxcount:
            results.append([word,bag[word]])
    return results

# same as above but with a list comprehension
def get_words_range(bag,mincount,maxcount):
    results = [ [x, bag[x]] for x in bag if bag[x] >= mincount \
        and bag[x] <= maxcount]
    return results

print(get_words_min_max(bag,100,500))

file = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/dictionary/scandal.txt")

raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)
print(bag)

print("--------------------------------")
l = [3,2,5,5,87,4,23,1]
print(sorted(l)) # Sorts the list in numeric order

l2 = sorted(l)
print(l2[-1:]) # Sorts to the last item of the list