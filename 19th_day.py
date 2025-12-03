'''
Write two functions. The first functionis calledcount_words
which takes a string of words as argument and counts how many
words are in the string.
The second function, called count_elements takes a string of
words and counts how many elements are in the string. Do not
count the whitespaces. The first function will return the number of
words in a string, and the second one will return the number of
elements (less whitespace). If you pass "I love learning", the
count_words function should return 3 words and
count_elements should return 13 elements.
'''

def calledcount_words (sentence):
    word_list = sentence.split(" ")
    word_count = 0
    for i in range(0, len(word_list) +1):
        word_count =+ i
    return print(word_count)

def count_elements(sentence):
    word_list = sentence.split(" ")
    letter_count = 0
    for i in word_list:
        letter_count = letter_count + len(i)
    return print(letter_count)

calledcount_words("i love learning")

count_elements("i love learning")

       
    