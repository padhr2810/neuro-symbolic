


############################## directory structure: 
### .py file is in main dir
### folder in main dir called transcripts


##############################
############################## import dependencies

import keras
import tensorflow as tf

from collections import Counter
import collections
import csv
import math
import nltk
from nltk.tokenize import sent_tokenize
import numpy as np
import os
import pandas as pd
import random
import re
from six.moves import range
from six.moves.urllib.request import urlretrieve
import string
import zipfile

import sklearn
from sklearn.model_selection         import train_test_split
from sklearn.linear_model            import LogisticRegressionCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn import svm


import matplotlib.pyplot as plt
from matplotlib import pylab

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Added version check for recent scikit-learn 0.18 checks
from distutils.version import LooseVersion as Version
from sklearn import __version__ as sklearn_version
if Version(sklearn_version) < '0.18':
    from sklearn.cross_validation import GridSearchCV
else:
    from sklearn.model_selection import GridSearchCV



############################## set up 1: empty list to contain the X text  """each turn is a string (ie a list of strings)"""
##############################        2: empty list for file names (each file name is a string)   """list of strings"""
##############################        3: empty array to contain the X vectors (i.e. sparse vectors)   """
##############################		  4: list of trigger phrases (cleaned i.e. lower case, removed punctuation)
"""

"""

X_txt_all_files  =  []
all_text_files_names = []
X_sparse_all_files = np.empty([0,0])
list_of_trigger_phrases  =  []




############################## 
############################## set up  5: SDM score for every turn: & SDM trigger phrase & item for turns (ie where SDM score is not zero obviously):
############################## 
"""
list of integers
"""

list_sdmAnyScore_each_turn = []
list_sdmScoreOO5_1_each_turn = []
list_sdmScoreOO5_2_each_turn = []
list_sdmScoreOO5_3_each_turn = []
list_sdmScoreOO5_4_each_turn = []
list_sdmScoreOO5_5_each_turn = []

list_sdmPhrases_each_turn = []   
list_item_each_turn = []           ### is it item 1-5
oo5_hits_count = 0                 ### total freq of triggers


##############################
##############################  define func - save all txt file names from 'dir' in a list: 'all_text_files_names'
##############################  """ list of strings """

def list_all_text_files_names(dir):
    my_cwd = os.getcwd()
    
    for root, dirs, files in os.walk("{}/{}".format(my_cwd, dir)):
        for file in files:
            if file.endswith('.txt'):
                all_text_files_names.append(file)
    print("The list of files in folder: {}".format(all_text_files_names))
    return all_text_files_names



############################## upload all txt files --- each 'turn' as separate string in list
############################## but only include utterances -- i.e. anything with a time in this format: "dd:dd"

all_text_files_names  =  list_all_text_files_names("transcripts")

for file  in  all_text_files_names:
    for turn in open("transcripts/{}".format(file)):  # where file_name is a string naming a file
        if re.match(r"[0-9][0-9]:[0-9][0-9]", turn):  # remove turn if doesn't have nn:nn (e.g. 53:58)
            X_txt_all_files.append(turn)


#########  check that only included genuine turns (i.e. with a timestamp at beginning)
for x in range(100):
    print("Turn {}: {}".format(x, X_txt_all_files[x]))

print("Type of X_txt_all_files: {}".format(type(X_txt_all_files)))


#########  remove redundant bits from each turn (e.g. timestamp, "D1:" etc)

def clean_list_of_strings(X_txt_all_files):
    for turn in range(len(X_txt_all_files)):
        X_txt_all_files[turn] = re.sub(r"[0-9][0-9]:[0-9][0-9]",  '',  X_txt_all_files[turn])
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("D1:", "")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("P1:", "")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("A1:", "")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("N1:", "")
        X_txt_all_files[turn] = re.sub('\'', '', X_txt_all_files[turn])         ### replace ' with empty (e.g. it's she's i've )
        X_txt_all_files[turn] = re.sub('\’', '', X_txt_all_files[turn])         ### replace ’ with empty 
        X_txt_all_files[turn] = re.sub('\”', '', X_txt_all_files[turn])         ### replace ” with empty 
        X_txt_all_files[turn] = re.sub('\“', '', X_txt_all_files[turn])         ### replace “ with empty 
        X_txt_all_files[turn] = re.sub('\…', '', X_txt_all_files[turn])         ### replace … with empty 
        X_txt_all_files[turn] = re.sub('%', ' percent', X_txt_all_files[turn])         ### replace … with empty 
        X_txt_all_files[turn] = re.sub('['+string.punctuation+']', ' ', X_txt_all_files[turn])        ### replace punctuation with space.
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("          ", " ")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("         ", " ")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("        ", " ")		### get rid of excess spaces.
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("   ", " ")
        X_txt_all_files[turn] = X_txt_all_files[turn].replace("  ", " ")
        X_txt_all_files[turn] = X_txt_all_files[turn].lower()				### lower case.
    return X_txt_all_files

X_txt_all_files = clean_list_of_strings(X_txt_all_files)


print("X_txt_all_files 1-10: \n{}".format(X_txt_all_files[:50]))
print("length of X_txt_all_files: {}".format(len(X_txt_all_files)))
from dict_words_to_correct import *

