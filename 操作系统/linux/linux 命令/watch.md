# watch 周期性执行命令

watch是一个非常实用的命令，基本所有的Linux发行版都带有这个小工具，如同名字一样，watch可以帮你监测一个命令的运行结果，省得你一遍遍的手动运行。在Linux下，watch是周期性的执行下个程序，并全屏显示执行结果。你可以拿他来监测你想要的一切命令的结果变化，比如 tail 一个 log 文件，ls 监测某个文件的大小变化，看你的想象力了！

## 选项

<blockquote>
-n或--interval  watch缺省每2秒运行一下程序，可以用-n或-interval来指定间隔的时间。

-d或--differences  用-d或--differences 选项watch 会高亮显示变化的区域。 而-d=cumulative选项会把变动过的地方(不管最近的那次有没有变动)都高亮显示出来。

-t 或-no-title  会关闭watch命令在顶部的时间间隔,命令，当前时间的输出。
</blockquote>