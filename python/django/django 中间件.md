# django 中间件

中间件是用来处理django 请求/相应的框架，全局化修改输入和输出的，轻量级，底层插件系统。

每个中间件组件负载做一些特定的功能，例如，django 包含的一个中间件 **AuthenticationMiddleware** 它用session将用户和请求关联起来。

这个文章将解释中间件如何工作，怎样激活中间件，怎样写自己的中间件，Django附带一些内置的中间件，您可以立即使用它们。这里有他们的文档 [内置中间件参考](https://docs.djangoproject.com/en/2.0/ref/middleware/)

