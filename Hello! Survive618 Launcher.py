#必要信息
version = '0.1' #程序版本
#import
import os
import sys
import time
import json #import json字典
import atexit
import logging
import datetime
from plyer import notification
#创建日志文件夹
if not os.path.exists('.Survive618'):
    os.makedirs('.Survive618')
    create_rootdir_path = open('.Survive618//log.log', 'w')
    create_rootdir_path.write("")
    create_rootdir_path.close()
    exec(open("Hello! Survive618 Launcher.py", encoding="utf-8").read())
    logging.info('已创建 .Survive618 文件夹')
    logging.info('已创建 log.log 文件')
#主日志记录器
log_dir = '.Survive618' #设置目录
log_file = os.path.join(log_dir, 'log.log') #log文件(log.log)
logging.basicConfig(filename=log_file, level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s', encoding='utf-8')
#日志相关 - 检查项
program_path = os.path.dirname(__file__) #获取程序的运行路径
program_version = version #获取程序的版本号
program_running_datetime = datetime.datetime.now() #获取程序运行的时间
#日志相关 - 函数使用
def exit_handler(): #检测退出后写入日志：已退出
    program_running_datetime = datetime.datetime.now() #获取程序运行的时间
    logging.info(f"收到关闭指令，程序已正常退出 | 当前时间为：{program_running_datetime}")
#日志及配置相关 - 逐个运行
open('.Survive618//log.log', 'w') #删除旧日志
logging.info(f'[Start] 程序的运行路径为：{program_path}')
logging.info(f'[Start] 程序版本：{program_version}')
logging.info(f'[Start] 当前时间为：{program_running_datetime}')
#配置相关 - 创建
def create_default_config(): #创建一个字典，包含你想要存储在配置文件中的配置项
    config_data = {
        "download_from": "jsDelivr",
    }
    config_path = ".Survive618//config.json" #指定要写入的文件名
    with open(config_path, 'w') as json_file: #将字典写入 JSON 文件
        json.dump(config_data, json_file, indent=4)  #使用缩进使 JSON 文件更易读
if not os.path.isfile('.Survive618//config.json'): #没有就直接创建json配置文件
    create_default_config()
    logging.info(f'已创建日志文件 位置 {program_path}\\.Survive618\\config.json')
with open('.Survive618//config.json', 'r') as json_file:
    all_config = json.load(json_file)
logging.info('[Start] 当前配置文件为：\n%s',json.dumps(all_config, indent=4)) #经过格式化的json配置文件
#程序开始
def o(text): #直接使用等效于 print , 只是增加了暂停, 类似于 ChatGPT /0.05秒暂停/ [普通]
    for char in text:
        print(char, end='', flush=True)  # 使用 end='' 避免换行，flush=True 立即输出
        time.sleep(0.01)  # 暂停 0.05 秒
    print()

def input_o(prompt):
                o(prompt)  # 打印提示信息
                sys.stdout.flush()  # 刷新输出缓冲区
                return input()
#加载完毕，开始清屏进入交互界面
os.system('cls') #清屏
#进入交互界面
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # 指定通知显示的时间（秒）
    )
show_notification("欢迎使用！", "欢迎使用 Hello! Survive618 Launcher！")
o('欢迎使用 Hello! Survive618 Launcher！')
o('请选择你要执行的操作')
def root():
    root_select = input_o('输入[1]开始游戏, 输入[2]打开设置, 输入[3]退出 Hello! Survive618 Launcher.')
    if root_select == '1':
        if not os.path.isfile('.Survive618//Survive618.py'):
            Download_or_Close = input_o('你还没有安装 Survive618！是否需要下载？（是/否）')
            if Download_or_Close == '是': #下载并安装s618
                import requests
                with open('.Survive618//config.json', 'r') as json_file:
                    download_config = json.load(json_file)
                config_download_from = download_config["download_from"] #获取特定项的值: 自下载
                if config_download_from == 'jsDelivr':
                     Survive618_GitHub_url = "https://ad-closenn.github.io/Survive618/Survive618.py" #使用jsdelivr的cdn来加速下载
                if config_download_from == 'GitHub Pages':
                     Survive618_GitHub_url = "https://ad-closenn.github.io/Survive618/Survive618.py" #使用github pages的源站链接来下载
                o('正在下载 Survive618...')
                print('请稍候...')
                response = requests.get(Survive618_GitHub_url) #开始下载s618
                if response.status_code == 200:
                    with open('.Survive618//Survive618.py', 'wb') as f:
                        f.write(response.content)
                        print("文件下载成功！")
                        logging.info('[Download] Survive618 下载成功 状态码：' + str(response.status_code)) #写日志
                    root()
                else:
                    print(f"文件下载失败！请重试 [错误代码：{response.status_code}]")
                    logging.info('[Download] Survive618下载失败，错误代码：' + str(response.status_code)) #写日志
            if Download_or_Close == '否': #关闭启动器
                 exit()
        if os.path.isfile('.Survive618//Survive618.py'):
             o('已找到游戏')
             o('正在启动... 请稍后...')
             os.system('cls') #清屏，美化启动器及游戏本体
             logging.info('[Launch] 已启动游戏')
             os.system('python .Survive618//Survive618.py')
    if root_select == '2':
         print('未制作，敬请期待。')
         logging.warning('[未制作] root_select: [2]打开设置：未制作，敬请期待。')
         exit()
    if root_select == '3':
         exit()
    else:
         o('请选择三项中的一个！')
         os.system('cls') #清屏回到起点
         root()
#主程序
if __name__ == "__main__":
    atexit.register(exit_handler)
    root()