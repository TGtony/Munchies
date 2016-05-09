from pymongo import MongoClient

#looks at mongodb on localhost
client = MongoClient()
db = client.munchies

#loop to query db with input string and output into array
def querydb(inputstring, outputarray):
    for item in inputstring:
        cursor = db.chips.find({"asin": item})
        for doc in cursor:
            #print(doc)
            outputstring.append(doc)
    return;



inputstr = "9742894116 B0000CNU2N B0000E5JQV"
#inputstr = input()

words = inputstr.split()

outputs =[]
outstring=""

querydb(words, outputs)

#putting items in array into string
for item in outputs:
    temp = str(item)
    outstring += temp
    #print(item)

print(outstring)
