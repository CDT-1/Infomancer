# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 15:23:14
# @Author  : Codete
# @FileName: main.py
# @IDE: PyCharm
# @E-Mail: CodeteMail@163.com
import sys
import CodeteLib as cl
import time as t
import gettext
import os
import http.server
import socketserver

cl.cls()

# Settings
if os.path.exists("data.imd") == False:
    with open("data.imd", "w", encoding="utf-8") as dataTemp:
        userLang = cl.getLanguage()
        dataTemp.write("language={}\nlevel=0".format(userLang))
with open("data.imd", "r", encoding="utf-8") as data1:
    d1 = data1.readlines()
    data = {}
    for d2 in d1:
        data[d2.split("=")[0]] = d2.split("=")[1].replace("\n", "")
    userLang = data['language']

lang = gettext.translation('IMTrans', localedir='.\\locales', languages=[userLang])
lang.install('IMTrans')
_ = lang.gettext

if data['level'] == '0':
    # Print Logo
    cl.cls()
    print(cl.CodeteLogo)
    t.sleep(5)
    cl.cls()
    print(cl.gameTitle)
    t.sleep(5)
    cl.cls()

    # Tips
    cl.cls()
    print(_("提示:"))
    print(_("1. 本游戏为关卡制游戏, 请确保您已经阅读了游戏规则"))
    print(_("2. 本游戏将会开启您的电脑的45678端口, 请确保您的电脑的45678端口未被占用"))
    print(_("3. 本游戏将会在您的电脑上开启一个HTTP服务器"))
    print(_("4. 本游戏将会在您的电脑中创建一些文件夹和文件"))
    print(_("5. 您可以在游玩本游戏的同时查看Github上的源代码, 但可能会影响游玩的体验"))
    print(_("6. 本游戏已在Github上开源, 如遇到bug, 请随时在Github上提交issue"))
    print(_("7. 如果您想查看本游戏的源代码, 请访问Github: https://github.com/CDT-1/Infomancer"))
    print(_("8. 如果您在游戏中遇到了困难, 可以查看Github上的教程"))
    print(_("9. 在一关结束后, 窗口会关闭, 请重新打开本游戏"))
    print(_("10. 祝您游戏愉快!"))
    print(_("11. 本提示将不会再次显示!!!!"))
    print()
    input(_("按回车键继续..."))
    cl.changeLevel(1)
    sys.exit(0)
else:
    cl.cls()
    print(_("---------- 开发中, 敬请期待 ----------"))
    input(_("按回车键继续..."))
    sys.exit(0)