#-----------------------------------------------------------------------------
# Name:        Skipping Even Numbers
# Purpose:     Write a program that prints numbers from `1` to `10`, but **skips even numbers** using the `continue` statement.
#
# Author:      Aleeza Siddiqui
# Created:     5-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

import time
for number in range(1, 11):  # >:) -from prutha  >:( -from Aleeza
    if number % 2 == 0:
        continue
    print(number)
    time.sleep(1)
