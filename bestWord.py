

def getGuess(words, letterFreq):
    leaderboard = []
    guess = ""
    high = 0
    for word in words:
        points = 0
        repeated = ""
        for letter in word:
            if not(letter in repeated): # skip repeated letters in word
                points += letterFreq[letter] #
                repeated += letter
        leaderboard.append(points) # add points to leaderboard

    for item in range(len(leaderboard)): # find the word with the highest points
        if leaderboard[item] > high:
            high = leaderboard[item]
            guess = words[item]
    return guess
