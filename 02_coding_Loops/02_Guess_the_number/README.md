Write a program that generates a random number between `1` and `10` and keeps asking the user to guess it using a `while` loop **until they guess correctly**.  

**Example:**  
```
Guess the number: 4  
Wrong, try again!  
Guess the number: 7  
Correct! 🎉
```

**Pseudocode**
1. Start
2. Import Random
3. Generate a random number between 1-10
4. Store randomly generated number in an integer variable "secret_number"
5. prompt user to input a number
6. Store number in an integer variable "guess"
7. If guess is equal to secret_number:
8. Print "Correct! Congrats!"
9. Exit loop
10. Else (if not equal to):
11. Print "Wrong! try again!"
12. End