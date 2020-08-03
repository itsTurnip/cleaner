if __name__ == "__main__":
    from bot import bot
    from os import environ

    TOKEN = environ.get("TOKEN")

    bot.run(TOKEN)