# COMPUTING LEXICAL FEATURES!
import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
import csv

# Number of sub categories. Eg, animal -> Dog, cat etc.
total_hyponyms = 0

# Number of parent categories.
total_hypernyms_paths = 0

#to_do
total_meronmys = 0
total_holonyms = 0

# Walk, invovles stepping. (Verb)
total_verb_entailments = 0

total_synonyms = 0

filename = 'only_train_words_semeval.txt'
raw_data = open(filename, 'r',encoding='ascii',errors='ignore')
reader = csv.reader(raw_data, delimiter='\n', quoting=csv.QUOTE_NONE)
w_words = list(reader)

actual_import = []

for sentence in w_words:
    for s in sentence:
        actual_import.append(s)

words = actual_import

#words = ['tree', 'bath', 'drive', 'talk tree bath']
total_synonyms_vector = []
total_hyponyms_vector = []
total_hypernyms_paths_vector = []
total_holonyms_vector = []
total_meronmys_vector = []
total_verb_entailments_vector = []

input_words = []

for eachword in words:
    
    input_words.append(eachword)

    #print(eachword)
    # if a phrase
    if eachword.find(" ") != -1:
        #print("if")
        words = eachword.split()
        #print(words)

        total_hyponyms = 0
        total_hypernyms_paths = 0
        total_meronmys = 0
        total_holonyms = 0
        total_verb_entailments = 0
        total_synonyms = 0
        
        for e in words:


            syn_word = wn.synsets(e)
            total_synonyms = total_synonyms + len(wn.synsets(e))

            #average polysemy of nouns, verbs, adjectives, and adverbs
            for each_word in syn_word:
                total_hyponyms = total_hyponyms + len(each_word.hyponyms())
                #print(each_word.hyponyms())
                
                paths = each_word.hypernym_paths()
                total_hypernyms_paths = total_hypernyms_paths + len(paths)
                #print(len(paths))

                #print(entailments)
                entailments = each_word.entailments()
                total_verb_entailments = total_verb_entailments + len(entailments)

                member_holonyms = each_word.member_holonyms()
                total_holonyms  = total_holonyms + len(member_holonyms)

                meronyms = each_word.part_meronyms()
                length = len(meronyms)
                total_meronmys = total_meronmys + length

        total_synonyms_vector.append(total_synonyms)
        total_hyponyms_vector.append(total_hyponyms)
        total_hypernyms_paths_vector.append(total_hypernyms_paths)
        total_holonyms_vector.append(total_holonyms)
        total_meronmys_vector.append(total_meronmys)
        total_verb_entailments_vector.append(total_verb_entailments)

    # only word
    else:
        #print("else")
        total_hyponyms = 0
        total_hypernyms_paths = 0
        total_meronmys = 0
        total_holonyms = 0
        total_verb_entailments = 0
        total_synonyms = 0
        
        syn_word = wn.synsets(eachword)
        total_synonyms = len(wn.synsets(eachword))

        #average polysemy of nouns, verbs, adjectives, and adverbs
        for each_word in syn_word:
            total_hyponyms = total_hyponyms + len(each_word.hyponyms())
            #print(each_word.hyponyms())
            
            paths = each_word.hypernym_paths()
            total_hypernyms_paths = total_hypernyms_paths + len(paths)
            #print(len(paths))

            #print(entailments)
            entailments = each_word.entailments()
            total_verb_entailments = total_verb_entailments + len(entailments)

            member_holonyms = each_word.member_holonyms()
            total_holonyms  = total_holonyms + len(member_holonyms)

            meronyms = each_word.part_meronyms()
            length = len(meronyms)
            total_meronmys = total_meronmys + length

        total_synonyms_vector.append(total_synonyms)
        total_hyponyms_vector.append(total_hyponyms)
        total_hypernyms_paths_vector.append(total_hypernyms_paths)
        total_holonyms_vector.append(total_holonyms)
        total_meronmys_vector.append(total_meronmys)
        total_verb_entailments_vector.append(total_verb_entailments)

'''
print(input_words)
print(total_synonyms_vector)
print(total_hyponyms_vector)
print(total_hypernyms_paths_vector) 
print(total_holonyms_vector) 
print(total_meronmys_vector) 
print(total_verb_entailments_vector)
'''

res = [input_words,total_synonyms_vector,total_hyponyms_vector,total_hypernyms_paths_vector,total_holonyms_vector,total_meronmys_vector,total_verb_entailments_vector]
my_df = pd.DataFrame(res)
df = my_df.T
df.to_csv('lexical_features.csv', index=False, header=False)
