# scrapy 

## 创建项目

```shell
scrapy startproject tutorial
```

该命令将会创建包含下列内容的 tutorial 目录:

```text
tutorial/
    scrapy.cfg
    tutorial/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
```

这些文件分别是:

- scrapy.cfg: 项目的配置文件
- tutorial/: 该项目的python模块。之后您将在此加入代码。
- tutorial/items.py: 项目中的item文件.
- tutorial/pipelines.py: 项目中的pipelines文件.
- tutorial/settings.py: 项目的设置文件.
- tutorial/spiders/: 放置spider代码的目录.

