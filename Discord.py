# 类导入
import discord
# 内部文件
import FileRead_GetSecretData


def discord_bot():
    TOKEN = FileRead_GetSecretData.Discord_Bot_Toke()
    bot = discord.Bot()
    ch_ids = FileRead_GetSecretData.Discord_Bot_guildIDs()

    @bot.event
    async def on_ready():                               #初始化成功
        print(f"We have logged in as {bot.user}")

    @bot.command(name='stop')
    @bot.event
    async def on_message(message):                      #接收到消息
        if message.author == bot.user:
            return
        print(message)
        print(message.content)
        if message.content == "/help":
            await message.channel.send("/TestLink - 测试电脑连接状态")
        if message.content == "/TestLink":
            import datetime
            await message.channel.send(f"电脑处于连接状态<{datetime.datetime.now()}>")
        # await message.channel.send(timeNow)
        return

    @bot.slash_command(guild_id=ch_ids)
    async def help(ctx):                               #斜杠指令
        await ctx.respond("测试主机连接 - TestLink")





    bot.run(TOKEN)

discord_bot()