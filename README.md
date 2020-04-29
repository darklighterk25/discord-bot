# Discord Bot

## Env variables
```
export DISCORD_CHANNEL={bot-token}
export DISCORD_GUILD={server-id}
export DISCORD_TOKEN={channel-id}
```

## Docker
Build image:
```bash
docker build -t discord-bot .
```
Init swarm:
```bash
docker stack deploy -c discord-bot.yml discord
```
