# AkagiBot

Updated for 2023 with new slash commands, using [nextcord](https://github.com/nextcord/nextcord) for the API.

## Prerequisites:
* [Python 3.10+](https://www.python.org/)
* [nextcord](https://pypi.org/project/nextcord/)

## Initialization

* You can install the required packages by running `python3 -m pip install -r requirements.txt`
* Then, create a directory named `keys`.
* Create `discord.txt` and `serverids.txt` inside the `keys` directory.
* Put your discord bot API key into `discord.txt`
* Put the Ids of the servers you would like to allow the bot to be used on in `serverids.txt` on each line.

## Features Implemented

* Role reaction monitor abilities.

## Code Structure

* `main.py` is the main "executable". It creates a cogs list to use the modules in `cogs/`.
* `utils.py` is for json loading and saving utils.
* `apikeys.py` is for loading api keys and server Ids.
* cog modules explained below.

## Admin.py

* For admin commands, such as `/botsay`.
* Full role monitoring and adding role monitors.
* Only users with the "Board" role can use these commands.

## General.py

* For general public use functions such as retrieval of commonly used links.