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

        otp_sentence = ""

        for token in tokens :
            otp_sentence += token + " "
        
        otp_sentence = otp_sentence[:(len(otp_sentence)-1)]  #remove last space
        f_list.append(otp_sentence)    

    f_list[0] = f_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return f_list    


def translate() :
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    f_Output = ""
    with open("TagalogTest(30%).txt", encoding="utf-8") as f:
        tagalog_data = f.readlines()

    tagalog_lines = sentence_tokenizer(tagalog_data)

    tagalog_sentences = list()
    for line in tagalog_lines:
        l = tokenizer.tokenize(line)
        for sen in l:
            tagalog_sentences.append(sen)

    otp_file = open("TagalogOutput(30%).txt", "w+", encoding="utf-8")
    for index in range(len(tagalog_sentences)):
        current_sentence = tagalog_sentences[index]
        translated_sentence = ModelTester.sentence_tester1(current_sentence, 1)
        otp_file.write(translated_sentence)
        otp_file.write(". \n")
        
    print("\nSuccessfully translated! Translated document is 'TagalogOutput(30%).txt' ")
