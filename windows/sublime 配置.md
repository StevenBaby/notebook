## 添加 Sublime Text3 到右键菜单

```
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\*\shell\Sublime Text 3]
@="Sublime Text 3"
"Icon"="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"

[HKEY_CLASSES_ROOT\*\shell\Sublime Text 3\command]
@="C:\\Program Files\\Sublime Text 3\\sublime_text.exe %1"
```
将上面的文字复制粘贴到文本文件 a.reg 中，双击导入即可，注意 C:\\Program Files\\Sublime Text 3\\sublime_text.exe 为文件路径

----

## Windows 10 输入法无法跟随光标 ##

下载下面的zip，解压放到菜单 Preferences > Browse Packages 出来的目录。重启Sublime就可以了

**注意：这个包无法用 Package Control 来安装**

<https://github.com/zcodes/IMESupport>

----

## 缩进改成4个空格 ##

     "tab_size": 4,

## 转换TAB为空格 ##

     "translate_tabs_to_spaces": true,

## 显示空白字符 ##

     "draw_white_space": "all",

## 主题

<https://github.com/dempfi/ayu>

## 转换行结尾格式 <sub> [1]</sub>

windows 文件的换行符为：[CR][LF]
Linux和Unix文件的换行符为：[LF]
有些需要转换使用，需要保证换行符为Unix形式才能使用。
其中一种办法是在linux系统中重新保存一份文件，或者使用vim命令 set ff=unix
在Sublime中，如何转换成Unix / Linux / Mac 换行符呢？

点击菜单 View -> Line Endings -> 选择需要的格式，然后保存即可。


## 参考资料
- [1] [windows和linux中换行符的转换](https://blog.csdn.net/quzhongxin/article/details/46476659)