initial_len_X_txt_all_files =  len(X_txt_all_files)
for i in range(len(X_txt_all_files)):
    """
	use a hand-crafted dict (built by manually reviewing every unique token in corpus)
		to replace some tokens in corpus e.g. due to mispellings.
	"""
	
    temp_data = X_txt_all_files[i]
    temp_data = temp_data.split()           ####### split string into 1 list of items (split on white space)
    temp_data = [dict_words_to_correct_data.get(item,item)  for item in temp_data]
    temp_data_str = " ".join(temp_data)
    X_txt_all_files[i] = temp_data_str

new_len_X_txt_all_files =  len(X_txt_all_files)
assert initial_len_X_txt_all_files == new_len_X_txt_all_files


#########  check that removed the right stuff from each turn.
for x in range(100):
    print("Turn {}: {}".format(x, X_txt_all_files[x]))


######### SET of all tokens - every unique token and see what needs to be removed (e.g. '<unintelligible>')

set_tokens = []
for turn in range(len(X_txt_all_files)):
    tokens_from_one_turn = [i for i in X_txt_all_files[turn].split()]
    set_tokens.extend(tokens_from_one_turn)
set_tokens = set(set_tokens)
print(set_tokens)
print("\n\nThe number of unique tokens: {}\n\n".format(len(set_tokens)))


with open("set_all_tokens_filesave", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(set_tokens)



##############################	  
############################## define CountVectorizer func & create array of SPARSE vectors corresponding to entire first document
##############################


# FORMAT:
# X_txt_all_files = [
#    'This is sentence_1',
#    'And this is a sentence_2',
# ]


def sentence_list_to_array(turn_list):
    vectorizer = CountVectorizer()
    X_vect_all_files = vectorizer.fit_transform(turn_list)
    print("\n\nType of X_vect_all_files: {}".format(type(X_vect_all_files)))
    print("\n\nShow the features used in vectorizer i.e. tokens: (alphabetical order) \n\n{}".format(vectorizer.get_feature_names()))
    print("\n\nNumber of features used in vectorizer i.e. tokens: \n{}".format(len(vectorizer.get_feature_names())))

    ### i.e. list of lists (sparse vectors)
    #X_sparse_all_files.extend(X_vect_all_files)
    return X_vect_all_files


X_sparse_all_files = sentence_list_to_array(X_txt_all_files)

print("\n\nDimensions of X_sparse_all_files: \n{}\n\n".format(X_sparse_all_files.ndim))
print("Shape of X_sparse_all_files: \n{}\n\n".format(X_sparse_all_files.shape))


##############################
##############################	create list of stop words
##############################

nltk.download('stopwords')
print('remove stop words')
stop = stopwords.words('english')
print("\n\nType of 'stop' object: {}\n\n".format(type(stop)))
print("\n\nFirst 10 stop words: {}\n\n".format(stop[:10]))


##############################
##############################	create tokenizer func
##############################    & Porter stem tokenizer func.

porter = PorterStemmer()
def tokenizer(text):
    return text.split()
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

str = "I'm ok. This is the ending"
new_str = tokenizer(str)
new_porter_str = tokenizer_porter(str)

print("\nOriginal string: {}".format(str))
print("Tokenized string: {}".format(new_str))
print("Porter tokenized string: {}\n".format(new_porter_str))


##############################  
##############################   import labels and trigger phrases --- clean the trigger phrases.
##############################   

df_trigger_phrases  =  pd.read_excel("oo5_trigger_phrases_clean.xlsx", columns=['item', 'score', 'phrase'])
print("df_trigger_phrases.head (DF BEFORE CLEANING): \n{}\n\n".format(df_trigger_phrases.head(5)))

##### Show the number of trigger phrases:  
print("\nThis is the number of trigger phrases: {}\n\n".format(len(df_trigger_phrases.index)))


list_of_trigger_phrases = list(df_trigger_phrases["phrase"])
print("First x10 list_of_trigger_phrases: \n{}".format(list_of_trigger_phrases[:10]))

list_of_trigger_phrases  =  clean_list_of_strings(list_of_trigger_phrases)

print("\n\nAFTER CLEANING - ALL OF: list_of_trigger_phrases:")
counter = 1
for trigger_phrase in list_of_trigger_phrases:
    print("Trigger Phrase {}: {}".format(counter,  trigger_phrase))
    counter += 1


##############################  After cleaning trigger phrases list, put back in the DF (call this "clean_phrase")
series_of_trigger_phrases = pd.Series(list_of_trigger_phrases)
series_of_trigger_phrases.rename("phrase_cleaned")
print(series_of_trigger_phrases.head())
df_trigger_phrases = pd.concat([df_trigger_phrases, series_of_trigger_phrases], axis=1)
print(df_trigger_phrases.head())
print("column headers in df_trigger_phrases: {}".format(list(df_trigger_phrases)))
df_trigger_phrases.columns = ['item','score','raw_phrase', 'clean_phrase']
print("df_trigger_phrases.head: {}\n\n".format(df_trigger_phrases.head(5))) 


##############################  
##############################   loop over every trigger phrase and every x-phrase --- see where matches.
##############################   generate OO5 score for every sentence.


###############   2x INPUTS:
####  1: df_x_txt 			  	-  data frame containing text of every turn.
####  2: df_trigger_phrases   	-  data frame containing every trigger phrase

###############   2x COUNTERS:
####  3: counter_x_turn		  	-  iterate over each X turn.
####  4: counter_trigger_phrase -  iterative over each trigger phrase (starts at 0 again for every X turn)

###############   3x OUTPUTS:
####  5: list_sdmAnyScore_each_turn 	-  SDM score each turn.
####  6: list_sdmPhrases_each_turn 	-  SDM trigger phrase for turns (ie where SDM score is not zero obviously)
####  7: oo5_hits_count       	-  total no. oo5 hits



df_x_txt = pd.DataFrame(data=X_txt_all_files, columns = ['x'])

print("df_x_txt.head: {}\n\n".format(df_x_txt.head(5)))
print("Dimensions of df_x_txt (i.e. number of sentences): {}\n\n".format(df_x_txt.shape))


counter_x_turn = 0   						
for x_turn in X_txt_all_files:					##### ie loop over each X strings
    list_sdmPhrases_each_turn.append(0)			##### put in 0 as the 'sdmPhrase' -- ie will put in real one if triggered.
    list_item_each_turn.append(0)				##### put in 0 as the 'item'     -- ensures list correct length to add 'item' & match "counter_x_turn" each time.
    list_sdmAnyScore_each_turn.append(0)				##### put in 0 as default 'score' 	  -- ie will put in higher score if triggered.
    list_sdmScoreOO5_1_each_turn.append(0)
    list_sdmScoreOO5_2_each_turn.append(0)
    list_sdmScoreOO5_3_each_turn.append(0)
    list_sdmScoreOO5_4_each_turn.append(0)
    list_sdmScoreOO5_5_each_turn.append(0)
		
    for counter_trigger_phrase in range(len(df_trigger_phrases.index)):                         	##### ie loop over each trigger phrases
        if df_trigger_phrases.iat[counter_trigger_phrase, 3] in df_x_txt.iat[counter_x_turn, 0]:    #####  if trigger_phrase matches part of x_turn:   
            list_sdmPhrases_each_turn[counter_x_turn]  =   \
			    df_trigger_phrases.at[counter_trigger_phrase, 'clean_phrase']						#####  record the triggering sdm phrase.
            list_sdmAnyScore_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']		##### update score
			
            if  df_trigger_phrases.at[counter_trigger_phrase, 'item']	== 1:
                list_sdmScoreOO5_1_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']	  ##### update score
            if  df_trigger_phrases.at[counter_trigger_phrase, 'item']	== 2:
                list_sdmScoreOO5_2_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']	  ##### update score
            if  df_trigger_phrases.at[counter_trigger_phrase, 'item']	== 3:
                list_sdmScoreOO5_3_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']	  ##### update score
            if  df_trigger_phrases.at[counter_trigger_phrase, 'item']	== 4:
                list_sdmScoreOO5_4_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']	  ##### update score
            if  df_trigger_phrases.at[counter_trigger_phrase, 'item']	== 5:
                list_sdmScoreOO5_5_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'score']	  ##### update score
				
            list_item_each_turn[counter_x_turn] = df_trigger_phrases.at[counter_trigger_phrase, 'item']			##### update item
            oo5_hits_count += 1																					##### times oo5 score triggered
    counter_x_turn += 1	
    if (counter_x_turn) % 1000 == 0:
	    print("Turns completed check for trigger phrases: {}".format(counter_x_turn))



