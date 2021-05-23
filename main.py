import os

import discord
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.reactions = True

class MyClient(discord.Client):

    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_member_join(self, member):
        print("member join")
        role = discord.utils.get(member.guild.roles, id=844532858118733824)
        await member.add_roles(role)

    async def on_message(self,message):
        if message.channel.id == 844558702103232563:
            print("guild app")
            role = discord.utils.get(message.author.guild.roles, id=844532858118733824)
            if role in message.author.roles:
                print("adding wait list")
                role2 = discord.utils.get(message.author.guild.roles, id=844574498975514624)
                await message.author.remove_roles(role)
                await message.author.add_roles(role2)

    async def on_raw_reaction_add(self, RawReactionActionEvent):
        
        usr = RawReactionActionEvent.member
        emo = RawReactionActionEvent.emoji.name
        msg = RawReactionActionEvent.message_id
        if msg == 846001584516104292:
            print("reaction added")
            umbrage = discord.utils.get(usr.guild.roles, id=843479518357880842)
            if emo == "🍰":
                if umbrage in usr.roles:
                    role = discord.utils.get(usr.guild.roles, id=843555520295469067)
                    await usr.add_roles(role)
            elif emo == "🦑":
                if umbrage in usr.roles:
                    role = discord.utils.get(usr.guild.roles, id=845947787673206794)
                    await usr.add_roles(role)
            elif emo == "🦁":
                if umbrage in usr.roles:
                    role = discord.utils.get(usr.guild.roles, id=845947449540739092)
                    await usr.add_roles(role)
            elif emo == "🔪":
                if umbrage in usr.roles:
                    role = discord.utils.get(usr.guild.roles, id=845947863807688716)
                    await usr.add_roles(role)
            elif emo == "👻":
                if umbrage in usr.roles:
                    role = discord.utils.get(usr.guild.roles, id=845947323845836840)
                    await usr.add_roles(role)

    async def on_raw_reaction_remove(self, RawReactionActionEvent):
        
        usr = RawReactionActionEvent.user_id
        emo = RawReactionActionEvent.emoji.name
        msg = RawReactionActionEvent.message_id
        guild = self.get_guild(RawReactionActionEvent.guild_id)
        usr = guild.get_member(usr)
        if msg == 846001584516104292:
            print("reaction removed")
            umbrage = discord.utils.get(guild.roles, id=843479518357880842)
            if emo == "🍰":
                if umbrage in usr.roles:
                    role = discord.utils.get(guild.roles, id=843555520295469067)
                    await usr.remove_roles(role)
            elif emo == "🦑":
                if umbrage in usr.roles:
                    role = discord.utils.get(guild.roles, id=845947787673206794)
                    await usr.remove_roles(role)
            elif emo == "🦁":
                if umbrage in usr.roles:
                    role = discord.utils.get(guild.roles, id=845947449540739092)
                    await usr.remove_roles(role)
            elif emo == "🔪":
                if umbrage in usr.roles:
                    role = discord.utils.get(guild.roles, id=845947863807688716)
                    await usr.remove_roles(role)
            elif emo == "👻":
                if umbrage in usr.roles:
                    role = discord.utils.get(guild.roles, id=845947323845836840)
                    await usr.remove_roles(role)


client = MyClient(intents =intents)
client.run(os.getenv('SECRET_TOKEN'))
