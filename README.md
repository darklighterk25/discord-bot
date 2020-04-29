# Discord Bot

## Environment variables
Create a `.env` file with the following variables:
```
DISCORD_CHANNEL={channel-id}
DISCORD_GUILD={server-id}
DISCORD_TOKEN={bot-token}
```

## Docker
Build image:
```bash
docker build -t discord-bot .
```
Docker Compose:
```bash
docker stack deploy -c discord-bot.yml discord
```
