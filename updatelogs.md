Aug 08, 2022 4:02 am - Jericho Longabela
Update/s:
        - Main.py
            > tweaked some formats (you can use yung yellow colors beside pycharm editor para malaman if may
                pwedeng maimprove sa formatting ng code)
            > removed getting bleu scores from main and moved it to both EnglishtoTagalog.py and TagalogtoEnglish.py
        - ModelTester.py
            > changed some variables and function for better readability
        - EnglishtoTagalog.py
            > changed some variables for better readability
        - TagalogtoEnglish.py
            > changed some variables for better readability
            > instead of "nltk.data.load('tokenizers/punkt/English.pickle')" for the tokenizer variable,
                I used PunktSentenceTokenizer("Tagalog.txt")
                ++ see https://www.nltk.org/api/nltk.tokenize.punkt.html for more info about this
        - bleu.py
            > changed some variable formats