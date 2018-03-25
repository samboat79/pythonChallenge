# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

f = open('hpexerpt.txt','r')
message = f.read()
print(message)
f.close()

#Define variables
numchars = 0
wordslist = 0
numwords = 0
wordlen = 0
sentnum = 0
average = 0

# #use for loop

with open('hpexerpt.txt','r') as file:
    for line in file:
        wordslist = line.split()
        numwords += len(wordslist)
        numchars += len(line) # getting length of the line on each iteration 
        wordlen = numchars/numwords
        average = sum(len(word) for word in wordslist)/len(wordslist)
        #avgsent = 
#now the output



#print the statments
print("-----------------------------------")

print("Paragraph Analysis")

print("-----------------------------------")

print("Approximate number of words: ", numwords)

print("Approximate letter count (per word): ", "%.2f" % wordlen)

print ("Approximate sentence count: ", open('hpexerpt.txt','r').read().count("."))
with open ('hpexerpt.txt') as f:
    data = f.read()

print ("Average sentence length (in words) ", "%.2f" % average)
