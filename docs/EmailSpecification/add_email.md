# About $add_email
This command lets the users along with TA and professor to configure an email address to receive attachments and notifications.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/chandur626/ClassMateBot/blob/main/cogs/email_address_spec.py).

# Code Description
## Functions
1. def add_email_address(self, ctx, email_address: str) <br>
This function accepts the email address provided by the user and verifies the email address to ensure the correct email address is provided. Configures the email address once it turns out to be valid and returns a success message.



# How to run it?
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'add_email' pass in all the parameters as a space seperated inputs in the following order:
(email_address)
```
$add_email email_address
$add_email noreplyclassmatebot@example.com
```
Successful execution of this command will configure the email address.
<p align="left"><img width=75% src="https://github.com/chandur626/ClassMateBot/blob/main/data/media/Email_Address.gif"></p>