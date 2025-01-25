from os import system
try:
    from wget import download
except ImportError:
    system("python -m pip install wget")


def get():
    #  获取必要的文件（from: https://github.com/huluobuo/my_toolkit/raw/refs/heads/master/my_toolkit.zip)

    print("正在获取必要的文件...")
    # 这些变量有用吗？
    url = "https://github.com/huluobuo/my_toolkit/raw/refs/heads/master/my_toolkit.zip"
    save_path_and_name = ".\\my_toolkit.zip"            # 声明一下，仅支持Windows操作系统
    download(url, save_path_and_name)
    print("获取完毕！,准备解压文件...")

    #  解压文件
    print("正在解压文件...")
    system("tar -xzvf my_toolkit.zip")              # 我不道啊
    print("解压完毕，正在清除残留文件")
    system("del my_toolkit.zip")
    print("清除完毕，即将开始运行...")
