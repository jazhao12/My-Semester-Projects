#James Zhao
#Feb 12
#Period 7
#Word Counter


#Initialize
import string

#Functions
def word_counter(sentence):
    x = ''
    y = ''
    z = string.punctuation
    my_table = sentence.maketrans(x, y, z)
    list_version = sentence.translate(my_table)
    list_version = list_version.split()
    list_version = list(list_version)
    print(list_version)
    words = len(list_version)
    print(f'There are {words} words.')

#Main
word_counter('This: is. an example, of a text; supplied as- an argument! with a like yes( or) no+')

