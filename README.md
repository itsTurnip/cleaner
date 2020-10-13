# Cleaner discord bot

Simple discord bot for cleaning chat from users' and bot command messages.

Host it yourself with docker:

```console
docker build -t cleaner .
docker run -d -e TOKEN={bot token} cleaner
```

## Command list

* `^!clean user @user#tag` - cleans all the messages sent by specified user
* `^!clean starts !` - cleans all the messages that starts with specified symbol

All of the commands that are to be executed needs the bot to have read message history and manage messages permissions to be set to true
