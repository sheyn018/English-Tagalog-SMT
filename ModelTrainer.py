# import nltk
from nltk.tokenize import word_tokenize
import IBM1_EM
import string
import numpy as np
import Utils


def sentence_tokenizer(sentence_list, max_index):
    final_list = list()
    word_dictionary = {}    #this dictionary will keep both word and its order in its language
    reverse_dictionary = {}
    lang_order = 0
    cnt = 0
    translate_table = dict((ord(char), None) for char in string.punctuation)
    for r in sentence_list[:max_index]:
        if cnt == 0 :
            r = r.replace(u'\ufeff', '')
            cnt += 1

        r = r.translate(translate_table)            #remove punctuation
        tokens = word_tokenize(r.lower())

        produced_sentence = ""
        for token in tokens:
            if token not in word_dictionary:
                word_dictionary[token] = lang_order
                reverse_dictionary[lang_order] = token
                lang_order += 1
            produced_sentence = produced_sentence + token + " "
        produced_sentence = produced_sentence[:(len(produced_sentence) - 1)]  # remove last space

        final_list.append(produced_sentence)

    final_list[0] = final_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return final_list, word_dictionary, reverse_dictionary


def model_trainer():
    with open("English.txt", encoding="utf8") as f:
        english_data = f.readlines()
        #print("\n*****\n******\n",english_data)
        #print("\n*****\n******\n",len(english_data))

    with open("Tagalog.txt", encoding="utf8") as f:
        tagalog_data = f.readlines()
        #print("\n*****\n******\n",tagalog_data)
        #print("\n*****\n******\n",len(tagalog_data))
        

    #just use sentences with length at most 25 words.
    new_english_data = list()
    new_tagalog_data = list()

    for sen_marker in range(len(english_data)):
        if sen_marker > 500000 :
            break 
        cur_en_sen = english_data[sen_marker].split()                #tokenizing current sentence
        cur_tr_sen = tagalog_data[sen_marker].split()
        new_english_data.append(english_data[sen_marker])
        new_tagalog_data.append(tagalog_data[sen_marker])

    english_data = new_english_data.copy()                          # english_data is now a list of tokenized sentence
    tagalog_data = new_tagalog_data.copy()                          # i.e. a list of sentences where each sentence is a list of words

    #max_num_of_translations = 1000
    max_num_of_translations = 3000

    # parse tagalog sentences, tokenize the words
    tagalog_sentences, tagalog_word_dict, reverse_tagalog_word_dict = sentence_tokenizer(tagalog_data, max_num_of_translations)

    # parse english sentences, tokenize the words
    english_sentences, english_word_dict, reverse_english_word_dict = sentence_tokenizer(english_data, max_num_of_translations)

 
    #run the EM algorithm of IBM Model 1
    translate_eng_tagalog  = IBM1_EM.expectation_maximization(tagalog_word_dict,english_word_dict,tagalog_sentences,english_sentences)
    

    # The following code finds out the maximum probability 
    # for translating a tagalog/English word to English/tagalog
    # from the existing e-f matrix.
    # These maximum probabilities are stored in dictionaries 
    # and saved as .npy files for being used for translation
 
    total_tagalog_ocurrences = translate_eng_tagalog.shape[0]
    total_eng_occurrences = translate_eng_tagalog.shape[1]

    #final dictionaries for translation mapping
    english_map = {}
    tagalog_map = {}

    for eng_marker in range(total_eng_occurrences): #for all foreign words f do
        maximum = -100
        i = 0
        for tagalog_marker in range(total_tagalog_ocurrences):
         #for all English words e do
            if translate_eng_tagalog[tagalog_marker][eng_marker] > maximum : 
                maximum = translate_eng_tagalog[tagalog_marker][eng_marker]
                i = tagalog_marker

        english_map[reverse_english_word_dict[eng_marker]] = reverse_tagalog_word_dict[i]
        #end for
    #end for
    for tagalog_marker in range(total_tagalog_ocurrences): #for all foreign words f do
        maximum = -100
        i = 0
        for eng_marker in range(total_eng_occurrences):
         #for all English words e do
            if translate_eng_tagalog[tagalog_marker][eng_marker] > maximum : 
                maximum = translate_eng_tagalog[tagalog_marker][eng_marker]
                i = eng_marker
        #end for
        tagalog_map[reverse_tagalog_word_dict[tagalog_marker]] = reverse_english_word_dict[i]
    #end for    

    np.save("trained_data/tagalog_to_english_maximised",tagalog_map)
    np.save("trained_data/english_to_tagalog_maximised",english_map)