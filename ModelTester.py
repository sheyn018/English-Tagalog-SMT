import numpy as np
from nltk.tokenize import word_tokenize
import string


def get_tokens_of_sentence(sentence):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    sentence = sentence.translate(translate_table)
    tokens = word_tokenize(sentence.lower())
    return tokens


def test_data(sentence_to_translate, translate_option):
    tagalog_to_english_maximised = np.load("trained_data/tagalog_to_english_maximised.npy", allow_pickle=True).item()
    english_to_tagalog_maximised = np.load("trained_data/english_to_tagalog_maximised.npy", allow_pickle=True).item()

# Option 1 == FILIPINO TO ENGLISH
# Option 2 == ENGLISH TO FILIPINO
    if translate_option == 1:
        sentence_from_file = get_tokens_of_sentence(sentence_to_translate)
        sentence_to_object = ""
        for word in sentence_from_file:
            if word in tagalog_to_english_maximised:
                sentence_to_object = sentence_to_object + tagalog_to_english_maximised[word] + " "
            else:
                print("word '" + word + "' does not exist in trained language translation dictionary")
                continue
        return sentence_to_object
    elif translate_option == 2:
        sentence_from_file = get_tokens_of_sentence(sentence_to_translate)
        sentence_to_object = ""
        for word in sentence_from_file:
            if word in english_to_tagalog_maximised:
                sentence_to_object = sentence_to_object + english_to_tagalog_maximised[word] + " "
            else:
                print("word '" + word + "' does not exist in trained language translation dictionary")
                continue
        return sentence_to_object


def test(sentence_to_translate, translate_option):
    return test_data(sentence_to_translate, translate_option)
