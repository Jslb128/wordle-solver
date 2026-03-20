from words import words

def remove(let):
    wordsToRmv = []
    for word in words:
        if let in word:
            wordsToRmv.append(word)
    for rmv in wordsToRmv:
        words.remove(rmv)


def searchAt(let,pos):
    gWords = []
    for word in words:
        if let == word[pos]:
            gWords.append(word)
            
    return gWords

def isYellow(let, pos):
    newWords = []
    for word in words:
        if let in word and let != word[pos]:
            newWords.append(word)
    return newWords

count = 0

result = "_"
guess = "stale"
while result != "ggggg":
    result = input("result: ")

    for i in result:
        if i == "b":
            letter = guess[count]
            remove(letter)
        elif i == "g":
            letter = guess[count]
            words = searchAt(letter, count)
        elif i == "y":
            letter = guess[count]
            words = isYellow(letter, count)
        count+=1
    print(words[0])
    guess = words[0]
    count = 0


