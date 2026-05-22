# Wordle Solver
A CLI python program that filters out possible answers for a wordle game and returns the best possible word based on letter frequency.

---

## How to use
 - Run main.py
 ```bash
 python main.py
 ```
 - Program will give a guess word
 ```bash
 _____________________________
Possible words : 2315
Guess  : later
Result : 
```
 - Input the results in y/g/b (🟨🟩⬛)
 ```bash
 Result : bybby
 ```
 - It will then output a possible answer
 ```bash
 _____________________________
Possible words : 71
Guess  : acorn
Result : 
```

 ## How it works
 Based on results it filters for possible words based on letters on correct spot (g) wrong spot (y) or not in word (b), it also filters for words with double/single letters.

 Finds the best word in possbile words by looping through each word in list, and giving them a score; letter thats most common in the word list will get more points and repeated letters get no points. It will recalculate letter frequencies every turn with the new possible word list.
 
