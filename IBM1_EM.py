import numpy as np
import math
import Utils


# expectation maximization
def expect_max(pfil_word_dict, pen_word_dict, plst_fil_sen, plst_en_sen):
    fil_occur = len(pfil_word_dict)
    en_occur = len(pen_word_dict)

    # IBM1 Expectaion Maximization algorithm
    trans_en_fil_matrix = np.full((len(pfil_word_dict), len(pen_word_dict)), 1 / len(pen_word_dict), dtype=float)
    trans_en_fil_matrix_prev = np.full((len(pfil_word_dict), len(pen_word_dict)), 1, dtype=float)

    int_count = 0
    while not Utils.is_converged(trans_en_fil_matrix, trans_en_fil_matrix_prev, int_count):
        int_count += 1

        # making the current matrix as the old one
        trans_en_fil_matrix_prev = trans_en_fil_matrix.copy()

        # initializing the enfil's value as 0
        total_enfil = np.full((len(pfil_word_dict), len(pen_word_dict)), 0, dtype=float)

        # initializing the final total value
        total_fin = np.full((len(pen_word_dict)),0, dtype=float)

        for int_index, lst_fil_sen in enumerate(plst_fil_sen):  # for all sentence pairs (e,f) do
            # computing for the normalization
            lst_fil_words = lst_fil_sen.split(" ")
            total_sen = np.full((len(lst_fil_words)), 0, dtype=float)

            # for all words in the filipino list of words
            for int_index2 in range(len(lst_fil_words)):
                str_fil_word = lst_fil_words[int_index2]
                total_sen[int_index2] = 0
                lst_en_words = plst_en_sen[int_index].split(" ")

                # for all string words in the list of words
                for str_en_word in lst_en_words:
                    # continue even if the string is empty
                    if str_en_word == '':
                        continue

                    int_index_fildict = pfil_word_dict[str_fil_word]
                    int_index_endict = pen_word_dict[str_en_word]
                    total_sen[int_index2] += trans_en_fil_matrix[int_index_fildict][int_index_endict]
                #end for
            #end for

            #collect counts
            lst_fil_words = lst_fil_sen.split(" ")

            for int_index2 in range(len(lst_fil_words)): #for all words e in e do
                str_fil_word = lst_fil_words[int_index2]
                lst_en_words = plst_en_sen[int_index].split(" ")

                for str_en_word in lst_en_words: #for all words f in f do
                    if str_en_word == '' :
                        continue
                    int_index_fildict = pfil_word_dict[str_fil_word]
                    int_index_endict = pen_word_dict[str_en_word]
                    total_enfil[int_index_fildict][int_index_endict] += trans_en_fil_matrix[int_index_fildict][int_index_endict] / total_sen[int_index2]
                    total_fin[int_index_endict] += trans_en_fil_matrix[int_index_fildict][int_index_endict] / total_sen[int_index2]
                #end for
            #end for
        #end for

        #estimate probabilities
        for int_en_index in range(en_occur):  # for all foreign words f do

            for int_fil_index in range(fil_occur):  # for all English words e do

                if total_enfil[int_fil_index][int_en_index] != 0 :
                    trans_en_fil_matrix[int_fil_index][int_en_index] = total_enfil[int_fil_index][int_en_index] / total_fin[int_en_index]

            #end for
            
        #end for

    #end while

    print("EM Algorithm Converged in ",(int_count-1)," iterations")
    return trans_en_fil_matrix


def get_translation_prob(e, f, t, e_dict, f_dict):
    const = Utils.const
    l_e = len(e)
    l_f = len(f)
    res = const / math.pow((l_f+1),l_e)
    for j in range(l_e):
        e_word = e[j]
        if e_word in e_dict:
            e_j = e_dict[e_word]
        else:
            print("word '"+ e_word +"' is not found in target language dictionary")
            continue
            #return 0

        sum = 0
        for i in range(l_f):
            f_word = f[i]

            if f_word in f_dict:
                f_i = f_dict[f_word]
                sum += t[e_j][f_i]
            else:
                print("word '" + f_word  +"' is not found in source language dictionary")

        res *= sum

    return res