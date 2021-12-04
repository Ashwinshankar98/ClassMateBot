# About $unban
This command is used by the bot to unban a banned member.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/banUsers.py).

# Code Description
## Functions

1. def ban(ctx,member:discord.Member,*,reason=None):
   
   This function unbans a banned member.

Inputs:

- ctx: used to access the values passed through the current context
- member: name of the member

Outputs: Bots response

   
# How to run it? (Small Example)
Enter : "$unban name"
```
$unban @user
```
Successful execution will unban the member.

![image](https://user-images.githubusercontent.com/19858170/144727322-b495f1a7-9785-4535-b1f2-16fbd6c41eb6.png)
