from words import words

def remove(let, arr):
    wordsToRmv = []
    for word in arr:
        if let in word:
            wordsToRmv.append(word)
    for rmv in wordsToRmv:
        arr.remove(rmv)


def fltrGreen(let,pos):
    gWords = []
    for word in words:
        if let == word[pos]:
            gWords.append(word)
            
    return gWords

def fltrYellow(let, pos):
    newWords = []
    for word in words:
        if let in word and let != word[pos]:
            newWords.append(word)
    return newWords
def fltrDYellow(let):#find words with two or more letters
    newWords = []
    for word in words:
        ltrs = 0
        for lt in range(0,5):
            if word[lt] == let:
                ltrs+=1
        if ltrs >1:
            newWords.append(word)

    return newWords

count = 0

result = "_"
guess = "stale"

print("guess:\t", guess)
while result != "ggggg":
    result = input("result: ")
    #filter words
    green = []
    for i in result:
        letter = guess[count]
        if i == "g":
            words = fltrGreen(letter, count)
            green.append(letter)
        count+=1
    count = 0
    for i in result:
        letter = guess[count]
        if i == "y":
            words = fltrYellow(letter, count)
        if i == "y" and letter in green:
            words = fltrDYellow(letter)
        count+=1
    count = 0
    for i in result:
        letter = guess[count]
        if i == "b" and not(letter in green):
            remove(letter,words)
        count+=1
    count = 0

    guess = words[0]
    possWords = len(words)

    print("possible words:", possWords)

    print("guess:\t", guess)
