'''
team bpan
Brian Leung and Carol Pan
SoftDev2 pd7
HW17- something about books
2017-04-31
'''

from functools import reduce


dracula = open('dracula.txt', 'r')
draculist = dracula.read().replace("\r\n", " ").split(" ")
#print draculist

#find the frequency of a single word
def word_freq(word):
    lst = [1 for x in draculist if word.lower() == x.lower().strip(".?!,\'")]
    return reduce ((lambda x,y: x+y), lst) 

#find total frequency of a group of words



#find most frequently occuring word

print word_freq("dracula")
