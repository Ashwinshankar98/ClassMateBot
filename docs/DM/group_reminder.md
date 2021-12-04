# About $reminder
This command is used to send a reminder to all users in the guild.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/cogs/dm.py).

# Code Description
## Functions

1. def reminder(self, ctx,*,message=None):

This function is used to send a reminder to all users in the guild. 

Inputs:

        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - recipient name 
        - content 

Outputs: Bots response

# How to run it? (Small Example)
Enter space-separated: "$reminder hello"
```
$reminder "Submission Today for HW!!"
```
Successful execution will send a dm from classmate bot to all members

![Reminder](https://user-images.githubusercontent.com/19858170/144726697-2bc24b75-ed28-4e6b-9637-76b316f4a1f0.gif)
