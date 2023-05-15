from datetime import datetime


def test() -> str:
    return "System is Online..." + str(datetime.now())


commandList = {"help": "test - 测试连接",
               "test": test()
               }
