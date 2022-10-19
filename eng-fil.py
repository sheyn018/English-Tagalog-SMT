import nltk
import numpy as np
from nltk.tokenize import word_tokenize
import string

def get_tokens_of_sentence(sentence):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    sentence = sentence.translate(translate_table)
    tokens = word_tokenize(sentence.lower())
    return tokens

def sentence_tester1(sentence_to_translate, translate_option):
    english_to_tagalog_maximised = np.load("trained_data/english_to_tagalog_maximised.npy", allow_pickle=True).item()

    if translate_option == 2:
        e_sentence = get_tokens_of_sentence(sentence_to_translate)
        f_sentence = ""
        for word in e_sentence:
            if word in english_to_tagalog_maximised:
                f_sentence = f_sentence + english_to_tagalog_maximised[word] + " "
            else:
                continue
        return f_sentence

filepath = 'EnglishTest(30%).txt'
df=open("output.txt","w", encoding="utf-8")

with open(filepath) as fp:
   line = fp.readline()

   while line:
    line = fp.readline()
    sentence_to_translate = line
    translate_option = 2;
    translated_sentence = sentence_tester1(sentence_to_translate,translate_option)

    df.write(translated_sentence)
    df.write('\n')

    def test(sentence_to_translate,translate_option):
        return sentence_tester1(sentence_to_translate,translate_option)
df.close()
fp.close()
