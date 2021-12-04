# About $ask
This command is used to ask a question in the q-and-a channel.
It will be auto-numbered and will have the author name next to the question.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/qanda.py).

# Code Description
## Functions

1. def ask(self, ctx, question):
   
   This function adds the question in the q-and-a channel.

Inputs:

- question: Entered question
   
# How to run it? (Small Example)
Enter space-separated: "$ask "question" "
```
$ask "How are you?"
```
Successful execution will add the question to the q-and-a channel.

![ask](https://user-images.githubusercontent.com/19858170/144726034-93cabf07-0e38-4614-bc40-0127f364db22.gif)
