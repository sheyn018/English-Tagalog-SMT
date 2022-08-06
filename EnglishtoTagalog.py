from nltk.tokenize import word_tokenize
import nltk.data
import string
import ModelTrainer
import ModelTester
import Utils

def sentence_tokenizer(sentence_list) :
    f_list = list()
    index_list = 0
    for sen in sentence_list:
        if index_list == 0 :
            sen = sen.replace(u'\ufeff', '')
            index_list += 1

        tokens = word_tokenize(sen.lower())

        output_sentence = ""

        for token in tokens :
            output_sentence += token + " "
        
        output_sentence = output_sentence[:(len(output_sentence)-1)]  #remove last space
        f_list.append(output_sentence)    

    f_list[0] = f_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return f_list    


def translate():
    tokenizer = nltk.data.load('tokenizers/punkt/tagalog.pickle')
    final_output = ""
    with open("EnglishTest(30%).txt", encoding="utf-8") as f:
        english_data = f.readlines()

    english_lines = sentence_tokenizer(english_data)

    english_sentences = list()
    for line in english_lines :
        curr_line = tokenizer.tokenize(line)
        for sen in curr_line :
            english_sentences.append(sen)

    otp_file = open("EnglishOutput(30%).txt", "w+", encoding="utf-8")
    for index in range(len(english_sentences)):
        current_sentence = english_sentences[index]
        translated_sentence = ModelTester.sentence_tester1(current_sentence, 2)
        otp_file.write(translated_sentence)
        otp_file.write(". ")
        
    print("\nSuccessfully translated! Translated document is 'EnglishOutput(30%).txt' ")