##############################  
##############################   Create binary versions of OO5 scores:
##############################

def convert_to_bin(input_list):
    binary_list = [1 if x > 1 else x for x in input_list]
    return binary_list
	
list_sdmAnyScore_each_turn_bin = 		convert_to_bin(list_sdmAnyScore_each_turn)
list_sdmScoreOO5_1_each_turn_bin = 		convert_to_bin(list_sdmScoreOO5_1_each_turn)
list_sdmScoreOO5_2_each_turn_bin = 		convert_to_bin(list_sdmScoreOO5_2_each_turn)
list_sdmScoreOO5_3_each_turn_bin = 		convert_to_bin(list_sdmScoreOO5_3_each_turn)
list_sdmScoreOO5_4_each_turn_bin = 		convert_to_bin(list_sdmScoreOO5_4_each_turn)
list_sdmScoreOO5_5_each_turn_bin = 		convert_to_bin(list_sdmScoreOO5_5_each_turn)



##############################  
##############################   Count the OO5 scores (and the bin scores) for each class and aggregate.
##############################

list_scores_agg		 = [list_sdmAnyScore_each_turn, list_sdmAnyScore_each_turn_bin]
list_scores_per_item = [list_sdmScoreOO5_1_each_turn, list_sdmScoreOO5_2_each_turn, list_sdmScoreOO5_3_each_turn, 
    list_sdmScoreOO5_4_each_turn, list_sdmScoreOO5_5_each_turn]
list_scores_per_item_bin = [list_sdmScoreOO5_1_each_turn_bin, list_sdmScoreOO5_2_each_turn_bin, list_sdmScoreOO5_3_each_turn_bin, 
    list_sdmScoreOO5_4_each_turn_bin, list_sdmScoreOO5_5_each_turn_bin]

	
