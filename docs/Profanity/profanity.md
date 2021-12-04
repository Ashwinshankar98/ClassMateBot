# About $custom
This command is used to add a custom word to be considered as profane.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/profanity.py).

# Code Description
## Functions

1. def on_message(self, message):
   
   This function checks for profanity in all messages.

Inputs:

- message: Entered message
   
2. def on_message_edit(self, before, after):

This function checks for profanity on edited messages.

Inputs:

- before: Original msg
- after: Edited msg

3. def custom(self, ctx, text):

    This function adds the custom word to the custom profanity filter.

Input:

-text: Custom word to be added to the filter

# How to run it? (Small Example)
Enter space-separated: "$custom word"
```
$custom word
```
Successful execution will add the word to the profane list and block it.

![image](https://user-images.githubusercontent.com/19858170/144726498-ec56a292-220c-495f-a791-6ae36a031dc4.png)

![image](https://user-images.githubusercontent.com/19858170/144726475-0eedb449-c2cf-46eb-941d-6bbad64980b5.png)

![image](https://user-images.githubusercontent.com/19858170/144726486-eae3073c-c7e9-43eb-992f-bf73198a5a2d.png)

