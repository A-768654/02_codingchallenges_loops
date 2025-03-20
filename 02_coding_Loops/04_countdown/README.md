### 🔹 Challenge 4: **Countdown Timer** (While Loop + Break)  
Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.  

**Example:**  
```
10  
9  
8  
Enter "stop" to cancel or press Enter:  
7  
6  
Enter "stop" to cancel or press Enter: stop  
Countdown stopped!
```

💡 **Hint:** Use `input()` inside the loop and check if the user entered `"stop"`.  

---

**Pseudocode**
1. Start
2. Start countdown from 10
3. set in Variable count
3. While count is greater than 0:
4. Print count
5. Subtract 1 from count each time
6. Prompt user to enter "stop" to stop or press enter to continue
7. Store in variable "userinput"
8. If user input is equal to "stop"
9. Print "countdown stopped!"
10. Break/end the loop
11. If count is equal to 0
12. Print "countdown finished"
13. End