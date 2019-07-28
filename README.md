# Fakah Bot


## How to develop?

The makefile is your friend, but have a few perquisites you will need to cover first.
You will need pipenv, make, gcc (linux) for compiling fun. This readme will not go
over all this, but should be straight forward. Some info about [pipenv](https://realpython.com/pipenv-guide/#pipenv-introduction)



### Running commands

#### make init
does the base install of the source package through pipenv that should already be installed,
if a local pipenv isn't yet setup this is when it will happen (python 3.6.8)

#### make check
Designed to do linting and pipenv checking for dependencies and such

#### make test
This is designed to install fakahbot package and testing packages if I ever decided to write tests for it :shrug:

#### make dist
Makes is dist package for system built on.

#### make live
This run only on image builds in my CI/CD pipeline just install the package in the image and pushes into image repo.


### After installing fakah-bot what do?

You will need to copy example.env to .env and update the value inside

| ENV Variable | Description | Required | Default |
| :----------- | :---------: | -------: | :-----: |
| `APP_ID`     | APP ID of your discordapp | NO | N/A |
| `TOKEN`      | Token for your bots api access to discord | YES | N/A |
| `BLOCKED_USERS` | Blocked UID's of users | NO | N/A |
| `GAMES`      | Comma delimited list of games your bot is playing | NO | N/A |
| `VOICE_CHANNEL_PREFIX` | The prefix the voice channels the bot manages | NO | "!F " |



## Okay I got it running so?
Either fix things or change things you want. This runs on the discordpy API documentation [here](https://discordpy.readthedocs.io/en/latest/index.html)
If you want to fix things or just improve it go ahead and submit PRs against the repo, I will welcome any changes!
