# Set misspelledWords = empty
# Check each word in document:
# 		If word is misspelled:
# 			add word to misspelledWords
# Return misspelledWords

from string import punctuation

def misspelled_words(document, dictionary_list):
    misspelled = []
    print(document.split())
    for word in document.split():
        if is_misspelled(word, dictionary_list) == True:
            misspelled.append(word)
    return misspelled




def is_misspelled(word, dictionary_list):
    """"""
    lower_case_word = word.lower()
    no_punc = lower_case_word.strip(punctuation)
    print(no_punc)
    if no_punc in dictionary_list:
        return False
    else:
        return True




document = "Computr science is fun.  We have spent time coding."
dictionary = ["computer","coding", "science", "is", "fun", "the", "how", "spent", "time", "we", "have"]
print(misspelled_words(document, dictionary))
# print(is_misspelled("Computer", dictionary))