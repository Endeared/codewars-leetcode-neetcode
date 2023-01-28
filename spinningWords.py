# kata 6

def spin_words(sentence):
    words = sentence.split(" ")
    reversed = []
    newSentence = []
    i = 0
    newWord = ""
    for word in words:
        if len(word) >= 5:
            thisWord = list(word)
            thisWord.reverse()
            for char in thisWord:
                print(char)
                newWord += char
            reversed.append(newWord)
            newWord = ""
    
    for word in words:
        if len(word) >= 5:
            newSentence.append(reversed[i])
            i += 1
        else:
            newSentence.append(word)
            
    print(reversed)
    print(newSentence)
    final = " ".join(tuple(newSentence))
    return final