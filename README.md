<p align="center"><img width=100% src="https://github.com/Ashwinshankar98/ClassMateBot/blob/README-update/data/title.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5730692.svg)](https://doi.org/10.5281/zenodo.5730692)
[![Python application](https://github.com/Ashwinshankar98/ClassMateBot/actions/workflows/main.yml/badge.svg)](https://github.com/Ashwinshankar98/ClassMateBot/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Ashwinshankar98/ClassMateBot/branch/main/graph/badge.svg?token=6RRZ67UAA3)](https://codecov.io/gh/Ashwinshankar98/ClassMateBot)
<p align="center">
  <a href="#dart-basic-overview">Basic Overview</a>
  ::
  <a href="#orange_book-description">Description</a>
  ::
  <a href="#arrow_down-installation">Installation</a>
  ::
  <a href="#computer-commands">Commands</a>
  ::
  <a href="#earth_americas-future-scope">Future Scope</a>
  ::
  <a href="#pencil2-contributors">Contributors</a>
  
</p>

---

## :dart: Basic Overview

https://user-images.githubusercontent.com/60410421/140225894-5da3c56e-829f-4407-ba72-c0878081e388.mp4



This project helps to improve the life of students, TAs and teachers by automating many mundane tasks which are sometimes done manually. ClassMateBot is a discord bot made in Python and could be used for any discord channel. 

In Iteration 2, we added 6 main quality-of-life improvements to be more useful to admins (Professor and TA) and students alike.

---

## :orange_book: Description

There are three basic user groups in a ClassMateBot, which are Students, Professor and TAs. Some basic tasks for the bot for the students user group should be automating the task of group making for projects or homewroks, Projection deadline reminders, etc. For TAs it is taking up polls, or answering FAQs asked by the students. Our ClassMateBot focuses on the student side of the discord channel, i.e. currently it focuses on the problems faced by the students while using these discord channels.The user stories covered here would be more concerned about the activities for the channel for Software Engineering class in North Carolina State University for the Fall 2021 semester.

For Iteration 2, we aimed to expand the Bot's functionality so Professors and TAs can be more efficient and widened our scope outside of just our Software Engineering class. We researched how different classes in different programs (ex. Social Sciences, English, Humanities) could benefit from an improved bot. We believe our bot's commands like auto-grouping students, sending emails directly from discord to students, sentiment analysis, visualizing data/statistics, greatly benefits class management and information distribution. 

---

### Phase 1 Features
You can find the Features from Iteration 1 [here](./docs/Iteration1Features.md)
### Phase 2 Features
You can find the Features from Iteration 2 [here](./docs/Iteration2Features.md)

---
### Phase 3 Features

### 1. New channels and roles
  
We have introduced more channels for ease of communication. We have below channels created at the start of the bot,
- Instructor
- Q-and-A
- TA
- Course Calendar
 
We have introduced roles for better classification of the members and to restrict access for certain commands. We have added below roles,
- Instructor
- TA

### 2. Instructor commands

We have multiple commands to handle functionalities related to instructor roles. The instructor has access to the instructr cannel and we have restricted ceratin commands(like attendance) to be used only in the instructor channel.

### 3. TA commands

We have multiple commands to handle functionalities related to TA roles. The TAs will have access to the TA channel and similar to Instructors, they also have more access than other members to execute ceratin commands.

### 4. Direct Messaging

Direct messsaging commands allo people to dm privately to any other member of the guild. We also have a command to sned a reminder message or a broadcast message to all the memebrs of the guild privately.

### 5. Attendance

The instructors can check the attendees and absentees list using this command. This can be executed only in the instructors channel. This will also show them a districution cart with the present and absentees.

### 6. Profanity

This enables users to add a custom word to the profanity filter. These words will be added to the profanity filter and will be blocked from the messages.

### 7. Question and Answer

This functionality enables users to ask questions in the q-and-a channel. They can ask it as themselves, that is, the author name will be displayed next to the question, ot they can ask questions anonymously.  All the questions are auto-numbered for ease of tracking.

Members can also answer these questions. The role will be displayed next to the answer.

---

## :arrow_down: Installation

1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/chandur626/ClassMateBot.git
cd (into the ClassMateBot folder. If you type the commmand "ls", you should see the contents of the ClassMateBot folder)
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip install -r requirements.txt
```
3. Once the installation is complete with requirements installed, you have to generate a .env file and place it in the root of your project folder. The .env file contains your bot TOKEN and your Discord GUILD (guild is your discord server name). [Check out this video](https://youtu.be/nW8c7vT6Hl4?t=256) to see how you can setup your discord developer settings and .env file. You may also contact Niraj Lavani (nrlavani@ncsu.edu) for additional information on this process. 
```
PLEASE DO NOT SHARE THE TOKEN ONLINE, 
DO NOT UPLOAD TO GITHUB OR ELSE THE TOKEN WILL AUTOMATICALLY GET DESTROYED AND HAS TO BE REGENERATED.
```
4. Once all the requirements are installed, use the python command to run the ```bot.py``` file.
```
python3 bot.py 
```

---
## Version 3 Commands
Attendance

:open_file_folder: [$takeattendance command](./docs/Attendance/takeattendance.md)

Messaging

:open_file_folder: [$DM command](./docs/DM/Private_msg.md)

:open_file_folder: [$reminder command](./docs/DM/group_reminder.md)

Profanity

:open_file_folder: [$custom command](./docs/Profanity/profanity.md)

Question and Answers

:open_file_folder: [$ask command](./docs/Q%20and%20A/ask.md)

:open_file_folder: [$askanonym command](./docs/Q%20and%20A/ask_anonymous.md)

:open_file_folder: [$answer command](./docs/Q%20and%20A/answer.md)

New Role - Instructor

:open_file_folder: [$getInstructor command](./docs/Instructors/Get_Instructor.md)

:open_file_folder: [$setInstructor command](./docs/Instructors/Set_Instructor.md)

:open_file_folder: [$removeInstructor command](./docs/Instructors/Remove_Instructor.md.md)

New Role - TA

:open_file_folder: [$getTA command](./docs/TA/Get_TA.md)

:open_file_folder: [$setTA command](./docs/TA/Set_TA.md)

:open_file_folder: [$removeTA command](.docs/TA/Remove_TA.md)

## Version 2 Commands
Data Visualization

:open_file_folder: [$grades command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/grades.md)

:open_file_folder: [$attendance command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/attendance.md)

:open_file_folder: [$customchart command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/customchart.md)

:open_file_folder: [$checkgrade command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/checkgrade.md)

:open_file_folder: [$checkattendance command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/checkattendance.md)

:open_file_folder: [$checkchart command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/charts/checkchart.md)


User Ranking

:open_file_folder: [$levels command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/userRanking/level.md)

:open_file_folder: [$add_database command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/userRanking/add_database.md)


Email Specification

:open_file_folder: [$add_email_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/EmailSpecification/add_email.md)

:open_file_folder: [$view_email_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/EmailSpecification/view_email.md)

:open_file_folder: [$update_email command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/EmailSpecification/update_email.md)

:open_file_folder: [$delete_email_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/EmailSpecification/delete_email.md)


Auto-Grouping

:open_file_folder: [$auto-assign_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/auto-assign.md)

:open_file_folder: [$find-group_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/find-group.md)

:open_file_folder: [member remove event](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/member-remove.md)


Sentiment Analysis

:open_file_folder: [$sentiment_analysis_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/SentimentAnalysis/Sentiment.md)


Link Saving

:open_file_folder: [$send_links_command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/StoreLinks/Links.md)



## Original Commands
For the newComer.py file

:open_file_folder: [$verify command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Verification/verify.md)

For the voting.py file

:open_file_folder: [$projects command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Voting/projects.md)

:open_file_folder: [$vote command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Voting/vote.md)

For the deadline.py file

:open_file_folder: [$add_homework command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/add_homework.md)

:open_file_folder: [$change_reminder_due_date command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/change_reminder_due_date.md)

:open_file_folder: [$clear_all_reminders command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/clear_all_reminders.md)

:open_file_folder: [$course_due command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/course_due.md)

:open_file_folder: [$delete_reminder command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/delete_reminder.md)

:open_file_folder: [$due_this_week command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/due_this_week.md)

:open_file_folder: [$due_today command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/due_today.md)

:open_file_folder: [$list_reminders command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Reminders/list_reminders.md)

For the pinning.py file

:open_file_folder: [$pin command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/PinMessage/pin.md)

:open_file_folder: [$unpin command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/PinMessage/unpin.md)

:open_file_folder: [$pinnedmessages command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/PinMessage/pinnedmessages.md)

:open_file_folder: [$updatepin command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/PinMessage/updatepin.md)

For the groups.py file

:open_file_folder: [$group command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/group.md)

:open_file_folder: [$join command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/join.md)

:open_file_folder: [$remove command](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/docs/Groups/remove.md)


---

## :earth_americas: Future Scope
[Project 3](https://github.com/chandur626/ClassMateBot/projects/2) TODO tasks are located in the Projects tab. 

---

## :pencil2: Contributors
### Version 3
[Ashwin Shankar](https://github.com/Ashwinshankar98)

[Kailash Singaravelu](https://github.com/kailash1998s)

[Itha Aswin](https://github.com/ithaaswin)

[SaiKaushik](https://github.com/saikaushik1997)

[Shakthi Nandana Govindan](https://github.com/shakthinandana)

### Version 2 

[Chandrahas Reddy Mandapati](https://github.com/chandur626)

[Sri Pallavi Damuluri](https://github.com/SriPallaviDamuluri)

[Niraj Lavani](https://github.com/nirajlavani)

[Harini Bharata](https://github.com/HariniBharata)

[Sandesh Aladhalli Shivarudre Gowda](https://github.com/05sandesh)

### Version 1

[Chaitanya Patel](https://github.com/War-Keeper)

[Evan Brown](https://github.com/wevanbrown)

[Kunwar Vidhan](https://github.com/kunwarvidhan)

[Sunil Upare](https://github.com/sunil1511)

[Sumedh Salvi](https://github.com/salvisumedh2396)
