import pyautogui
from datetime import datetime

import discord
from discord.ext import commands
import asyncio

chat=("Channel ID")#insert Channel IDs where you want to run the command Here
run=0
tag=0
direction={'i':'up','j':'left','k':'down','l':'right'}

intent = discord.Intents.all()
intent.members = True
intent.typing = True
intent.presences = True

#intent = discord.Intents(guilds=True, members=True, messages=True)
client = commands.Bot(command_prefix=('O','o'),
                      case_insensitive=True,
                      intents=intent,
                      allowed_mentions=discord.AllowedMentions(
                          everyone=False,
                          users=True,
                          roles=True,
                          replied_user=True))
def logchat(key,msg):
    print(f"{datetime.now().strftime('%H:%M:%S')}: [#{msg.channel.name}]: {msg.author}: {key}")
    f=open("log.txt",'a',encoding="utf-8")
    f.write(f"{datetime.now()}: [#{msg.channel.name}]: {msg.author.id} ({msg.author}): {key}\n")
    f.close()
    f=open("chat.txt",'a',encoding="utf-8")
    f.write(f" {key}: {msg.author}\n")
    f.close()

def logchatmulti(msg,i):
    print(f"{datetime.now().strftime('%H:%M:%S')}: [#{msg.channel.name}]: {msg.author}: {''.join([(direction[i] if i in direction else i).upper()+' ' for i in msg.content])}{'' if i==0 else f'[{i+1}]'}")
    f=open("log.txt",'a',encoding="utf-8")
    f.write(f"{datetime.now()}: [#{msg.channel.name}]: {msg.author.id} ({msg.author}): {''.join([(direction[i] if i in direction else i).upper()+' ' for i in msg.content])}{'' if i==0 else f'[{i+1}]'}\n")
    f.close()
    f=open("chat.txt",'a',encoding="utf-8")
    f.write(''.join([f' {msg.author}: {(direction[i] if i in direction else i).upper()}\n' for i in msg.content]))
    f.close()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    client.ochannel=client.get_channel(chat)

@client.event
async def on_message(msg):
    global run,tag,direction
    if msg.channel.id in chat and len(msg.content)<=10 and msg.content[0]!='=' and not msg.author.bot:

        msg.content=msg.content.lower()
        if msg.content in ('left','right','up','down'):
            pyautogui.keyDown(msg.content)
            pyautogui.keyUp(msg.content)
            logchat(msg.content.upper(),msg)
        elif msg.content == 'ok':
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')
            logchat(msg.content.upper(),msg) 
        elif msg.content in ("run","shift"):
            run= not run
            if run:
                pyautogui.keyDown("shift")
            else:
                pyautogui.keyUp("shift")
            logchat("SHIFT",msg)

        else:
            flag=1
            for i in range(len(msg.content)):
                if not msg.content[i] in ('q','w','a','z','x','i','j','k','l'):
                    flag=0
            if flag:
                logchatmulti(msg,i)
                for i in range(len(msg.content)):
                    if msg.content[i] in ('q','w','z','x'):
                        pyautogui.keyDown(msg.content[i])
                        pyautogui.keyUp(msg.content[i])
                    
                    if msg.content[i] in direction.keys():
                        pyautogui.keyDown(direction[msg.content[i]])
                        pyautogui.keyUp(direction[msg.content[i]])
                        
                    if msg.content[i] in ("a","a"):
                        tag= not tag
                        if tag:
                            pyautogui.keyDown('a')
                        else:
                            pyautogui.keyUp('a')

        await client.process_commands(msg)

@client.event
async def Ping(self, ctx):
        await ctx.send(f'Pong! `{round(self.client.latency * 1000)}ms`')

token = "Insert-Bot-Token-Here"
client.run(token)
