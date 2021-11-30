# About $removeTA
This command is used to remove a member from TA list.

# Location of Code
The code that implements the above mentioned functionality is located [here](../../cogs/ta.py).

# Code Description
## Functions

1. def remove_ta(self, ctx, member:discord.Member):
   
   This function removes a member from TA position.

Inputs:

- self: used to access parameters passed to the class through the constructor
- ctx: used to access the values passed through the current context
- member: name of member to be removed from TA

Outputs: Bots response

   
# How to run it? (Small Example)
Enter : "$removeTA name"
```
$removeTA name
```
Successful execution will remove the member from the TA list.

![removeTA](./removeTA.png)
