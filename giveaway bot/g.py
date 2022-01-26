import discord
from discord.ext import commands
import asyncio
import random
import time

client = commands.Bot(command_prefix = "urprefix")

token = 'urtoken'




@client.command()
@commands.has_role("Giveaway Host")
async def gcreate(ctx, time=None, *, prize=None):
    if time == None:
        return await ctx.send('please include a time')
    elif prize == None:
        return await ctx.send('please include a prize')
    embed = discord.Embed(title='New Giveaway!', description=f'{ctx.author.mention} is giving away **{prize}**!!')
    time_convert = {"s":1, "m":60, "h":3600, "d": 86000}
    gawtime = int(time[0]) * time_convert[time[-1]]
    embed.set_footer(text=f'Giveaway ends in {time}')
    gaw_msg = await ctx.send(embed = embed)

    await gaw_msg.add_reaction("🎉")
    await asyncio.sleep(gawtime)

    new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"YAY! THE WINNER IS {winner.mention} has won the giveaway for **{prize}**!!!")

@client.event
async def on_ready():
    print("ready")



client.run(token)
