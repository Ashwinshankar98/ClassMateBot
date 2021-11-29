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
Enter space-separated: "$custom never"
```
$custom never
```
Successful execution will add the word to the profane list and block it.

![profanity](./profanity.png)