print("\n\n\n")
counter = 1
for x in list_scores_per_item:
    print("\nscore counter for list_sdmScoreOO5_", counter, "_each_turn: {}".format(Counter(x)))
    print("length of list_sdmScoreOO5_", counter, "_each_turn: {}".format(len(x)))
    counter+=1
	
print("\n\n\n")
counter = 1
for x in list_scores_per_item_bin:
    print("\nscore counter for list_sdmScoreOO5_", counter, "_each_turn_bin: {}".format(Counter(x)))
    print("length of list_sdmScoreOO5_", counter, "_each_turn_bin: {}".format(len(x)))
    counter+=1
	
print("\n\n\n")
for x in list_scores_agg:
    print("\nscore counter for {}: {}".format("Aggregate all items", Counter(x)))
    print("length of {}: {}".format("Aggregate all items", len(x)))



##############################  
##############################   Examine OO5 Phrases (from Robin etc) that DID and DID NOT trigger oo5 score in any turn.
##############################


unused_trigger_phrases = set(series_of_trigger_phrases).difference(list_sdmPhrases_each_turn)

###############  List the triggers in X  - and the missed triggers:
print("\n\n Trigger phrases in X: \n{}".format(set(list_sdmPhrases_each_turn)))
print("\n\n Trigger phrases NOT in X: \n{}".format(unused_trigger_phrases))

###############  Count the triggers in X  - and the missed triggers:
print("\n\n oo5_hits_count: {}".format(oo5_hits_count))
print("\n\n Number of Trigger phrases in X: {}".format(len(set(list_sdmPhrases_each_turn))))
print("\n\n Number of Trigger phrases NOT in X: {}".format(len(set(unused_trigger_phrases))))


"""
assert len(set(unused_trigger_phrases))  +  len(set(list_sdmPhrases_each_turn))  ==  len(set(series_of_trigger_phrases))
"""

############################## 
print("Note: len(list_sdmPhrases_each_turn): {}".format(len(list_sdmPhrases_each_turn)))
print("Note: len(list_sdmAnyScore_each_turn): {}".format(len(list_sdmAnyScore_each_turn)))
print("Note: len(X_txt_all_files): {}".format(len(X_txt_all_files)))
assert len(list_sdmPhrases_each_turn) == len(list_sdmAnyScore_each_turn) == len(X_txt_all_files) == X_sparse_all_files.shape[0]
print("asserted len(list_sdmPhrases_each_turn) == len(list_sdmAnyScore_each_turn) == len(X_txt_all_files) == X_sparse_all_files.shape[0]")


print("Note: X_sparse_all_files.shape[0]: {}".format(X_sparse_all_files.shape[0]))
print("Note: type(X_sparse_all_files): {}".format(type(X_sparse_all_files)))
print("Note: type of first item in: (X_sparse_all_files): {}".format(type(X_sparse_all_files[0])))

print("\nNote: X_sparse_all_files - First one: \n{}".format(X_sparse_all_files[:1]))
print("Note: X_txt_all_files - First one: \n{}".format(X_txt_all_files[:1]))

print("\nNote: X_sparse_all_files - Second one: \n{}".format(X_sparse_all_files[1:2]))
print("Note: X_txt_all_files - Second one: \n{}".format(X_txt_all_files[1:2]))

print("\nNote: X_sparse_all_files - Third one: \n{}".format(X_sparse_all_files[2:3]))
print("Note: X_txt_all_files - Third one: \n{}".format(X_txt_all_files[2:3]))

print("\nNote: X_sparse_all_files - Fourth one: \n{}".format(X_sparse_all_files[3:4]))
print("Note: X_txt_all_files - Fourth one: \n{}".format(X_txt_all_files[3:4]))



array_phrases_each_turn = np.array(list_sdmPhrases_each_turn)
array_score_each_turn_bin = np.array(list_sdmAnyScore_each_turn_bin)
print("\n\nset_score_each_turn - i.e. which scores were assigned: {}".format(set(array_score_each_turn_bin)))



########################################################################################################################


##############################  
##############################   split COUNTVECTORIZER SPARSE ARRAY into train / test.
##############################

X_train_countVect, X_val_countVect, y_train_countVect, y_val_countVect = train_test_split(
    X_sparse_all_files, 
    array_score_each_turn_bin, 
    test_size=0.33, 
    random_state=42)
	
print("X_train_countVect: {}".format(X_train_countVect[:100]))
print(X_train_countVect[-100:])
print("X_val_countVect: {}".format(X_val_countVect[-100:]))
print(X_val_countVect[:100])


##############################  
##############################    CLEAN "X_txt_all_files" A BIT -- REMOVE SPACE FROM START AND \n FROM END.
##############################   

X_txt_all_files_list  =  X_txt_all_files
#for x in range(len(X_txt_all_files_list)):
#    X_txt_all_files_list[x] = X_txt_all_files_list[x][1:]
#    X_txt_all_files_list[x] = X_txt_all_files_list[x][:-2]
	

##############################  
##############################     SPLIT EACH TURN STRING INTO LIST OF TOKENS.
##############################  

X_txt_all_files_list  =  [x.split(" ") for x in X_txt_all_files_list]
assert len(X_txt_all_files_list) == len(X_txt_all_files)
print("X_txt_all_files_list[:5]: {}".format(X_txt_all_files_list[:5]))
print("X_txt_all_files[:5]: {}".format(X_txt_all_files[:5]))
print("\nSplitted X_txt_all_files_list into list of lists (ie each token is item in list")


