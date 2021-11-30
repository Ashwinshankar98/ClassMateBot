# About $ban
This command is used by the bot to Ban spammers.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/banUsers.py).

# Code Description
## Functions

1. def ban(ctx,member:discord.Member,*,reason=None):
   
   This function bans a member from the guild.

Inputs:

- ctx: used to access the values passed through the current context
- member: name of the member
- reason: reason for ban

Outputs: Bots response

   
# How to run it? (Small Example)
Enter : "$ban name"
```
$Ban name
```
Successful execution will ban the member.

![ban](./ban.png)
