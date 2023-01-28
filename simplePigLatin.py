# kata 5

def pig_it(text):
    words = text.split(" ")
    newWord = ""
    i = 1
    sentenceList = []
    
    for word in words:
        if word in ['!', '?']:
            sentenceList.append(word)
        else:
            chars = list(word)
            while i < len(chars):
                newWord += chars[i]
                i += 1
            newWord += chars[0] + "ay"
            sentenceList.append(newWord)
            newWord = ""
            i = 1
    
    final = " ".join(tuple(sentenceList))
    
    return final