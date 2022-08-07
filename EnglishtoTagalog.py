from nltk.tokenize import word_tokenize
import nltk.data
import ModelTester
import bleu


def sentence_tokenizer(sentence_list):
    token_list = list()
    index_list = 0
    for word in sentence_list:
        if index_list == 0 :
            word = word.replace(u'\ufeff', '')
            index_list += 1

        tokens = word_tokenize(word.lower())

        output_sentence = ""

        for token in tokens:
            output_sentence += token + " "
        # remove last space
        output_sentence = output_sentence[:(len(output_sentence)-1)]
        token_list.append(output_sentence)

    token_list[0] = token_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return token_list


def translate():
    # tokenizer loads the pre-trained English model for punkt tokenizer
    tokenizer = nltk.data.load('tokenizers/punkt/English.pickle')
    with open("EnglishTest(30%).txt", encoding="utf-8") as file_reader:
        english_data = file_reader.readlines()

    english_lines = sentence_tokenizer(english_data)

    english_sentences = list()
    for line in english_lines:
        current_line = tokenizer.tokenize(line)
        for word in current_line:
            english_sentences.append(word)

    output_file = open("TagalogOutput(30%).txt", "w+", encoding="utf-8")
    for index in range(len(english_sentences)):
        current_sentence = english_sentences[index]
        translated_sentence = ModelTester.test_data(current_sentence, 2)
        output_file.write(translated_sentence)
        output_file.write("\n")
        
    print("\nSuccessfully translated! Translated document is 'TagalogOutput(30%).txt' ")

# Get BLEU Score
    bleu.solve_for_bleu("TagalogOutput(30%).txt", "EnglishTest(30%).txt")