# Django - 静态文件

```python

# 如何在django中引用static资源文件


方式一:

1. 修改settings配置


	 STATIC_URL = '/static/'		// 别名配置， html 文件引用时会使用到这个名称
  
  
2. 添加static配置文件

   在django项目中创建一个static目录
  
   STATICFILES_DIRS = (
   
   		path.join(BASEDIR,<stati目录>)
   
   
   )

   
    
引用方式:
  
  
 方式一:
   
    <script> src="static/jquery.js"<script/>
    
    
 方式二:
  
  	jinjia 模板引用方式:
      
    {% load static %}
    <script type="text/javascript" src="{% static 'jq/jquery.js' %}"></script>
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <script type="text/javascript" src="{% static 'js/bootstrap.js' %}"></script>
```

