import os.path

if (not os.path.isfile('config.ini')):
    raise FileNotFoundError('配置文件 config.ini 未找到，请检查是否配置正确！')