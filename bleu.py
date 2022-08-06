import nltk
from nltk import word_tokenize

# di ko alam para saan ito
def convert(lst):
    return (lst[0].split())

# a function to put into memory the stored output.txt (aka hypotheses)
def sentence_tokenizer(sentence_list):
    file_content = list()
    index = 0

    # tbh I don't quite get this part
    for sentence in sentence_list:
        if index == 0:
            sentence = sentence.replace(u'\ufeff', '')
            index += 1

        tokens = word_tokenize(sentence.lower())

    # I also don't get this part
        otp_sentence = ""

        for token in tokens:
            otp_sentence += token + " "

        otp_sentence = otp_sentence[:(len(otp_sentence) - 1)]  # remove last space
        file_content.append(otp_sentence)

    # I also don't get this part
    file_content[0] = file_content[0].replace(u'\ufeff', '')  # ufeff character from document start
    return file_content

# a function to call to get the current bleu score
def get_bleu_score(hypothesis, reference):
    bleu_score = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
    return bleu_score

def read_file_save(file):
    # initialize tagalog sentences variable (list)
    tagalog_sentences = list()

    # tokenizer is a loader of the punkt library
    tokenizer = nltk.load('tokenizers/punkt/english.pickle')
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

    while True:
        try:
            ans = int(input('\n\nSolve for the bleu?\n\t'
                             '1: Yes\n\t'
                             '2: No\n\t'))
        except ValueError:
            print("Not a number")

        if ans == 1:
            # get the files and convert them into temporary files
            hypothesis_data = read_file_save(hypothesis_file_name)
            reference_data = read_file_save(reference_file_name)

            index = 0
            bleu_score = 0
            # to ensure that both data have the same length
            if len(hypothesis_data) == len(reference_data):
                for index in range(len(hypothesis_data)):
                    bleu_score += get_bleu_score(hypothesis_data[index], reference_data[index])
            else:
                print("Length of the data is not the same")

            print("BLEU Score is", bleu_score/index, " with an N of", index)

        elif ans == 2:
            break

        else:
            print("invalid mode")
