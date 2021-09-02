# Django - 模板渲染

```python
如果你创建一个 Template 对象，你可以用 context 来传递数据给它。 一个context是一系列变量和它们值的集合。

context在Django里表现为 Context 类，在django.template 模块里。 她的构造函数带有一个可选的参数：


一个字典映射变量和它们的值。 调用 Template 对象 的 render() 方法并传递context来填充模板


from django.template import  Template,Context


# Django Template Context 使用
def query(request):

    # 创建模板
    C_Template = Template("<h1>hello {{ name }}</h1>")

    # 实例化Context 生成模板
    C_Context = Context({"name": 123})

    C_Context = C_Template.render(C_Context)

    # Django 的render 就是实例化好 templates 静态文件，然后实例化Context 从而生成了最终的 浏览器能识别的内容调用HttpResponse返回

    print(C_Context)
    return  HttpResponse(C_Context)


```

