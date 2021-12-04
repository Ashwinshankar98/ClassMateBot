# About $start_reminders
This command lets the user start the email reminder notification service for subscribed users.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/deadline.py).

# Code Description
## Functions
1. start_reminders(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'start_reminders' with no parameters:

```
$start_reminders
```
Successful execution of this command will start the email reminder notification service. 
It checks if there are any upcoming events, once every 6 hours, and notifies the students via email. 

![$start_reminders](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/listreminders.gif)