##############################  
##############################     TURN LENGTHS (NO. WORDS) - CUT OFF AT MAXIMUM.
############################## 

counter_for_all_sentence_lengths_dict = {}
max_sent_length = 0
n = 0
for x in X_txt_all_files_list:
    if len(x) > max_sent_length:
        max_sent_length = len(x)
    counter_for_all_sentence_lengths_dict[n] = len(x)
    n += 1
counter_for_all_sentence_lengths = Counter(sorted(list(counter_for_all_sentence_lengths_dict.values())))

print("\nmax_sent_length: {}".format(max_sent_length))
print("\ncounter_for_all_sentence_lengths: \n{}".format(counter_for_all_sentence_lengths))

##### TRIM THE SIZE OF SENTENCES TO A REASONABLE LEVEL FOR CNN PADDING: GO FOR 10.
for x in range(len(X_txt_all_files_list)):
    if len(X_txt_all_files_list[x]) > 10:
	    X_txt_all_files_list[x] = X_txt_all_files_list[x][:10]

print("\nReset max_sent_length to 10")
max_sent_length = 10



##############################  
##############################    DELETE ANY TURNS (& CORRESPONDING SCORES) WITH ONLY ONE WORD (AND CORRESPONDING LABEL OBVIOUSLY)
############################## 

list_indices_of_single_token_sentences = []
for i in range(len(X_txt_all_files_list)):
    if len(X_txt_all_files_list[i]) == 1:
        list_indices_of_single_token_sentences.append(i)
list_indices_of_single_token_sentences = sorted(list_indices_of_single_token_sentences, reverse=True)

##### OBVIOUSLY DONT DELETE INDICES FROM THE MAIN ONE - CREATE A NEW "CNN" ONE TO MODIFY. (IE DELETE ANY IF ONLY ONE WORD IN SENTENCE)
list_sdmAnyScore_each_turn_bin_cnn  =  list_sdmAnyScore_each_turn_bin
for i in list_indices_of_single_token_sentences:
    del X_txt_all_files_list[i]
    del list_sdmAnyScore_each_turn_bin_cnn[i]

array_score_each_turn_bin_cnn = np.array(list_sdmAnyScore_each_turn_bin_cnn)

assert len(X_txt_all_files) == len(X_txt_all_files_list) + len(list_indices_of_single_token_sentences)
assert len(array_score_each_turn_bin) == len(array_score_each_turn_bin_cnn) + len(list_indices_of_single_token_sentences)

#then do a counter of the sentence length for all sentences ....can prob drop last X words of some sentences i.e. put upper lmiit on number of tokens that will be included -- this will help run CNN more easily.
print("list_indices_of_single_token_sentences: {}".format(list_indices_of_single_token_sentences))




########################################################################################################################
########################################################################################################################  Sebastian Raschka - Python Machine Learning (chpt 8)
########################################################################################################################


tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)

param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__use_idf':[False],
               'vect__norm':[None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              ]

lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=42))])

gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='recall',
                           cv=5,
                           verbose=1,
                           n_jobs=-1)

y_pred = gs_lr_tfidf.fit(X_train_txt, y_train_txt).predict(X_val_txt)

print('\n\nBest parameter set: %s ' % gs_lr_tfidf.best_params_)
print('\n\nCV Recall: %.3f' % gs_lr_tfidf.best_score_)


clf = gs_lr_tfidf.best_estimator_
print('Validation Set Recall: %.3f' % clf.score(X_val_txt, y_val_txt))







##############################  
##############################    TRAIN-TEST SPLIT FOR CNN:
############################## 

X_train_txt_list4cnn, X_val_txt_list4cnn, y_train_txt, y_val_txt = train_test_split(
    X_txt_all_files_list, 
    array_score_each_turn_bin_cnn, 
    test_size=0.33, 
    random_state=42)



##### REVIEW THE INPUTS FOR CNN:  i.e. X_train_txt_list4cnn // X_val_txt_list4cnn // y_train_txt // y_val_txt
print("\n\n##### REVIEW THE INPUTS FOR CNN:  i.e. X_train_txt_list4cnn // X_val_txt_list4cnn // y_train_txt // y_val_txt")

print("\nX_train_txt_list4cnn: {}".format(X_train_txt_list4cnn[:10]))
print("\nX_val_txt_list4cnn: {}".format(X_val_txt_list4cnn[:10]))

print("\ny_train_txt[:10]: {}".format(y_train_txt[:10]))
print("\ny_val_txt[:10]: {}".format(y_val_txt[:10]))

print("\nConfirming the types")
print("type of X_train_txt_list4cnn: {}".format(type(X_train_txt_list4cnn)))
print("type of X_val_txt_list4cnn: {}".format(type(X_val_txt_list4cnn)))
print("type of y_train_txt: {}".format(type(y_train_txt)))
print("type of y_val_txt: {}".format(type(y_val_txt)))


#clf = LogisticRegressionCV(random_state=42, solver='lbfgs',
#                    multi_class='multinomial').fit(X_train_countVect, y_train_countVect)

##############################  
##############################   account for multiclass  - split into multiple binary classes
##############################  



