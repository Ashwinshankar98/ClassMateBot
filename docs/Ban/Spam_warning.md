# About Spam warning
This functionality tracks the messages and displays a warning to the members who are spamming the server.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../bot.py).

# Code Description

This is checked during every message.
The spam_log tracks the authors and displays a warning if the same person has more than 4 consecutive messages in the server.

   
# How to run it? (Small Example)
This is handled by the bot in the backend.


When a person has more than 4 consecutive msgs, after their 5th msg, warning will appear and all their spams will be deleted.

![Spam](https://user-images.githubusercontent.com/19858170/144726962-3ed63870-e0b5-4162-ac68-f86bcd9dc7aa.gif)
