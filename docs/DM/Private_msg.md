# About $DM
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
$DM @username hello
```
Successful execution will send a dm to the person from bot with sender info.

![image](https://user-images.githubusercontent.com/19858170/144726748-ec021e60-0e30-4c69-bd2d-72710b91ba31.png)
![image](https://user-images.githubusercontent.com/19858170/144726784-c36e0a87-9836-41b8-91dd-2dfd4b776c89.png)


