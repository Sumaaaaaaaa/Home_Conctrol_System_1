# 内部调用
from Log import Log
import Discord

# 设置
LogFilePath = "C:\\@ControlSystem_LOG"  # LOG文件地址设置


if __name__ == '__main__':

    # 创建log对象，并输出正常启动提示
    log = Log(LogFilePath)
    log.Record("Log system started successfully.", path="Log")

    # 设置Discord收发系统中的Log的地址（它会在启动bot时产生内部对象），并开启bot
    Discord.Set_Log_File_Path(LogFilePath)
    Discord.discord_bot()