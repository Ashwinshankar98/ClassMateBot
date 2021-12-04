# About $remindme
This command lets the user set a personal reminder. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](../../cogs/deadline.py).

# Code Description
## Functions
                
1. def remindme(self, ctx, quantity: int, time_unit: str, *, text: str)
This function takes as arguments the values provided by the constructor through self and the context in which the command was called. 
   
Inputs:
- ctx: used to access the values passed through the current context.
- quantity: time after which the reminder will be sent  
- time_unit: unit of the quantity
- text: Reminder text

Output:
Bot response 

# How to run it? (Small Example)
Enter Space separated: "$remindme quantity time_unit "reminder text" "

```
$remindme 5 seconds "Submit the project"
```
Successful execution of this command will display bot message and after the given time, will send a reminder.

![remindme](https://user-images.githubusercontent.com/19858170/144727638-2d0091b7-fa68-4a47-9b26-e6e732c15d9d.gif)
