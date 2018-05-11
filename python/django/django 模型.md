# django 模型

## 自定义数据库表名称

修改 Model 元数据

```python
class SomeModel(models.Model):

    # 定义表结构

    class Meta:
        db_table = 'mytable' # 修改表名称

```

---
