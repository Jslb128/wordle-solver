from words import words

# remove words that have a letter
def remove(let, arr):
    wordsToRmv = []
    for word in arr:
        if let in word:
            wordsToRmv.append(word)
    for rmv in wordsToRmv:
        arr.remove(rmv)

# return words that have a letter at that position
def fltrGreen(let,pos):
    gWords = []
    for word in words:
        if let == word[pos]:
            gWords.append(word)
            
    return gWords
# return words that have a letter but not at that postion
def fltrYellow(let, pos):
    newWords = []
    for word in words:
        if let in word and let != word[pos]:
            newWords.append(word)
    return newWords

# find words with two or more letters
def fltrDYellow(let):
    newWords = []
    for word in words:
        ltrs = 0
        for lt in range(0,5): # loop through the letters in word
            if word[lt] == let:# if letter == search letter
                ltrs+=1
        if ltrs >1:# if there are two same letters
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
        if i == "y" and letter in green:# if there are two of the same letter in this word
            words = fltrDYellow(letter)
        count+=1
    count = 0
    for i in result:
        letter = guess[count]
        if i == "b" and not(letter in green):# if this is not a repeated letter in guess word
            remove(letter,words)
        count+=1
    count = 0

    guess = words[0]
    possWords = len(words)

    print("possible words:", possWords)

    print("guess:\t", guess)
