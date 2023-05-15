# 基本信息
# 【创建】
# 创建Log对象 => (LOG文件存储的文件夹地址.str)
# 【方法】
# Log对象.Record(content: str, path:str="?Unknow?", isError: bool = False)
# content:(必须)输出的文字内容；path:调用对象；isError:是错误提示吗？


# 库导入
import datetime
import os


# 关联文件


class Log(object):
    # 初始化函数
    def __init__(self, LogFilePath: str):
        # 需要输入一个LOG文件夹地址，若该地址错误会直接{ERROR结束程序}
        if os.path.exists(LogFilePath):
            self.LogFilePath = LogFilePath
        else:
            raise ValueError

    # Path:调用方; content:字符串输出内容 ; isError:是错误提示吗
    def Record(self, content: str, path: str = "?Unknow?", isError: bool = False):
        self.__Console_Print(content, path, isError)
        self.__File_Writing(content, path, isError)

    def __Console_Print(self, content, path, isError):
        if path == "?Unknow?": path = "\033[31m?Unknow?\033[0m"
        if isError:
            print(
                f"\033[31m/// E R R O R ///\033[0m <\033[92m{datetime.datetime.now()}\033[0m> "
                f"<\033[96m{path}\033[0m> : {content}")
        else:
            print(f"<\033[92m{datetime.datetime.now()}\033[0m> <\033[96m{path}\033[0m> : {content}")

    def __File_Writing(self, content, path, isError):
        filepath = f"{self.LogFilePath}\\{str(datetime.date.today())}.txt"
        with open(filepath, 'a', ) as file:
            if isError:
                file.write(f"<{datetime.datetime.now()}>\t"
                           f"<{path}>\t:\t{content}\t[ERROR]\n")
            else:
                file.write(f"<{datetime.datetime.now()}>\t<{path}>\t:\t{content}\n")
