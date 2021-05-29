import discord
from discord.ext import commands
from discord.ext.commands import Context
import re
from datetime import datetime, timedelta


bot = commands.Bot(command_prefix="^!")


@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


@bot.group()
@commands.has_permissions(manage_messages=True)
async def clean(ctx: Context):
    if ctx.invoked_subcommand is None:
        await ctx.send_help(clean)
    await ctx.message.delete()

@clean.command(description="Deletes latest messages", brief="Deletes latest messages")
@commands.bot_has_permissions(manage_messages=True, read_message_history=True)
async def last(ctx: Context, count: int=25):
    await cleaner(ctx, lambda x: True, count)

@clean.command(description="Deletes mentioned user's messages", brief="Deletes mentioned user's messages")
@commands.bot_has_permissions(manage_messages=True, read_message_history=True)
async def user(ctx: Context, target: discord.Member, count: int=25):
    await cleaner(ctx, lambda x: x.author.id == target.id, count)

@clean.command(description="Deletes messages that start with specified symbols", brief="Deletes messages that start with specified symbols")
@commands.bot_has_permissions(manage_messages=True, read_message_history=True)
async def starts(ctx: Context, start: str, count: int=25):
    await cleaner(ctx, lambda x: x.clean_content.startswith(start), count)

async def cleaner(ctx: Context, predicate: callable, count: int):
    if count > 100:
        await ctx.send("Count cannot be larger than 100")
        return
    date = datetime.today() - timedelta(days=14)
    channel: discord.TextChannel = ctx.channel
    remove_messages = list()
    async for message in channel.history(after=date, oldest_first=False).filter(predicate):
        remove_messages.append(message)
        if len(remove_messages) >= count:
            break
    if len(remove_messages) > 0:
        await channel.delete_messages(remove_messages)
        await ctx.send("Done", delete_after=5)
    else:
        await ctx.send("Did not find any messages to delete.\nI can't delete messages older than 14 days.", delete_after=7)
