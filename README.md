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


### Now Running the bot locally
run:
```bash
pipenv run fakah
```

```bash
pipenv run fakah                                                                                            
Loading .env environment variables...
[2019-07-28 13:12:52][INFO] [fakah.fakah_bot.main:50] LONG LIVE Fakah
[2019-07-28 13:12:52][DEBUG] [asyncio.__init__:54] Using selector: EpollSelector
[2019-07-28 13:12:52][INFO] [fakah.lib.plugin.load:20] Loaded extension: fakah.lib.plugins.fakahchannels
[2019-07-28 13:12:52][INFO] [fakah.lib.plugin.load:20] Loaded extension: fakah.lib.plugins.server
[2019-07-28 13:12:52][INFO] [discord.client.login:399] logging in using static token
[2019-07-28 13:12:53][INFO] [discord.gateway.from_client:241] Created websocket connected to wss://gateway.discord.gg?encoding=json&v=6&compress=zlib-stream
[2019-07-28 13:12:53][INFO] [discord.gateway.identify:320] Shard ID 0 has sent the IDENTIFY payload.
[2019-07-28 13:12:53][INFO] [discord.gateway.received_message:411] Shard ID 0 has connected to Gateway: ["gateway-prd-main-b811",{"micros":44430,"calls":["discord-sessions-prd-1-23",{"micros":42254,"calls":["start_session",{"micros":40905,"calls":["api-prd-main-m834",{"micros":36215,"calls":["get_user",{"micros":3243},"add_authorized_ip",{"micros":6},"get_guilds",{"micros":6617},"coros_wait",{"micros":0}]}]},"guilds_connect",{"micros":2,"calls":[]},"presence_connect",{"micros":2,"calls":[]}]}]}] (Session ID: 700d602acb2d6d15a2b9cbc73acd7b10).
[2019-07-28 13:12:57][INFO] [discord.state.parse_guild_members_chunk:796] Processed a chunk for 998 members in guild ID 249693478424936458.
[2019-07-28 13:12:57][INFO] [fakah.lib.plugins.fakahchannels.on_ready:41] Starting Voice Channel purger loop
[2019-07-28 13:12:57][INFO] [fakah.lib.plugins.server.on_ready:20] Logged in as Fakah
[2019-07-28 13:12:57][INFO] [fakah.lib.plugins.fakahchannels.purge_unused_vc:24] Purged 0 Channels this loop
[2019-07-28 13:12:57][INFO] [fakah.lib.utils.list_servers:87] Current servers: ['Tamago', '24/7 Gaming Community']
```


## Okay I got it running so?
Either fix things or change things you want. This runs on the discordpy API documentation [here](https://discordpy.readthedocs.io/en/latest/index.html)
If you want to fix things or just improve it go ahead and submit PRs against the repo, I will welcome any changes!
