from words import words

# return words that dont have a letter
def fltrBlack(searchLetter):
    newWords = []
    for word in words:
        if not(searchLetter in word):
            newWords.append(word)
    return newWords

# return words that have a letter at that position
def fltrGreen(searchLetter,pos):
    newWords = []
    for word in words:
        if searchLetter == word[pos]:
            newWords.append(word)
            
    return newWords

# return words that have a letter but not at that postion
def fltrYellow(let, pos):
    newWords = []
    for word in words:
        if let in word and let != word[pos]:
            newWords.append(word)
    return newWords

# return words with two or more letters
def fltrDLetters(searchLetter, mode):
    newWords = []
    for word in words:
        Dletters = 0
        for letter in word: # loop through the letters in word
            if letter == searchLetter:
                Dletters+=1
        if mode == "add":
     	    if Dletters > 1:# if there are two same letters
                newWords.append(word)
        elif mode == "rmv":
            if Dletters < 2:
                newWords.append(word)

    return newWords

result = ""
guess = "stale"
possWords = len(words)

while possWords > 0:
    print("_____________________________")
    print("Possible words :", possWords)
    print("Guess  :", guess)
    result = input("Result : ")

    #filter words
    green = []
    yellow = []
    lettersInWord = []
    for i in range(0,len(result)):
        letter = guess[i]
        if result[i] == "g":
            words = fltrGreen(letter, i)
            lettersInWord.append(letter)

    for i in range(0,len(result)):# loop for yellows
        letter = guess[i]

        if result[i] == "y" and letter in lettersInWord:# if there are two of the same letter in this word
            words = fltrDLetters(letter, "add")
        if result[i] == "y":
            words = fltrYellow(letter, i)
            lettersInWord.append(letter)

    for i in range(0,len(result)):
        letter = guess[i]
        if result[i] == "b" and not(letter in lettersInWord):# if this is not a repeated letter in guess word
            words = fltrBlack(letter)
        if result[i] == "b" and letter in lettersInWord:
            words = fltrDLetters(letter, "rmv")
            print("ran fltrDblack")
    possWords = len(words)
    try:
        guess = words[0]
        words.remove(guess)
    except:
        print("\nAnswer :", guess)
