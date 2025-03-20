#-----------------------------------------------------------------------------
# Name:        Countdown Timer (While Loop + Break)
# Purpose:     Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.
#
# Author:      Aleeza Siddiqui
# Created:     6-Mar-2025
# Updated:     7-Mar-2025
#-----------------------------------------------------------------------------

count = 10
while count > 0:
    print(count)
    count -= 1

#user input
    userinput = input('enter "stop" to cancel or press Enter to continue: ')
    if userinput.lower() == 'stop':
        print("countdown stopped!")
        break

#when countdown reaches 0
if count == 0:
    print("countdown finished!")