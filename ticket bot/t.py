import discord
from discord.ext import commands
import discord
import asyncio
import datetime
client = commands.Bot(command_prefix = "$")
client.ticket_configs = {}

token = "OTI4MTg5NzkyMTc5NjE3Nzkz.YdVKGw.Xx7eV4t88mr6Ny0iRtFzKx1AXfA"


@client.command() 
async def new(ctx):
    await ctx.author.send("making ticket now!")
    categ=discord.utils.get(ctx.guild.categories,name="OPENED TICKETS") 
    for ch in categ.channels: 
        if ch.topic==str(ctx.author.id): 
            return await ch.send(f"{ctx.author.mention}! You already have a ticket here!")
    r1=ctx.guild.get_role(role id)
    overwrite={
        ctx.guild.default_role:discord.PermissionOverwrite(read_messages=False),
        ctx.me:discord.PermissionOverwrite(read_messages=True),
        ctx.author:discord.PermissionOverwrite(read_messages=True),
        r1:discord.PermissionOverwrite(read_messages=True)
        } 
    channel=await categ.create_text_channel(name=f"channel-name",overwrites=overwrite,topic=f"{ctx.author.id}") 
    em=discord.Embed(title="Ticket created!",
                        description=f"description",
                        color=discord.Color.random())

    await asyncio.sleep(3)
    await channel.send(f"ticket created by {ctx.author.mention}")
    await channel.send(embed=em),
    await ctx.author.send(f"{ctx.author.mention} ur ticket has been made! - click here {channel.mention}")
    


@client.event
async def on_ready():
    print("ready")

client.run(token)