##############################
##############################  run ML algorithms
##############################



########################################################################################################################
########################################################################################################################   CNN
########################################################################################################################





## 4x inputs:     X_train_txt_list4cnn, X_val_txt_list4cnn, y_train_txt, y_val_txt

y_train_txt_str   = []
y_val_txt_str     = []

for n in y_train_txt:
    if n == 0:
	    y_train_txt_str.append("Not_SDM")
    if n == 1:
	    y_train_txt_str.append("SDM")
for n in y_val_txt:
    if n == 0:
	    y_val_txt_str.append("Not_SDM")
    if n == 1:
	    y_val_txt_str.append("SDM")
		
print(Counter(y_train_txt))
print(len(y_train_txt_str))
assert len(y_train_txt_str) == len(y_train_txt)
assert len(y_val_txt_str) == len(y_val_txt)


######### Record the max length of the sentences -- as we need to pad shorter sentences accordingly




######### Padding Shorter Sentences --- so that all the sentences are of the same length.

print("Type of training X object: List of lists (i.e. the sub-lists contain 1 string = 1 word): {}".format(type(X_train_txt_list4cnn)))
print("Length of train X object: {}".format(len(X_train_txt_list4cnn)))
print("First 100 training X: {}".format(X_train_txt_list4cnn[:100]))


# Padding training data
for qi,que in enumerate(X_train_txt_list4cnn):
    for _ in range(max_sent_length-len(que)):
        que.append('PAD')
    assert len(que)==max_sent_length
    X_train_txt_list4cnn[qi] = que
print('\nTrain sentences padded')

# Padding testing data
for qi,que in enumerate(X_val_txt_list4cnn):
    for _ in range(max_sent_length-len(que)):
        que.append('PAD')
    assert len(que)==max_sent_length
    X_val_txt_list4cnn[qi] = que
print('\nValidation sentences padded')  

# Printing a test sentence to see if everything is correct
print('\nAFTER PADDING - Sample test sentence: %s',X_val_txt_list4cnn[0])




# ## Building the Dictionaries
# Builds the following. To understand each of these elements, let us also assume the text "I like to go to school"
# 
# * `dictionary`: maps a string word to an ID (e.g. {I:0, like:1, to:2, go:3, school:4})
# * `reverse_dictionary`: maps an ID to a string word (e.g. {0:I, 1:like, 2:to, 3:go, 4:school}
# * `count`: List of list of (word, frequency) elements (e.g. [(I,1),(like,1),(to,2),(go,1),(school,1)]
# * `data` : Contain the string of text we read, where string words are replaced with word IDs (e.g. [0, 1, 2, 3, 2, 4])
# 
# We do not replace rare words with "UNK" because the vocabulary is already quite small.


def build_cnn_dataset(sentences):
    words = []
    data_list = []
    count = []
    
    # First create a large list with all the words in all the sentences
    for d in sentences:
        words.extend(d)
    print('Number of Words (tokens) found in data: {}'.format(len(words)))   
    print('Found {} words in vocabulary.'.format(len(collections.Counter(words).most_common())))
    
    # Sort words by their frequency
    count.extend(collections.Counter(words).most_common())
    
    # Create an ID for each word by giving the current length of the dictionary
    # And adding that item to the dictionary
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    
    ##### Traverse through all the text and replace the string words with the ID of the word found at that index
    for d in sentences:
        data = list()
        for word in d:
            index = dictionary[word]        
            data.append(index)  
        data_list.append(data)
        
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys())) 
    
    return data_list, count, dictionary, reverse_dictionary

# Create a dataset with both train and test sentences
all_sentences = list(X_train_txt_list4cnn)
all_sentences.extend(X_val_txt_list4cnn)

# Use the above created dataset to build the vocabulary
all_sentence_ind, count, dictionary, reverse_dictionary = build_cnn_dataset(all_sentences)

# Print some statistics about the processed data
print('All words (count)', count[:5])
print('\n0th entry in dictionary: %s',reverse_dictionary[0])
print('\nSample data', all_sentence_ind[0])
print('\nSample data', all_sentence_ind[1])
print('\nVocabulary: ',len(dictionary))
vocabulary_size = len(dictionary)

print('\nNumber of training sentences: ',len(X_train_txt_list4cnn))
print('Number of testing sentences: ',len(X_val_txt_list4cnn))


# ## Generating Batches of Data
# ie generate a batch of data from a given set of sentences and labels.


batch_size = 16 # We process 16 sentences at a time
sent_length = max_sent_length

##### Number of classes
num_classes = 2 
all_labels = ['Not_SDM','SDM'] 

