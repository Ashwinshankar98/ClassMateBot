# About $answer
This command is used to answer a question in the q-and-a channel.
It will be updated right after the question with answer tag along with the rle of the person who answered the question(Instructor/Student).

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/qanda.py).

# Code Description
## Functions

1. def answer(self, ctx, q_num, ans):
   
   This function updated the given question number with the given answer.

Inputs:

- q_num: Question number
- ans: Answer to be updated
   
# How to run it? (Small Example)
Enter space-separated: "$answer q_num "ans" "
```
$answer 1 "Good Thanks:)"
```
Successful execution will update the question with the answer.

![Answer](https://user-images.githubusercontent.com/19858170/144726077-c297a06e-16c7-4ce8-9c1e-57e510f8fd42.gif)
