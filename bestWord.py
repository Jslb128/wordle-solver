

def getGuess(words):
    scoreboard = []
    leaderboard = {}
    guess = ""
    high = 0
    #recalculate letter frequencies
    letterFreq = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for word in words:
        for letter in word:
            letterFreq[letter]+=1
    # percentage calculation
    total = len(words)*5
    for letter in letterFreq:
        letterFreq[letter] = letterFreq[letter]/total*100
    for word in words:
        points = 0
        repeated = ""
        for letter in word:
            if not(letter in repeated): # skip repeated letters in word
                points += letterFreq[letter] #
                repeated += letter
        scoreboard.append(points) # add points to scoreboard

    for item in range(len(scoreboard)): # find the word with the highest points
        if scoreboard[item] > high:
            high = scoreboard[item]
            guess = words[item]
    return guess