class BatchGenerator(object):
    '''
    Generates a batch of data
    '''
    def __init__(self,batch_size,sentences,labels):
        self.sentences = sentences
        self.labels = labels
        self.text_size = len(sentences)
        self.batch_size = batch_size
        self.data_index = 0
        assert len(self.sentences)==len(self.labels)
        
    def generate_batch(self):
        '''
        Data generation function. This outputs two matrices
        inputs: a batch of sentences where each sentence is a tensor of size
        [sent_length, vocabulary_size] with each word one-hot-encoded
        labels_ohe: one-hot-encoded labels corresponding to the sentences in inputs
        '''
        global sent_length,num_classes
        global dictionary, all_labels
        
        # Numpy arrays holding input and label data
        inputs = np.zeros((self.batch_size,sent_length,vocabulary_size),dtype=np.float32)
        labels_ohe = np.zeros((self.batch_size,num_classes),dtype=np.float32)
        
        # When we reach the end of the dataset
        # start from beginning
        if self.data_index + self.batch_size >= self.text_size:
            self.data_index = 0
            
        # For each sentence in the dataset
        for qi,que in enumerate(self.sentences[self.data_index:self.data_index+self.batch_size]):
            # For each word in the sentence
            for wi,word in enumerate(que): 
                # Set the element at the word ID index to 1
                # this gives the one-hot-encoded vector of that word
                inputs[qi,wi,dictionary[word]] = 1.0
            
            # Set the index corrsponding to that particular class to 1
            labels_ohe[qi,all_labels.index(self.labels[self.data_index + qi])] = 1.0
        
        # Update the data index to get the next batch of data
        self.data_index = (self.data_index + self.batch_size)%self.text_size
            
        return inputs,labels_ohe
    
    def return_index(self):
        # Get the current index of data
        return self.data_index

# Check our batch generator
sample_gen = BatchGenerator(batch_size,X_train_txt_list4cnn,y_train_txt_str)
# Generate a single batch
sample_batch_inputs,sample_batch_labels = sample_gen.generate_batch()
# Generate another batch
sample_batch_inputs_2,sample_batch_labels_2 = sample_gen.generate_batch()

# Make sure that we have the sentence 0 as the 0th element of our batch
assert np.all(np.asarray([dictionary[w] for w in X_train_txt_list4cnn[0]],dtype=np.int32) 
              == np.argmax(sample_batch_inputs[0,:,:],axis=1))

# Print some data labels we obtained
print('Sample batch labels')
print(np.argmax(sample_batch_labels,axis=1))
print(np.argmax(sample_batch_labels_2,axis=1))






##############################
##############################  Sentence Classifying Convolution Neural Network
##############################  Defining hyperparameters and inputs

tf.reset_default_graph()

batch_size = 32
# Different filter sizes we use in a single convolution layer
filter_sizes = [3,5,7] 

# inputs and labels
sent_inputs = tf.placeholder(shape=[batch_size,sent_length,vocabulary_size],dtype=tf.float32,name='sentence_inputs')
sent_labels = tf.placeholder(shape=[batch_size,num_classes],dtype=tf.float32,name='sentence_labels')


################################################################# 
################################################################# SET UP CNN MODEL ARCHITECTURE.
################################################################# 

# One layer (with 3 different parallel layers). 
# Followed by a pooling-over-time layer
# a fully connected layer produces the logits.


# ## Defining Model Parameters
# * 3 sets of convolution layer weights and biases (one for each parallel layer)
# * 1 fully connected output layer

# 3 filters with different context window sizes (3,5,7)
# Each of this filter spans the full one-hot-encoded length of each word and the context window width

# Weights of the first parallel layer
w1 = tf.Variable(tf.truncated_normal([filter_sizes[0],vocabulary_size,1],stddev=0.02,dtype=tf.float32),name='weights_1')
b1 = tf.Variable(tf.random_uniform([1],0,0.01,dtype=tf.float32),name='bias_1')

# Weights of the second parallel layer
w2 = tf.Variable(tf.truncated_normal([filter_sizes[1],vocabulary_size,1],stddev=0.02,dtype=tf.float32),name='weights_2')
b2 = tf.Variable(tf.random_uniform([1],0,0.01,dtype=tf.float32),name='bias_2')

# Weights of the third parallel layer
w3 = tf.Variable(tf.truncated_normal([filter_sizes[2],vocabulary_size,1],stddev=0.02,dtype=tf.float32),name='weights_3')
b3 = tf.Variable(tf.random_uniform([1],0,0.01,dtype=tf.float32),name='bias_3')

# Fully connected layer
w_fc1 = tf.Variable(tf.truncated_normal([len(filter_sizes),num_classes],stddev=0.5,dtype=tf.float32),name='weights_fulcon_1')
b_fc1 = tf.Variable(tf.random_uniform([num_classes],0,0.01,dtype=tf.float32),name='bias_fulcon_1')


# ## Defining Inference of the CNN
# Here we define the CNN inference logic. First compute the convolution output for each parallel layer within the convolution layer. Then perform pooling-over-time over all the convolution outputs. Finally feed the output of the pooling layer to a fully connected layer to obtain the output logits.

# Calculate the output for all the filters with a stride 1
# We use relu activation as the activation function
h1_1 = tf.nn.relu(tf.nn.conv1d(sent_inputs,w1,stride=1,padding='SAME') + b1)
h1_2 = tf.nn.relu(tf.nn.conv1d(sent_inputs,w2,stride=1,padding='SAME') + b2)
h1_3 = tf.nn.relu(tf.nn.conv1d(sent_inputs,w3,stride=1,padding='SAME') + b3)

# Pooling over time operation

# This is doing the max pooling. There are two options to do the max pooling
# 1. Use tf.nn.max_pool operation on a tensor made by concatenating h1_1,h1_2,h1_3 and converting that tensor to 4D
# (Because max_pool takes a tensor of rank >= 4 )
# 2. Do the max pooling separately for each filter output and combine them using tf.concat 
# (this is the one used in the code)

