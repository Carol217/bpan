'''team bpanBrian Leung and Carol PanSoftDev2 pd7HW17- Reductio ad Absurdum2017-04-31'''from functools import reducedracula = open('dracula.txt', 'r')draculist = dracula.read().replace("\"", "").replace("\n", " ").split(" ")#print draculist#find the frequency of a single worddef word_freq(word):    dl = [x[0 : x.index("'")] if "'" in x else x for x in draculist]    lst = [1 for x in dl if word.lower() == x.lower().strip(".?!,;")]    return reduce ((lambda x,y: x+y), lst) #find total frequency of a group of wordscount = -1def p_helper(phrase,x):    global count    #if the next word of the phrase is there    if phrase[count + 1] in x:        count += 1 #add to the count        #do not go out of bounds        if len(phrase) == count + 1:            count = -1            return 1        else:            return 0    #if the next word in phrase is NOT there    else:        count = -1        return 0def phrase_freq(phrase):    global count    count = -1    phrase = phrase.lower().split(" ")    lst = [p_helper(phrase,x.lower()) for x in draculist]    return reduce((lambda x,y: x+y), lst) #find most frequently occuring worddef top_word():    returnprint word_freq("Dracula")print phrase_freq("Dracula")print phrase_freq("Count Dracula")print phrase_freq("Do you know")