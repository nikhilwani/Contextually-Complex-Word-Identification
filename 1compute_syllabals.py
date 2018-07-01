import pyphen
import curses 
from curses.ascii import isdigit 
import nltk
from nltk.corpus import cmudict
import csv
import numpy
import pandas as pd

from numpy import loadtxt





dic = pyphen.Pyphen(lang='en_US')
d = cmudict.dict()


filename = 'only_training_sentences.txt'
raw_data = open(filename, 'r',encoding='ascii',errors='ignore')
reader = csv.reader(raw_data, delimiter='\n', quoting=csv.QUOTE_NONE)

words = list(reader)

print("HERE")
print(words[:5])
#words = x

actual_import = []

for sentence in words:
    for s in sentence:
        actual_import.append(s)

syllabals_count = []
input_word = []


print(len(actual_import))
print(actual_import[:5])

#words = ['hello','cease-fire','reportedly','case yes yes','peace','plan','Nikhil','Meghalaya chief minister V. Shanmuganathan']

words = actual_import


def nsyl(word): 
   return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]


for n in words:
    input_word.append(n)
    
    #phrase wise
    if n.find(" ") != -1:
        #print("word:" + n)
        words = n.split()
        #print(words)
        
        counter = 0
        counterr = 0
        
        for e in words:
            try:
                counter = counter + nsyl(e)[0]
                #print("second-try-count:" + e)
                #print("Try phrase word")
            except Exception:
                counterr = 0
                for pair in dic.iterate(e):
                    #print("second-except-counterr")
                    #print(pair)
                    counterr = counterr + len(pair)
                    #print(counterr)

        #print("counter: " + str(counter))
        #print("counterr: " + str(counterr))
        #print(counter + counterr)
        final_count = counter + counterr
        syllabals_count.append(final_count)
        
    else:
        try:
            #print("word:" + n)
            #print(nsyl(n)[0])
            syllabals_count.append(nsyl(n)[0])
            #print("Executed in Try 1 word" )
        except Exception:
            counter = 0
            for pair in dic.iterate(n):
                #print("pairs:")
                #print(pair)
                #print(str(len(pair)) + "Executed in Except 1 word")
                counter = counter + len(pair)
                
            #print(counter)
            syllabals_count.append(counter)
            #print(" Executed in Except 1 word")        
    
#print(input_word)
#print(syllabals_count)

res = [input_word,syllabals_count]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('out.csv', index=False, header=False)
#printmy_df

'''  
with open('syllable_count.csv', 'w') as f:
    writer = csv.writer(f)
    for s in syllabals_count:
        writer.writerow([s])
'''

'''

    #word
        try:
            print(nsyl(n))
            print("Try 1 word")


        except Exception:
 
'''


 

      






  
    

