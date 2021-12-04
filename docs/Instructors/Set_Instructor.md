# About $setInstructor
This command is used to set a member as instructor.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/instructor.py).

# Code Description
## Functions

1. def set_instructor(self, ctx, member:discord.Member):

This function is used to set a member as instructor. 

Inputs:

- self: used to access parameters passed to the class through the constructor
- ctx: used to access the values passed through the current context
- member: name of member to be made instructor 
         

Outputs: Bots response

# How to run it? (Small Example)
Enter: "$setInstructor user"
```
$setInstructor @user
```
Successful execution will set the member as an instuctor and repond with a bot message.

![image](https://user-images.githubusercontent.com/19858170/144727065-fef96f60-8417-4604-b133-2eeee26374fd.png)

