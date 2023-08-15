

TOKEN = ''
guild_id =  0 # Mesajı göndereceğiniz sunucunun ID'si
channel_id = 0  # Mesajı göndereceğiniz kanalın ID'si
server_name = "Hane Gaming"
server_logo = ""
max_count = 0
try:
    with open("settings.txt", 'r') as file:
        for v in file:
            v = v.replace("\n", "")
            data = v.split(",")
            if data[0] == "token":
                TOKEN = data[1]
            elif data[0] == "guild_id":
                guild_id = int(data[1])
            elif data[0] == "channel_id":
                channel_id = int(data[1])
            elif data[0] == "server_logo":
                server_logo = data[1]
            elif data[0] == "max_player_count":
                max_count = data[1]

except FileNotFoundError:
    print(f"Dosya bulunamadı:settings.txt")
except IOError as e:
    print(f"Dosya okuma hatası: {e}")


import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime
import game_stat

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready.")


    #repeat functions
    while True:
        await setGameStat()
        await asyncio.sleep(60)  # Mesaj gönderme aralığı (saniye cinsinden)





#########################################
## Set Game Stat
#########################################
message_id = None  # Mesajın ID'si
async def setGameStat():

    count,staffs,vips,players = game_stat.getPlayerList()


    await bot.change_presence(activity=discord.Game(name=f"{server_name} {count}/{max_count}"))

    global message_id

    global guild_id 
    global channel_id 
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)

    current_datetime = datetime.now()
    date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    embed = discord.Embed(title=server_name+' Oyuncu Listesi', description=f'Tarih: {date}', color=discord.Color.green())
    embed.set_thumbnail(url=server_logo)
    embed.add_field(name='Yetkililer', value=staffs, inline=False)
    embed.add_field(name='Vipler', value=vips, inline=True)
    embed.add_field(name='Oyuncular', value=players, inline=True)

    if message_id is None:
        message = await channel.send(embed=embed)
        message_id = message.id
    else:
        message = await channel.fetch_message(message_id)
        await message.edit(embed=embed)






# Botu çalıştırın

bot.run(TOKEN)
