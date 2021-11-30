## Features from Iteration 2

### 1 - Auto-Grouping Students

Auto-Grouping command allows TAs and Professors to automatically assign students into groups for project works. The Iteration 1 provided join command which can be used by students to join a specific group. Post deadline, If students have not yet joined a group, then the TA can simply use the auto-grouping command to assign those students into groups having vacant positions. Groups with maximum vacant positions are given the first priority. A simple example is shown below :


![$auto-assign](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Auto-grouping.gif)


### 2 - Email Functionality
Students can now configure their email address to receive attachments and various notifications such as reminders. Students can create or update the configured email address using the below-mentioned commands in the Version 2 commands section.

<p align="left"><img width=75% src="https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Email_Address.gif"></p>

Students can also get the attachments mailed to their configured email address by reacting with white_heavy_mark to the attachment message.

<p align="left"><img width=75% src="https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Email_Attachment.gif"></p>

### 3 - Sentiment Analysis 
Students can analyze the sentiment of the message. This will give the sentiment and the polarity score of the message. 

Students can analyze the sentiment using the below comments. 

<p align="left"><img width=75% src="https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/SentimentAnalysis.gif"></p>


### 4 - Data Visualization

Admins (In this case, TAs and Professors) can quickly make graphcs and charts directly in discord to share with students/users. Admins can use this feature to share grade distributions, lecture participation/attendance, or other course statistics. Pre-existing graph commands (such as grades or attendance) were made for ease-of-use so there are less command arguments for the admin to type. If the admin requires a custom chart, a command exists to do just that where admins can specify all data labels and information. All charts are named and stored into a json file when they are created. Students have acess to a command that allows them to view previously presented charts. 
<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969198-dcd79af8-eb59-4fa7-934b-aca7023574a0.gif"></p>

### 5 - Link Collection

Another problem that the students face is that they cannot save all the messages which contain important URLs that are helpful to them so we have built a user command where a student can retrieve all the links which are shared in the group with one click. This command lets users access all messages which contain URLs. The messages Containing URL are automatically get appended in a file and the file is attached when the `$send_links` command is input.

<p align="left"><img width=75% src="https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Links.gif"></p>

### 6 - User Participation Ranking

Users are all given a participation rank the moment they join a discord community with the ClassMateBot. As the user participates in the server, such as replying to the professor, answering questions, helping other students, etc., they increase their participation score. Courses within the Humanities and Social Sciences rely on student participation. Professors can use this feature to check which students are participating more and factor that into a class participation grade. Users can also check which level/rank they hold. Admins also have the ability to add/remove points from users.
<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969309-90b590b4-fe72-45ca-9956-b65bbf6db7b9.gif"></p>
