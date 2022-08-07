import nltk
from nltk import word_tokenize, PunktSentenceTokenizer


# a function to put into memory the stored output.txt (aka hypotheses)
def sentence_tokenizer(sentence_list):
    file_content = list()
    index = 0

    for sentence in sentence_list:
        if index == 0:
            sentence = sentence.replace(u'\ufeff', '')
            index += 1

        tokens = word_tokenize(sentence.lower())
        
        output_sentence = ""

        for token in tokens:
            output_sentence += token + " "

        output_sentence = output_sentence[:(len(output_sentence) - 1)]  # remove last space
        file_content.append(output_sentence)

    file_content[0] = file_content[0].replace(u'\ufeff', '')  # ufeff character from document start
    return file_content


# a function to call to get the current bleu score
def get_bleu_score(hypothesis, reference):
    bleu_score = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
    return bleu_score


def read_file_save(file):
    # PunktSentenceTokenizer is an unsupervised algorithm that learns how to tokenize
    tokenizer = PunktSentenceTokenizer("Tagalog.txt")
    with open(file, encoding="utf-8") as file_reader:
        hypothesis_data = file_reader.readlines()

        hypothesis_lines = sentence_tokenizer(hypothesis_data)
        hypothesis_sentence = list()

    # transferring the data from the file reader to the memory
    for line in hypothesis_lines:
        token = tokenizer.tokenize(line)
        for word in token:
            hypothesis_sentence.append(word)

    return hypothesis_sentence


def solve_for_bleu(hypothesis_file_name, reference_file_name):
    # get the files and convert them into temporary files
    hypothesis_data = read_file_save(hypothesis_file_name)
    reference_data = read_file_save(reference_file_name)

    index = 0
    total_bleu_score = 0

    # solve for the bleu score
    for index in range(len(hypothesis_data)):
        bleu_score = get_bleu_score(hypothesis_data[index], reference_data[index])
        total_bleu_score += bleu_score
        print(bleu_score, "at index", index)

    print("Total BLEU Score", total_bleu_score, "/", index)
    print("BLEU Score is", bleu_score/index, " with an N of", index)