h2_1 = tf.reduce_max(h1_1,axis=1)
h2_2 = tf.reduce_max(h1_2,axis=1)
h2_3 = tf.reduce_max(h1_3,axis=1)

h2 = tf.concat([h2_1,h2_2,h2_3],axis=1)

# Calculate the fully connected layer output (no activation)
# Note: since h2 is 2d [batch_size,number of parallel filters] 
# reshaping the output is not required as it usually do in CNNs
logits = tf.matmul(h2,w_fc1) + b_fc1



################################################################# 
################################################################# Model Loss and the Optimizer
################################################################# 

# Loss (Cross-Entropy)
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=sent_labels,logits=logits))

# Momentum Optimizer
optimizer = tf.train.MomentumOptimizer(learning_rate=0.01,momentum=0.9).minimize(loss)

# ## Model Predictions
# Note that we are not getting the raw predictions, but the index of the maximally activated element in the prediction vector.


################################################################# 
#################################################################   RUN THE MODEL.
################################################################# 

predictions = tf.argmax(tf.nn.softmax(logits),axis=1)


# ## Running Our Model to Classify Sentences
# Below we run our algorithm for 50 epochs. With the provided hyperparameters you should achieve around 90% accuracy on the test set. However you are welcome to play around with the hyperparameters.

# With filter widths [3,5,7] and batch_size 32 the algorithm 
# achieves around ~90% accuracy on test dataset (50 epochs). 
# From batch sizes [16,32,64] I found 32 to give best performance

session = tf.InteractiveSession()

num_steps = 50 # Number of epochs the algorithm runs for

# Initialize all variables
tf.global_variables_initializer().run()
print('Initialized\n')

print("X_train_txt_list4cnn 1-100: {}".format(X_train_txt_list4cnn[:100]))
print()


# Define data batch generators for train and test data
train_gen = BatchGenerator(batch_size,X_train_txt_list4cnn,y_train_txt_str)
test_gen = BatchGenerator(batch_size,X_val_txt_list4cnn,y_val_txt_str)

# How often do we compute the test accuracy
test_interval = 1

# Compute accuracy for a given set of predictions and labels
def accuracy(labels,preds):
    return np.sum(np.argmax(labels,axis=1)==preds)/labels.shape[0]

# Running the algorithm
for step in range(num_steps):
    avg_loss = []
    
    # A single traverse through the whole training set
    for tr_i in range((len(X_train_txt_list4cnn)//batch_size)-1):
        # Get a batch of data
        tr_inputs, tr_labels = train_gen.generate_batch()
        # Optimize the network and compute the loss
        l,_ = session.run([loss,optimizer],feed_dict={sent_inputs: tr_inputs, sent_labels: tr_labels})
        avg_loss.append(l)

    # Print average loss
    print('Train Loss at Epoch %d: %.2f'%(step,np.mean(avg_loss)))
    test_accuracy = []
    
    # Compute the test accuracy
    if (step+1)%test_interval==0:        
        for ts_i in range((len(X_val_txt_list4cnn)-1)//batch_size):
            # Get a batch of test data
            ts_inputs,ts_labels = test_gen.generate_batch()
            # Get predictions for that batch
            preds = session.run(predictions,feed_dict={sent_inputs: ts_inputs, sent_labels: ts_labels})
            # Compute test accuracy
            test_accuracy.append(accuracy(ts_labels,preds))
        
        # Display the mean test accuracy
        print('Test accuracy at Epoch %d: %.3f'%(step,np.mean(test_accuracy)*100.0))










########################################################################################################################
########################################################################################################################  Confusion matrix. -- 
########################################################################################################################

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax



	

np.set_printoptions(precision=2)

class_names = ["Not_SDM", "SDM"]

# Run classifier, using a model that is too regularized (C too low) to see
# the impact on the results

#classifier = svm.SVC(kernel='linear', C=0.01)
#y_pred = classifier.fit(X_train_countVect, y_train_countVect).predict(X_val_countVect)


print("\n\nSet of y_val_countVect:")
print(set(y_val_countVect))
print("Length of y_val_countVect: {}".format(len(y_val_countVect)))
print("Type of y_val_countVect: {}".format(type(y_val_countVect)))

print("\n\nSet of y_pred:")
print(set(y_pred))
print("Length of y_pred: {}".format(len(y_pred)))
print("Type of y_pred: {}".format(type(y_pred)))

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_val_countVect, y_pred, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plot_confusion_matrix(y_val_countVect, y_pred, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()


##############################
##############################  Next Steps.
##############################
"""

create DF for all X that trigger OO5 (i.e. DF TO INCLUDE: X // trigger phrase // OO5 label // OO5 score)
	ensure the triggers are doing their job properly for appropriate X values:

calculate the % of turns with a positive OO5.

add LSTM --- BOTH WAYS - I.E. LEFT TO RIGHT, AND RIGHT TO LEFT.

predict  5x categories according to each oo5 classes. --- i.e. main model will be 'any SDM form' -- and other classes will be 'oo1 - oo5'

Training and validation curve.
K-fold cross val.

FINALLY when working well - extend it to all transcripts.
"""
