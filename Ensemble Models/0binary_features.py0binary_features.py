import csv
import pandas as pd

filename1 = 'ogdens_basic1420.txt'
filename2 = 'ogdens_freq1000.txt'
filename3 = 'barrons_4853_complex_gre.txt'


raw_data_1 = open(filename1, 'r',encoding='ascii',errors='ignore')
raw_data_2 = open(filename2, 'r',encoding='ascii',errors='ignore')
raw_data_3 = open(filename3, 'r',encoding='ascii',errors='ignore')


# for ogden's basic
reader_1   = csv.reader(raw_data_1, delimiter = ' ', quoting=csv.QUOTE_NONE )
reader_2   = csv.reader(raw_data_2, delimiter = '\n', quoting=csv.QUOTE_NONE )
reader_3   = csv.reader(raw_data_3, delimiter = '\n', quoting=csv.QUOTE_NONE )


words_1   = list(reader_1)
words_2   = list(reader_2)
words_3   = list(reader_3)

# For ogden's basic
print(len(words_1[0]))
print(len(words_2))
print(len(words_3))

#print(words_3[0])

z = ['abase','a']

thing = words_3[0][:5]
print(type(thing))

print(thing)
#print(z)


'''
input_word = 'act'




'''
flatten_words1 = words_1[0]
flatten_words2 = []
flatten_words3 = []

for sublist in words_3:
    for item in sublist:
        flatten_words3.append(item)

for sublist in words_2:
    for item in sublist:
        flatten_words2.append(item)


'''
print(flatten_words3[:5])
print(flatten_words1[:5])
print(flatten_words2[:5])
'''

basic_ogden = []
fre_ogden   = []
barrons     = []


# Replace with file handling code
filename = 'only_development_sentences.txt'
raw_data = open(filename, 'r',encoding='ascii',errors='ignore')
reader = csv.reader(raw_data, delimiter='\n', quoting=csv.QUOTE_NONE)

words = list(reader)

actual_import = []

for sentence in words:
    for s in sentence:
        actual_import.append(s)

input_words = []


words = actual_import

for n in words:
    input_words.append(n)
    
    #phrase wise
    if n.find(" ") != -1:
        #print("word:" + n)
        words = n.split()
        #print(words)

        flag1 = 0
        flag2 = 0
        flag3 = 0
        
        for e in words:

            if flag1 != 1:
                if e in flatten_words1:
                    basic_ogden.append(1)
                    flag1 = 1
                else:
                    flag1 = 0
                    
            if flag2 != 1:
                if e in flatten_words2:
                    fre_ogden.append(1)
                    flag2 = 1
                else:
                    flag2 = 0

            if flag3 != 1:
                if e in flatten_words3:
                    barrons.append(1)
                    flag3 = 1
                else:
                    flag3 = 0
                    
        if flag1 == 0:
            basic_ogden.append(0)

        if flag2 == 0:
            fre_ogden.append(0)

        if flag3 == 0:
            barrons.append(0)
            
    else:
            if n in flatten_words1:
                basic_ogden.append(1)
            else:
                basic_ogden.append(0)

            if n in flatten_words2:
                fre_ogden.append(1)
            else:
                fre_ogden.append(0)

            if n in flatten_words3:
                barrons.append(1)
            else:
                barrons.append(0)
                



res = [input_words,basic_ogden]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('basic_ogden.csv', index=False, header=False)


res = [input_words,fre_ogden]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('fre_ogden.csv', index=False, header=False)


res = [input_words,barrons]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('barrons.csv', index=False, header=False)

res = [input_words]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('input_word.csv', index=False, header=False)


