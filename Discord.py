# 类导入
import discord

# 内部文件
import FileRead_GetSecretData
from Log import Log
import Discord_Commands

log = None


def discord_bot():
    # 安全防护
    if log is None:
        raise ValueError("log 未被设定")
    TOKEN = FileRead_GetSecretData.Discord_Bot_Toke()
    bot = discord.Bot()
    ch_ids = FileRead_GetSecretData.Discord_Bot_guildIDs()

    @bot.event
    async def on_ready():  # 初始化成功
        log.Record(f"logged in as {bot.user}", __name__)

    @bot.event
    async def on_message(message):  # 接收到消息
        # 防死循环
        if message.author == bot.user:
            return
        print(message)
        # print(message.content)
        reply = Discord_Commands.commandList.get(message.content, '<No corresponding command>')
        await message.channel.send(reply)
        log.Record(f"From\"{message.author}\" ; Get Message:\"{message.content}\"; Reply:\"{reply}\"",
                   "Discord_Commands")
        return

    # @bot.slash_command(guild_id=ch_ids)
    # async def help(ctx):                               #斜杠指令
    #     await ctx.respond("测试主机连接 - TestLink")

    bot.run(TOKEN)
