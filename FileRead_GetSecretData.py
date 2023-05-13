


def Discord_Bot_guildIDs():
    import re
    with open("C:\Controller_Secret_settings\Discord_Bot_guildIDs.txt", 'r') as File_Discord_Bot_guildIDs:
        text = File_Discord_Bot_guildIDs.readlines()
        return [int(s) for s in text if re.match(r'^\d+$', s, re.MULTILINE)]


def Discord_Bot_Toke():
    with open("C:\Controller_Secret_settings\Discord_Bot_Token.txt", 'r') as File_Discord_Bot_Token:
        return File_Discord_Bot_Token.readline()


# 用于测试
if __name__ == '__main__':
    print(f"<Discord_Bot_guildIDs> {type(Discord_Bot_guildIDs())}: {Discord_Bot_guildIDs()}")
    print(f"<Discord_Bot_Toke> {type(Discord_Bot_Toke())} : {Discord_Bot_Toke()}")


