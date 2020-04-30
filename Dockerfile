FROM python:3.8.2-buster

RUN mkdir -p /opt/discord-bot/
WORKDIR /opt/discord-bot/

COPY . .
RUN ls -ltra

RUN pip install discord.py
RUN pip install python-dotenv

CMD ["python", "-u", "./bot.py"]
