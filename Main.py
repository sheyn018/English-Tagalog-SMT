import ModelTrainer
import ModelTester
import TagalogtoEnglish
import EnglishtoTagalog

while True:
    try:
        mode = int(input('\n\nPlease choose what you want to do: \n\t'
                         '1: Train the Model\n\t'
                         '2: Test sentence to translate\n\t'
                         '3: Translate a tagalog document to English \n\t'
                         '4: Translate an English document to tagalog \n\t'
                         '5: For exit\n'
                         'Input: '))
    except ValueError:
        print("Not a number")

    if mode == 1:
        ModelTrainer.model_trainer()

    elif mode == 2:
        try:
            translate_option = int(input('Select translation option: \n\t1: '
                                         'tagalog to English \n\t2: English to tagalog\n'))
        except ValueError:
            print("Not a number")
        if translate_option > 2 or translate_option < 1:
            print("Invalid Option")
            exit()
        sentence_to_translate = input("Please provide sentence to translate: ")

        translated_sentence = ModelTester.test(sentence_to_translate,translate_option)
        print(translated_sentence)

    elif mode == 3:
        # translate tagalog document to English
        TagalogtoEnglish.translate()

    elif mode == 4:
        # translate English document to tagalog
        EnglishtoTagalog.translate()

    elif mode == 5:
        break

    else:
        print("invalid mode")

print("goodbye!")
