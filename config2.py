import asyncio
from discord.ext import commands

client = commands.Bot(description="IDK", command_prefix=commands.when_mentioned_or('$'),)

event = asyncio.Event()

tableflip_filter = 0

dont_fucking_do_the_fucking_ban_reason_thingy = 0

dont_fucking_do_the_fucking_kick_reason_thingy = 0

toggle_logs = 0

def toggle_next():
    client.loop.call_soon_threadsafe(event.set)
