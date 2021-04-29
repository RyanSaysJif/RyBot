<img src="https://github.com/ASMRyan/RyBot/blob/1.1.1/icon/icon.png" align="right" alt="RyBot v1.1.1" title="Bot Icon" width="256" height="256" />

# RyBot - v1.1.1

A Python-based Discord bot built on an as-needed basis for Queercraft.

Licensed under [GNU GPLv3](https://github.com/ASMRyan/RyBot/blob/1.1.1/LICENSE).

## Table of Contents
1. [General Info](#general-info)
2. [Thanks](#thanks)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Collaboration](#collaboration)
***
### General Info

This project is a Python-based Discord bot originally designed for custom use cases for Queercraft. Its original purpose is to be able to delete all messages in a specific channel from users who are no longer members of the Discord server. 

This bot requires the following permissions when invited:
* View Channels
* Manage Messages
* View Message History

Default Command Prefix: `.rybot`

Current Functions:
* `omnomnom`: **O**ld **M**essages **N**ow **O**bsolete **M**eaning **N**o **O**vert **M**ass - Deletes all messages in the channel sent by users no longer in the Discord server. Only works in the channel specified in the code file.
* `leave`: Kick the bot to the curb.
***
### Thanks
A big thank you to [aphymi](https://github.com/aphymi) for reviewing the pre-release code!
***
### Technologies

Built in Python 3.8.5
***
### Installation

Downloading this software for personal use assumes the user already has a working knowledge of, or can figure out on their own, how to use Discord, create a Discord bot on the developer portal, and run a Python script.
1. In the same directory as the RyBot.py file, create a file called BotToken.txt. In it, paste the bot token for the bot you created to use this on your server and save.
2. In RyBot.py, replace the constants at the beginning with the appropriate user and channel ID's for your server, and save the changes. The code is commented to help you out.
3. Run RyBot.py and invite it to join your server using your bot's invite URL. Be sure to include `&permissions=74752` at the end of the invite URL to ensure the bot is given the necessary permissions.
***
### Collaboration

This project is not seeking collaborators at this time.
