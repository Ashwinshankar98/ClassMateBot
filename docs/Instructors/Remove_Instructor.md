# About $removeInstructor
This command is used to remove a member from Instructors.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/instructor.py).

# Code Description
## Functions

1. def remove_instructor(self, ctx, member:discord.Member):

This function removes amember from Instructors.

Inputs:

- self: used to access parameters passed to the class through the constructor
- ctx: used to access the values passed through the current context
- member: name of member to be removed from instructor         

Outputs: Bots response

# How to run it? (Small Example)
Enter space separated: "$removeInstructor name"
```
$removeInstructor @user
```
Successful execution will remove the user as instructor and repond with bot message.

![image](https://user-images.githubusercontent.com/19858170/144727096-27c385e4-6e88-40ff-a084-354220f9632b.png)

