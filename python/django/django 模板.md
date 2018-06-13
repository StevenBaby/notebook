# django 模板

## context_processors 模板全局变量

一般情况下，django在渲染模板是需要 context 字典，里面存储了模板中需要的变量。View类中有 get_context_data 方法来添加或者删除变量。

这里有一种情况，就是所有的View都要用到的一些变量，这样在每个View中都写一下 get_context_data 就显得代码冗余了。

这时候可以使用 context_processors 来处理，在每次请求中都加入一些变量。

context_processors 是一个函数，返回一个字典，django 会把这个字典添加到 context 中。

假设我们在 app **hello** 中新建 python 文件 context_processors.py，其中声明如下函数。

```python 
def hello(request):
    context = {"current_time" : timezone.now()}
    return context
```

然后修改 **settings.py** 文件，修改如下，

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hello.context_processors.hello',
            ],
        },
    },
]
```

在 context_processeros， 列表中加入 **hello.context_processors.hello**, 这样就可以在 context 中自动加入 current_time 变量了，该变量可以在任意模板中使用。

---

## buildins 内建标签和过滤器

一个列表，列表中的元素是一个python点路径的字符串，用来从模板标签模块中添加 built-ins（内建）的标签。

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hello.context_processors.hello',
            ],
            'builtins': [
                'django.templatetags.i18n',
                'django.templatetags.static',
                'hello.builtins',
            ],
        },
    },
]
```

内建的标签和过滤器可以在不调用{% load %} 标签的情况下调用。如上所以，加入了 **django.templatetags.i18n** 和 **django.templatetags.static** 之后，就可以不用在模板中 load static 和 i18n 了。

builtins 是一个 python 文件，其中有名为 **register = template.Library()** 的变量。


## 内置标签

### slice 

返回列表分片，语法与Python分片相同

```python
{{ some_list|slice:":2" }}
```
