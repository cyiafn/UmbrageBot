import os

import discord
import datetime
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.reactions = True

startingTime = datetime.datetime.now()

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
        elif message.author.id == 132420435294814208 and message.content == "/ping":
            global startingTime
            diff = datetime.datetime.now() - startingTime
            diffInS = diff.total_seconds()

            days = divmod(diffInS, 86400)
            hours = divmod(days[1], 3600)
            minutes = divmod(hours[1], 60)
            seconds = divmod(minutes[1], 1)
            
            await message.channel.send(content=("Hello Cira. Current uptime = " + "%d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0])))

    async def on_raw_reaction_add(self, RawReactionActionEvent):
        
        usr = RawReactionActionEvent.member
        emo = RawReactionActionEvent.emoji.name
        msg = RawReactionActionEvent.message_id
        if msg == 863709395334332436:
            print("reaction added")
            umbrage = discord.utils.get(usr.guild.roles, id=843479518357880842)
            if emo == "🍰": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=843555520295469067)
                await usr.add_roles(role)
            elif emo == "🦑": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=845947787673206794)
                await usr.add_roles(role)
            elif emo == "🦁": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=845947449540739092)
                await usr.add_roles(role)
            elif emo == "👻": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=845947323845836840)
                await usr.add_roles(role)
            elif emo == "🦸‍♂️": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961319304626207)
                await usr.add_roles(role)
            elif emo == "🪙": #ok
                #if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961378204188693)
                await usr.add_roles(role)
            elif emo == "🎟️": #ok
               # if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961404850602024)
                await usr.add_roles(role)
            elif emo == "🕐": #ok
               # if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961428406861876)
                await usr.add_roles(role)
            elif emo == "💸":# ok
              #  if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961456403447869)
                await usr.add_roles(role)
            elif emo == "👁️":# ok
               # if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961488207675412)
                await usr.add_roles(role)
            elif emo == "🌥️":
               # if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961512732688426)
                await usr.add_roles(role)
            elif emo == "⛅":
               # if umbrage in usr.roles:
                role = discord.utils.get(usr.guild.roles, id=854961535616417792)
                await usr.add_roles(role)
            elif emo =="flemmagachi":
               # if umbrage in usr.roles:
                print("here")
                role = discord.utils.get(usr.guild.roles, id=854961555648806932)
                await usr.add_roles(role)
            elif emo=="🌓":
                role = discord.utils.get(usr.guild.roles, id=863511341302415370)
                await usr.add_roles(role)
            elif emo=="🌕":
                role = discord.utils.get(usr.guild.roles, id=849172336426483730)
                await usr.add_roles(role)

    async def on_raw_reaction_remove(self, RawReactionActionEvent):
        
        usr = RawReactionActionEvent.user_id
        emo = RawReactionActionEvent.emoji.name
        msg = RawReactionActionEvent.message_id
        guild = self.get_guild(RawReactionActionEvent.guild_id)
        usr = guild.get_member(usr)
        if msg == 863709395334332436:
            print("reaction removed")
            umbrage = discord.utils.get(guild.roles, id=843479518357880842)
            if emo == "🍰":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=843555520295469067)
                await usr.remove_roles(role)
            elif emo == "🦑":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=845947787673206794)
                await usr.remove_roles(role)
            elif emo == "🦁":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=845947449540739092)
                await usr.remove_roles(role)
            elif emo == "👻":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=845947323845836840)
                await usr.remove_roles(role)
            elif emo == "🦸‍♂️":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961319304626207)
                await usr.remove_roles(role)
            elif emo == "🪙":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961378204188693)
                await usr.remove_roles(role)
            elif emo == "🎟️":
               # if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961404850602024)
                await usr.remove_roles(role)
            elif emo == "🕐":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961428406861876)
                await usr.remove_roles(role)
            elif emo == "💸":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961456403447869)
                await usr.remove_roles(role)
            elif emo == "👁️":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961488207675412)
                await usr.remove_roles(role)
            elif emo == "🌥️":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961512732688426)
                await usr.remove_roles(role)
            elif emo == "⛅":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961535616417792)
                await usr.remove_roles(role)
            elif emo =="flemmagachi":
                #if umbrage in usr.roles:
                role = discord.utils.get(guild.roles, id=854961555648806932)
                await usr.remove_roles(role)
            elif emo=="🌓":
                role = discord.utils.get(guild.roles, id=863511341302415370)
                await usr.remove_roles(role)
            elif emo=="🌕":
                role = discord.utils.get(guild.roles, id=849172336426483730)
                await usr.remove_roles(role)

client = MyClient(intents =intents)
client.run("ODQ1OTk3MDUzNTIzMjYzNTE4.YKpGJw.XEtLx5QjZyuVTivVC4CSuZ0CeT8")
#client.run(os.getenv('SECRET_TOKEN'))
