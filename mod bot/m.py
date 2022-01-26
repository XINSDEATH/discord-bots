import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "urprefix")

token = 'urtoken'

@client.command(aliases=['c','clear'])
@commands.has_role("admin")
async def purge(ctx, amount=11):
    amount = amount+1
    if amount > 1000000000001:
        await ctx.send('above limit')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('cleared messages')
    

@client.command(aliases=['k','kickk'])
@commands.has_role("admin")
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.channel.send(member.name+"has been kicked for the reason of"+reason)
    await member.kick(reason=reason)


@client.command(aliases=['b','bann'])
@commands.has_role("admin")
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.channel.send(member.name+"has been banned for the reason of"+reason)
    await member.ban(reason=reason)


@client.command(aliases=['ub','unbann'])
@commands.has_role("admin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users: 
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.name}#{user.mention}')
            return 


@client.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send('please write a reason')
        return
    guild = ctx.Guild
    muteRole = discord.utiles.get(guild.roles, name = "Muted")

    if not muteRole:
        await ctx.send("No mute role found creating one now...")
        muteROle = await guild.create_role(name = "Muted")

        for channel in guild.channels:
            await channel.set_premissions(muteRole, speak=False, send_messages=False, read_messages=True, read_message_history=True)
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f"{member.mention} has been muted in {ctx.guild} | reason: {reason}")
        await member.send(f"you have been muted in {ctx.guild} | reason: {reason}")


@client.command()
async def unmute(ctx, member: discord.Member, *, reason=None):

    guild = ctx.Guild
    muteRole = discord.utils.get(guild.roles, name = "Muted")

    if not muteRole:
        await ctx.send("the Mute role can\'t be found please check if there is a mute role or if the user already has it")
        return
    await member.remove_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} has been unmuted in {ctx.guild}")
    await member.send(f"you have been unmuted in {ctx.guild}")


@client.event
async def on_ready():
    print("ready")



client.run(token)