from tok import getTok

import discord
import time
import logging


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print("member join")
    role = discord.utils.get(member.server.roles, id="844532858118733824")
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.channel.id == '844558702103232563':
        print("meember msg")
        role = discord.utils.get(message.author.server.roles, id="844532858118733824")
        if role in message.author.roles:
            print("adding guest")
            role2 = discord.utils.get(message.author.server.roles, id="844574498975514624")
            await client.remove_roles(message.author, role)
            await client.add_roles(message.author, role2)


@client.event
async def on_reaction_add(reaction, user):
    print("Added reaction")
    if reaction.message.id == "846001584516104292":
        umbrage = discord.utils.get(user.server.roles, id="843479518357880842")
        if reaction.emoji == "🍰":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="843555520295469067")
                await client.add_roles(user, role)
        elif reaction.emoji == "🦑":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947787673206794")
                await client.add_roles(user, role)
        elif reaction.emoji == "🦁":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947449540739092")
                await client.add_roles(user, role)
        elif reaction.emoji == "🔪":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947863807688716")
                await client.add_roles(user, role)
        elif reaction.emoji == "👻":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947323845836840")
                await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    print("reaction remove")
    if reaction.message.id == "846001584516104292":
        umbrage = discord.utils.get(user.server.roles, id="843479518357880842")
        if reaction.emoji == "🍰":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="843555520295469067")
                if role in user.roles:
                    await client.remove_roles(user, role)
        elif reaction.emoji == "🦑":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947787673206794")
                if role in user.roles:
                        await client.remove_roles(user, role)
        elif reaction.emoji == "🦁":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947449540739092")
                if role in user.roles:
                    await client.remove_roles(user, role)
        elif reaction.emoji == "🔪":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947863807688716")
                if role in user.roles:
                    await client.remove_roles(user, role)
        elif reaction.emoji == "👻":
            if umbrage in user.roles:
                role = discord.utils.get(user.server.roles, id="845947323845836840")
                if role in user.roles:
                    await client.remove_roles(user, role)




client.run(getTok())
