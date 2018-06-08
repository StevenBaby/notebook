# mariadb 

## ubuntu mariadb 无法登陆

给新机器Ubuntu安装的Mariadb后无法登录，通过网上各种方法修改root用户密码，仍然无法解决，耗费几个小时！

经过看日志和查手册，发现原因如下：

- ubuntu确实安装没有启用root用户，所以没有root用户密码，而新安装的mariadb使用的系统root的密码（初始安装后）
- 通过原来的方法重置password无效（原因就是采用了unix_socket认证）

那么，解决方法如下：
直接进入root用户下，就可以免密码登录！

如果，你希望采用原来的mysql密码方式，需要修改认证插件，方法如下：

```sql
update mysql.user set plugin='mysql_native_password' where user='root';
update mysql.user set password=password("您的密码") where user='root'; 
FLUSH PRIVILEGES;
```

对于CentOS，RedHat而言，使用root用户时，无需密码登录。
而且，也符合安全准则，新版本的MySQL密码会在日志中输出，MariaDB以前保持空密码，现在意味着，用root用户，无需登录。


## 参考资料

- [1][新版本Mariadb安装后无法登录问题的解决](https://blog.csdn.net/yin138/article/details/80293533)