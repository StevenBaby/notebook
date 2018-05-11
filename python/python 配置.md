# python 配置

## 配置pypi用户名密码 ##

修改配置文件  **~/.pypirc**

    [distutils]
    index-servers = pypi

    [pypi]
    username:username of yours
    password:password of yours

## pypi 打包上传命令

    python setup.py sdist bdist_wheel –universal
    python setup.py sdist bdist_wheel upload

## 修改 pip 源 ##

可以在 pip install 的时候直接加上

    pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple

或者 打开文件 **~/.pip/pip.conf**，写入下面的内容


    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple

一些源地址：

- 官方 <https://pypi.org/simple/>
- 清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple>
- 豆瓣 <http://pypi.douban.com/simple/>
