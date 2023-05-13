import discord
import FileRead_GetSecretData

def discord_bot():
    TOKEN = FileRead_GetSecretData.Discord_Bot_Toke()
    bot = discord.Bot()
    ch_ids = FileRead_GetSecretData.Discord_Bot_guildIDs()

    @bot.event
    async def on_ready():                               #初始化成功
        print(f"We have logged in as {bot.user}")

    @bot.event
    async def on_message(message):                      #接收到消息
        if message.author == bot.user:
            return
        print(message)
        print(message.content)
        return

    @bot.slash_command(guild_id=ch_ids)
    async def hello(ctx):                               #斜杠指令
        await ctx.respond("Hello!")


    bot.run(TOKEN)

discord_bot()