# Don't do this for project
# Only use split when doing basic stuff
#f = open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv")
#for line in f.readlines():
    #print(line)
    #line = line.strip()
    #print(line.split(","))


# Example using csv module into a list
import csv
#reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#for line in reader:
    #print(line)

# Example- average the ages
#reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#num_people = 0
#sum = 0
#for line in reader:
    #num_people = num_people + 1
    #sum = sum +int(line[2])
#print(sum/num_people)

# Can use list comprehensions
#reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#ages = [int(line[2]) for line in reader]
#print(sum(ages))

# Using a csv.reader on a data set
# Where the first line are the filed/column names
#reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#full_data = [x for x in reader]
#field_names = full_data[0]
#data = full_data[1:]

# Using the csv.DictReader
#reader = csv.DictReader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#for item in reader:
    #print(item)

# Using csv.DictReader to create a list of dictionaries
#reader = csv.DictReader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#data = []
#for item in reader:
    #data.append(item)
#print(data)

# Using DictReader and list comprehensions
#reader = csv.DictReader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/demo.csv"))
#data = [x for x in reader]
#print(data)

# Get all comedy ratings using a loop
#comedy = []
#for item in data:
    #comedy.append(int(item['Comedy']))

# Get all comedy using a comprehensions
#comedy =  [int(x['Comedy']) for x in data]

# Get all people who like comedy (>5)
#likes_comedy = [x['Code name'] for x in data if int(x['Comedy'])>5]

# Also likes horror 
#likes_comedy_andhorror = [x['Code name'] for x in likes_comedy if int(x['Horror']) > 6]



