# About $askanonym
This command is used to ask a question in the q-and-a channel anonymously.
It will be auto-numbered and instead of the author name it will have <i>anonymous</i> next to the question.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/qanda.py).

# Code Description
## Functions

1. def askanonym(self, ctx, question):
   
   This function adds the question in the q-and-a channel with <i> Anonymous</i> tag.

Inputs:

- question: Entered question
   
# How to run it? (Small Example)
Enter space-separated: "$askanonym "question" "
```
$askanonym "Is it okay?"
```
Successful execution will add the question to the q-and-a channel with <i> Anonymous</i> tag.

![Ask_anonym](https://user-images.githubusercontent.com/19858170/144726153-aba55b13-079f-44bd-8976-e6304c7fc792.gif)
