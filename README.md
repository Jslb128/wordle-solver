A CLI program that filters out possible answers for a wordle game and returns the best possible word based on letter frequency.

---

## How to use
 - Run main.py
 - Program will give a guess word
 - Input the results in y/g/b (🟨🟩⬛)
 - It will then output a possible answer

 ## How it works
 Based on results it filters for possible words.
 Finds the best word in possbile words by looping through each word, and giving them a score; word with most common letters will rank higher and repeated letters get no points. 
 
