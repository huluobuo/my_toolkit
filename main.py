from os import system
import json


try:
    from wget import download
except ImportError:
    system("python -m pip install wget")



class Toolkit:
    """
        主要的部分
    """

    def __init__(self):
        self.url = "https://github.com/huluobuo/my_toolkit/raw/refs/heads/master/my_toolkit.zip"
        self.save_path_and_name = ".\\my_toolkit.zip"            # 声明一下，仅支持Windows操作系统
        self.command_run_list = ["tar -xzvf my_toolkit.zip", "del my_toolkit.zip"]         # 我不道啊  [解压，删除]


    def get(self):
        #  获取必要的文件（from: https://github.com/huluobuo/my_toolkit/raw/refs/heads/master/my_toolkit.zip)

        print("正在获取必要的文件...")
        download(self.url, self.save_path_and_name)
        print("获取完毕！,准备解压文件...")

        #  解压文件
        print("正在解压文件...")
        system(self.command_run_list[0])
        print("解压完毕，正在清除残留文件")
        system(self.command_run_list[1])
        print("清除完毕，即将开始运行...")

    
    def check(self):
        try:
            with open(".\\tool_list.json", "r", encoding="UTF-8") as f:        # 不是，这编码真烦人！！！
                return [True, json.loads(f.read())]
        except FileNotFoundError:
            print("ERROR: 必要文件不存在，即将下载。")
            self.get()
            return [False, []]
        except json.decoder.JSONDecodeError:
            print("ERROR: 必要文件存在，但格式有误，即将重新下载。")
            self.get()
            return [False, []]
    
    def get_list(self, pt=False):    # pt => 是否打印（print）
        """
            返回一个列表，列表中的每个元素是一个列表，列表中的每个元素是一个列表
            返回格式 ：  [[序号, 路径], [序号, 路径], [序号, 路径]*****]
        """

        list_1 = self.check()
        if list_1[0] == True:
            print_serial = 1
            print_name = ''
            return_list = []           # {工具序号(int) ：  路径(str)，.........}

            #   tool_list.json =>  {"工具名称": ["路径", "备注"]}
            if pt == True:
                print("序号   | 工具名称                       |路径                                                |备注")
            for print_name in list_1[1]:
                if pt == True:
                    print("{:<6} | {:<30} | {:<50} | {:<10}".format(print_serial, print_name, list_1[1][print_name][0], list_1[1][print_name][1])) # 怎么这么复杂！！！
                return_list.append([print_serial, list_1[1][print_name][0]])
                print_serial += 1
            
            return return_list
        
    def run(self, serial):
        run_number = int(serial)
        a = self.get_list()
        if run_number > 0 and run_number <= len(self.get_list()):
            print("正在运行工具：{}".format(a[run_number - 1][1]))
            system(a[run_number - 1][1])
        else:
            print("ERROR: 序号错误，请重新输入。")
    
    def start(self):
        a = self.get_list(True)
        self.run(input("请输入序号："))




if __name__ == "__main__":
    toolkit = Toolkit()
    toolkit.start()

