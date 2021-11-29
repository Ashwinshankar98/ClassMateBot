# About $dm
This command sends a DM to a specific person in the guild.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/cogs/dm.py).

# Code Description
## Functions

1. def dm(self, ctx,user:discord.User,*,message=None):

This function sends dm to the specified person in the guild. 

Inputs:

        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - recipient name 
        - content 

Outputs: Bots response

# How to run it? (Small Example)
Enter space-separated: "$DM user hello"
```
$DM 
```
Successful execution will show a attendance distribution chart

![Private_msg](./Private_msg.png)
